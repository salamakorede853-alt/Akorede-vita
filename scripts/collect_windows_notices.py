#!/usr/bin/env python3
"""Collect third-party licence notices for the pinned Windows Vita3K build."""
from __future__ import annotations
import argparse, csv, hashlib, json, re, shutil
from pathlib import Path
NOTICE_NAMES = re.compile(r"^(license|licence|copying|notice|copyright|authors|patents)(\..*)?$", re.I)
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--upstream", type=Path, required=True)
    ap.add_argument("--vcpkg-installed", type=Path)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--commit", required=True)
    a = ap.parse_args()
    roots = [a.upstream] + ([a.vcpkg_installed] if a.vcpkg_installed and a.vcpkg_installed.exists() else [])
    a.output.mkdir(parents=True, exist_ok=True)
    records = []
    for root in roots:
        label = root.name or "source"
        for p in root.rglob("*"):
            if not p.is_file() or p.is_symlink() or ".git" in p.parts:
                continue
            if not (NOTICE_NAMES.match(p.name) or (p.name.lower() == "copyright" and "share" in p.parts)):
                continue
            try:
                data = p.read_bytes(); digest = hashlib.sha256(data).hexdigest()
                rel = p.relative_to(root).as_posix()
                dest = a.output / label / rel
                dest.parent.mkdir(parents=True, exist_ok=True); shutil.copy2(p, dest)
                records.append({"source_root":str(root),"source_path":rel,
                    "copied_path":dest.relative_to(a.output).as_posix(),
                    "size_bytes":len(data),"sha256":digest})
            except OSError:
                continue
    with (a.output / "NOTICE_INDEX.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["source_root","source_path","copied_path","size_bytes","sha256"])
        w.writeheader(); w.writerows(records)
    (a.output / "COLLECTION_METADATA.json").write_text(json.dumps({
        "upstream_commit":a.commit,"notice_file_count":len(records),
        "limitations":["Collected notices are evidence, not legal clearance.",
          "This does not map every notice to compiled or shipped objects.",
          "Unresolved licence questions remain; see UNRESOLVED_COMPONENTS.md."]}, indent=2)+"\n", encoding="utf-8")
    (a.output / "UNRESOLVED_COMPONENTS.md").write_text(
        "# Licence evidence still unresolved\n\n"
        "Authoritative licence/provenance evidence is still required for psvpfstools, psvpfsparser, "
        "and libzrif; root licence evidence for nested zlib; file-level mapping for mixed-licence "
        "components; and review of FFmpeg LGPL static-linking obligations. This directory is not release clearance.\n",
        encoding="utf-8")
    print(f"Collected {len(records)} licence/notice files.")
if __name__ == "__main__":
    main()
