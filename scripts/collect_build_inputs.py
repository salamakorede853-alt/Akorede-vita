#!/usr/bin/env python3
"""Collect reproducible Vita3K build-input evidence for Android and Windows.

This inventories pinned configuration inputs and hashes them. It does not resolve
packages, compile the project, or certify licence compliance.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

if len(sys.argv) != 3:
    raise SystemExit("usage: collect_build_inputs.py UPSTREAM_DIR OUTPUT_DIR")

root = Path(sys.argv[1]).resolve()
out = Path(sys.argv[2]).resolve()
if not (root / ".git").exists():
    raise SystemExit(f"not a Git checkout: {root}")
out.mkdir(parents=True, exist_ok=True)

def git(*args: str) -> str:
    p = subprocess.run(
        ["git", "-C", str(root), *args],
        check=False, text=True, stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
    )
    return p.stdout.strip()

# Explicit paths plus narrowly scoped build/configuration file discovery.
selected: set[Path] = set()
explicit = [
    "CMakeLists.txt", "CMakePresets.json", "vcpkg.json",
    "vcpkg-configuration.json", "vcpkg-ports",
    ".gitmodules", "building.md", "README.md",
    "android", ".ci", ".github/workflows",
    "vita3k/CMakeLists.txt",
]
for item in explicit:
    p = root / item
    if p.is_file():
        selected.add(p)
    elif p.is_dir():
        for f in p.rglob("*"):
            if f.is_file() and not f.is_symlink() and ".git" not in f.parts:
                if f.name in {
                    "CMakeLists.txt", "CMakePresets.json", "vcpkg.json",
                    "vcpkg-configuration.json", "build.gradle",
                    "gradle.properties", "gradle-wrapper.properties",
                    "AndroidManifest.xml", "local.properties",
                } or f.suffix in {".yml", ".yaml", ".cmake", ".gradle", ".md", ".properties"}:
                    selected.add(f)

# Also capture root-level CMake modules and manifests.
for pattern in ("*.cmake", "vcpkg*.json", "*.yml", "*.yaml"):
    selected.update(p for p in root.glob(pattern) if p.is_file())

files_dir = out / "build-input-files"
records = []
for src in sorted(selected, key=lambda p: p.relative_to(root).as_posix().lower()):
    rel = src.relative_to(root)
    try:
        data = src.read_bytes()
    except OSError:
        continue
    dest = files_dir / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_bytes(data)
    records.append({
        "path": rel.as_posix(),
        "size_bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "evidence_copy": (Path("build-input-files") / rel).as_posix(),
    })

submodules = git("submodule", "status", "--recursive")
(out / "submodule-status.txt").write_text(
    (submodules + "\n") if submodules else "(no submodule status output)\n",
    encoding="utf-8",
)

metadata = {
    "upstream_repository": "https://github.com/Vita3K/Vita3K",
    "upstream_commit": git("rev-parse", "HEAD"),
    "upstream_commit_subject": git("log", "-1", "--format=%s"),
    "submodule_status": submodules.splitlines(),
    "configuration_file_count": len(records),
    "configuration_files": records,
    "targets_reviewed": ["Android", "Windows"],
    "limitations": [
        "This is a configuration-input inventory, not a resolved dependency graph.",
        "It does not run CMake configure, vcpkg resolution, Gradle dependency resolution, or compilation.",
        "Platform-specific package selection and static/dynamic linkage still require build logs and package inspection.",
        "File hashes make the captured inputs identifiable and repeatable.",
    ],
}
(out / "build-input-evidence.json").write_text(
    json.dumps(metadata, indent=2) + "\n", encoding="utf-8"
)
(out / "build-input-sha256.txt").write_text(
    "".join(f"{r['sha256']}  {r['path']}\n" for r in records),
    encoding="utf-8",
)

print(f"Upstream commit: {metadata['upstream_commit']}")
print(f"Configuration files captured: {len(records)}")
print(f"Recursive submodule entries: {len(metadata['submodule_status'])}")
print("Build-input evidence collected; package resolution and builds are separate steps.")
