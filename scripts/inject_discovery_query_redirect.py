#!/usr/bin/env python3
"""
Insert an early <head> script so ?discovery=true redirects to the sibling *.discovery.html
(same path, filename becomes foo.discovery.html). Skips *.discovery.html and files that already
contain the marker DISCOVERY_QUERY_REDIRECT.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

MARKER = "DISCOVERY_QUERY_REDIRECT"

SNIPPET = f"""    <script>
    /* {MARKER}: ?discovery=true → sibling .discovery.html */
    (function () {{
      try {{
        var q = new URLSearchParams(window.location.search);
        if (String(q.get("discovery")).toLowerCase() !== "true") return;
        var parts = window.location.pathname.split("/");
        var file = parts.pop() || "";
        if (!/\\.html$/i.test(file) || /\\.discovery\\.html$/i.test(file)) return;
        q.delete("discovery");
        var qs = q.toString();
        var nextFile = file.replace(/\\.html$/i, ".discovery.html");
        parts.push(nextFile);
        var target = parts.join("/") + (qs ? "?" + qs : "") + window.location.hash;
        window.location.replace(target);
      }} catch (e) {{}}
    }})();
    </script>
"""


def inject(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    if MARKER in text:
        return False
    m = re.search(r"<head[^>]*>", text, re.IGNORECASE)
    if not m:
        print(f"skip (no <head>): {path.relative_to(ROOT)}", file=sys.stderr)
        return False
    insert_at = m.end()
    new_text = text[:insert_at] + "\n" + SNIPPET + text[insert_at:]
    path.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    n = 0
    for p in sorted(ROOT.rglob("*.html")):
        if p.name.endswith(".discovery.html"):
            continue
        if inject(p):
            print("injected", p.relative_to(ROOT))
            n += 1
    print(f"done, injected {n} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
