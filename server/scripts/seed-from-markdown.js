/**
 * Seed `discovery_topics` and `discovery_questions` from **/*.discovery.md under the repo root.
 * Run from server/: npm run seed
 */

import "dotenv/config";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { MongoClient } from "mongodb";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const serverRoot = path.join(__dirname, "..");
const repoRoot = path.resolve(serverRoot, process.env.REPO_ROOT || "..");

const MONGODB_URI = process.env.MONGODB_URI;
const DB_NAME = process.env.DB_NAME || "datalog";

if (!MONGODB_URI) {
  console.error("Set MONGODB_URI in server/.env");
  process.exit(1);
}

/**
 * @param {string} md
 */
function parseDiscoveryMarkdown(md) {
  const titleMatch = md.match(/^#\s+(.+)$/m);
  const title = titleMatch ? titleMatch[1].trim() : "";

  const companionMatch = md.match(/\*\*Companion:\*\*\s*`([^`]+)`/);
  const companionHtml = companionMatch ? companionMatch[1].trim() : "";

  const idx = md.indexOf("## Ten open-ended questions");
  const tail = idx >= 0 ? md.slice(idx) : md;
  const lines = tail.split(/\r?\n/);
  const questions = [];
  for (const line of lines) {
    const m = line.match(/^\s*(\d+)\.\s+(.+)$/);
    if (m) questions.push({ order: Number(m[1]), question: m[2].trim() });
  }

  return { title, companionHtml, questions };
}

/**
 * @param {string} dir
 * @returns {AsyncGenerator<string>}
 */
async function* walkMarkdownFiles(dir) {
  const entries = await fs.readdir(dir, { withFileTypes: true });
  for (const e of entries) {
    const full = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (e.name === "node_modules" || e.name === ".git" || e.name === ".venv") continue;
      yield* walkMarkdownFiles(full);
    } else if (e.name.endsWith(".discovery.md")) {
      yield full;
    }
  }
}

async function main() {
  const files = [];
  for await (const f of walkMarkdownFiles(repoRoot)) {
    files.push(f);
  }
  files.sort();

  if (files.length === 0) {
    console.warn("No **/*.discovery.md under", repoRoot);
  }

  const client = new MongoClient(MONGODB_URI);
  await client.connect();
  const db = client.db(DB_NAME);
  const topics = db.collection("discovery_topics");
  const questions = db.collection("discovery_questions");

  await topics.createIndex({ slug: 1 }, { unique: true });
  await questions.createIndex({ topicSlug: 1, order: 1 });

  let topicCount = 0;
  let qCount = 0;

  for (const full of files) {
    const rel = path.relative(repoRoot, full).split(path.sep).join("/");
    const slug = rel.replace(/\.discovery\.md$/i, "");
    const md = await fs.readFile(full, "utf8");
    const parsed = parseDiscoveryMarkdown(md);

    const companionDefault = `${slug}.html`;
    const now = new Date();
    await topics.updateOne(
      { slug },
      {
        $set: {
          slug,
          title: parsed.title || slug,
          companionHtml: parsed.companionHtml || companionDefault,
          sourceMarkdown: rel,
          updatedAt: now,
        },
        $setOnInsert: { createdAt: now },
      },
      { upsert: true },
    );
    topicCount += 1;

    const removed = await questions.deleteMany({ topicSlug: slug });
    if (removed.deletedCount) console.log(`  ${slug}: replaced ${removed.deletedCount} existing questions`);

    if (parsed.questions.length === 0) {
      console.warn(`  ${slug}: no numbered questions found`);
      continue;
    }

    const docs = parsed.questions.map((q) => ({
      topicSlug: slug,
      topicTitle: parsed.title || slug,
      order: q.order,
      question: q.question,
      description: "",
      customerResponse: "",
      createdAt: now,
      updatedAt: now,
    }));

    await questions.insertMany(docs);
    qCount += docs.length;
    console.log(`  ${slug}: inserted ${docs.length} questions`);
  }

  await client.close();
  console.log(`Done. Topics touched: ${topicCount}, questions inserted: ${qCount}`);
}

main().catch((e) => {
  console.error(e);
  process.exit(1);
});
