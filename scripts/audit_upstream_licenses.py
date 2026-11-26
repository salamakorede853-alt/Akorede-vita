#!/usr/bin/env python3
"""Collect licence evidence from a pinned upstream checkout and its submodules.

This script inventories evidence only. It does not determine legal compatibility.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit("usage: audit_upstream_licenses.py UPSTREAM_DIR OUTPUT_DIR")

upstream = Path(sys.argv[1]).resolve()
output = Path(sys.argv[2]).resolve()
if not (upstream / ".git").exists():
    raise SystemExit(f"not a Git checkout: {upstream}")
output.mkdir(parents=True, exist_ok=True)
license_output = output / "license-files"
license_output.mkdir(exist_ok=True)

def git(*args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(upstream), *args],
        check=False, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return result.stdout.strip()

license_name = re.compile(
    r"^(LICENSE|LICENCE|COPYING|NOTICE|COPYRIGHT|AUTHORS|PATENTS)(?:[._-].*)?$",
    re.IGNORECASE,
)
source_suffixes = {
    ".c", ".cc", ".cpp", ".cxx", ".h", ".hh", ".hpp", ".hxx",
    ".m", ".mm", ".s", ".S", ".py", ".rs", ".java",
}
header_markers = re.compile(
    r"SPDX-License-Identifier|copyright|licensed under|permission is hereby|"
    r"redistribution and use|all rights reserved|gnu general public license|"
    r"apache license|mozilla public license",
    re.IGNORECASE,
)

license_records = []
header_records = []
for path in upstream.rglob("*"):
    if not path.is_file() or path.is_symlink():
        continue
    relative = path.relative_to(upstream)
    if ".git" in relative.parts:
        continue
    if license_name.match(path.name):
        try:
            data = path.read_bytes()
        except OSError:
            continue
        digest = hashlib.sha256(data).hexdigest()
        destination = license_output / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
        license_records.append({
            "path": relative.as_posix(),
            "size_bytes": len(data),
            "sha256": digest,
            "evidence_copy": (Path("license-files") / relative).as_posix(),
        })
    if path.suffix in source_suffixes:
        try:
            if path.stat().st_size > 2_000_000:
                continue
            lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        except OSError:
            continue
        for number, line in enumerate(lines[:80], start=1):
            if header_markers.search(line):
                header_records.append({
                    "path": relative.as_posix(),
                    "line": number,
                    "text": line.strip()[:500],
                })

submodule_status = git("submodule", "status", "--recursive")
(output / "submodule-status.txt").write_text(
    (submodule_status + "\n") if submodule_status else "(no submodule status output)\n",
    encoding="utf-8",
)
gitmodules = git("config", "--file", ".gitmodules", "--list")
(output / "gitmodules-config.txt").write_text(
    (gitmodules + "\n") if gitmodules else "(no .gitmodules entries)\n",
    encoding="utf-8",
)
(output / "source-header-notices.json").write_text(
    json.dumps(header_records, indent=2) + "\n", encoding="utf-8"
)

metadata = {
    "upstream_path": str(upstream),
    "upstream_commit": git("rev-parse", "HEAD"),
    "submodule_status": submodule_status.splitlines(),
    "license_file_count": len(license_records),
    "license_files": sorted(license_records, key=lambda item: item["path"].lower()),
    "source_header_notice_count": len(header_records),
    "scope_note": (
        "Evidence inventory only. Filename matches and source-header excerpts are not "
        "legal conclusions. Review exact compiled files and each applicable licence."
    ),
}
(output / "audit-evidence.json").write_text(
    json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
)
(output / "license-file-list.txt").write_text(
    "".join(record["path"] + "\n" for record in sorted(
        license_records, key=lambda item: item["path"].lower()
    )),
    encoding="utf-8",
)

print(f"Upstream commit: {metadata['upstream_commit']}")
print(f"Licence/notice candidates copied: {len(license_records)}")
print(f"Source-header notice matches: {len(header_records)}")
print("Evidence inventory complete; human review is still required.")
