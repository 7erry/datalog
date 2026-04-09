import "dotenv/config";
import path from "node:path";
import { fileURLToPath } from "node:url";
import cors from "cors";
import express from "express";
import { ObjectId } from "mongodb";
import { getClient, getDb } from "./db.js";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const serverRoot = path.join(__dirname, "..");
const repoRoot = path.resolve(serverRoot, process.env.REPO_ROOT || "..");

const MONGODB_URI = process.env.MONGODB_URI;
const DB_NAME = process.env.DB_NAME || "datalog";
const PORT = Number(process.env.PORT) || 3000;

if (!MONGODB_URI) {
  console.error("Missing MONGODB_URI. Copy server/.env.example to server/.env and set your Atlas URI.");
  process.exit(1);
}

const app = express();
app.use(cors());
app.use(express.json({ limit: "1mb" }));

/** Serve static demo site and admin UI from repo root. */
app.use(express.static(repoRoot));

/**
 * @param {import('mongodb').Db} db
 */
function questionsCollection(db) {
  return db.collection("discovery_questions");
}

/**
 * @param {import('mongodb').Db} db
 */
function topicsCollection(db) {
  return db.collection("discovery_topics");
}

app.get("/api/health", (_req, res) => {
  res.json({ ok: true, db: DB_NAME });
});

/** List discovery topics (slug + title) sorted by slug. */
app.get("/api/discovery/topics", async (_req, res) => {
  try {
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const topics = await topicsCollection(db)
      .find({})
      .project({ slug: 1, title: 1, companionHtml: 1, updatedAt: 1 })
      .sort({ slug: 1 })
      .toArray();
    res.json({ topics });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to list topics" });
  }
});

/** All questions for a topic, ordered. */
app.get("/api/discovery/topics/:slug/questions", async (req, res) => {
  try {
    const slug = req.params.slug;
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const items = await questionsCollection(db)
      .find({ topicSlug: slug })
      .sort({ order: 1 })
      .toArray();
    res.json({ topicSlug: slug, questions: items });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to load questions" });
  }
});

/** Create a new question on a topic (order defaults to last + 1). */
app.post("/api/discovery/topics/:slug/questions", async (req, res) => {
  try {
    const slug = req.params.slug;
    const { question, description, customerResponse, order } = req.body || {};
    if (!question || typeof question !== "string") {
      res.status(400).json({ error: "Field `question` (string) is required" });
      return;
    }
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const col = questionsCollection(db);
    let nextOrder = order;
    if (typeof nextOrder !== "number" || Number.isNaN(nextOrder)) {
      const last = await col.find({ topicSlug: slug }).sort({ order: -1 }).limit(1).toArray();
      nextOrder = last.length ? last[0].order + 1 : 1;
    }
    const topic = await topicsCollection(db).findOne({ slug });
    const now = new Date();
    const doc = {
      topicSlug: slug,
      topicTitle: topic?.title || slug,
      order: nextOrder,
      question: question.trim(),
      description: typeof description === "string" ? description : "",
      customerResponse: typeof customerResponse === "string" ? customerResponse : "",
      createdAt: now,
      updatedAt: now,
    };
    const r = await col.insertOne(doc);
    res.status(201).json({ _id: r.insertedId, ...doc });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to create question" });
  }
});

/** Update question text, seller description, or customer response. */
app.patch("/api/discovery/questions/:id", async (req, res) => {
  try {
    const id = req.params.id;
    if (!ObjectId.isValid(id)) {
      res.status(400).json({ error: "Invalid id" });
      return;
    }
    const { question, description, customerResponse, order } = req.body || {};
    const patch = { updatedAt: new Date() };
    if (typeof question === "string") patch.question = question;
    if (typeof description === "string") patch.description = description;
    if (typeof customerResponse === "string") patch.customerResponse = customerResponse;
    if (typeof order === "number" && !Number.isNaN(order)) patch.order = order;
    if (Object.keys(patch).length <= 1) {
      res.status(400).json({ error: "No valid fields to update" });
      return;
    }
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const col = questionsCollection(db);
    const oid = new ObjectId(id);
    const ur = await col.updateOne({ _id: oid }, { $set: patch });
    if (ur.matchedCount === 0) {
      res.status(404).json({ error: "Question not found" });
      return;
    }
    const doc = await col.findOne({ _id: oid });
    res.json(doc);
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to update question" });
  }
});

app.delete("/api/discovery/questions/:id", async (req, res) => {
  try {
    const id = req.params.id;
    if (!ObjectId.isValid(id)) {
      res.status(400).json({ error: "Invalid id" });
      return;
    }
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const r = await questionsCollection(db).deleteOne({ _id: new ObjectId(id) });
    if (r.deletedCount === 0) {
      res.status(404).json({ error: "Question not found" });
      return;
    }
    res.status(204).end();
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to delete question" });
  }
});

/** Text bundle for future RAG: each answered question as a chunk. */
app.get("/api/discovery/topics/:slug/rag-context", async (req, res) => {
  try {
    const slug = req.params.slug;
    const mongo = await getClient(MONGODB_URI);
    const db = getDb(mongo, DB_NAME);
    const items = await questionsCollection(db).find({ topicSlug: slug }).sort({ order: 1 }).toArray();
    const chunks = items.map((q) => ({
      id: String(q._id),
      order: q.order,
      text: `Q: ${q.question}\nContext: ${q.description || "(none)"}\nCustomer: ${q.customerResponse || "(not captured)"}`,
    }));
    res.json({ topicSlug: slug, chunks });
  } catch (err) {
    console.error(err);
    res.status(500).json({ error: "Failed to build RAG context" });
  }
});

app.listen(PORT, () => {
  console.log(`datalog API http://localhost:${PORT}`);
  console.log(`Admin UI   http://localhost:${PORT}/discovery-admin.html`);
  console.log(`Static site from ${repoRoot}`);
});
