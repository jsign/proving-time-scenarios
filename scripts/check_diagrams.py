#!/usr/bin/env python3
"""Validate editable diagram sources, SVG exports, and Markdown references."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from xml.etree import ElementTree


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DIAGRAMS = DOCS / "diagrams"


def main() -> int:
    errors: list[str] = []
    sources = {path.stem: path for path in DIAGRAMS.glob("*.excalidraw")}
    exports = {path.stem: path for path in DIAGRAMS.glob("*.svg")}

    for path in sorted(sources.values()):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            errors.append(f"Invalid Excalidraw JSON: {path.relative_to(ROOT)}: {error}")

    for path in sorted(exports.values()):
        try:
            ElementTree.parse(path)
        except (OSError, ElementTree.ParseError) as error:
            errors.append(f"Invalid SVG XML: {path.relative_to(ROOT)}: {error}")

    for stem in sorted(sources.keys() - exports.keys()):
        errors.append(f"Missing SVG export for {sources[stem].relative_to(ROOT)}")

    for stem in sorted(exports.keys() - sources.keys()):
        errors.append(f"Missing Excalidraw source for {exports[stem].relative_to(ROOT)}")

    markdown = "\n".join(
        path.read_text(encoding="utf-8") for path in sorted(DOCS.rglob("*.md"))
    )
    for stem, path in sorted(exports.items()):
        if path.name not in markdown:
            errors.append(f"Unreferenced diagram export: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(sources)} Excalidraw/SVG diagram pairs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
