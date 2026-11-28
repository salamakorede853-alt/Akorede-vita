#!/usr/bin/env python3
"""Prepare per-ABI Android SBOM inputs and collect third-party licence notices."""
from __future__ import annotations
import argparse, csv, hashlib, json, re, shutil, zipfile
from pathlib import Path

NOTICE_NAMES = re.compile(r"^(license|licence|copying|notice|copyright|authors|patents)(\\..*)?$", re.I)

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

def collect_notices(roots, output: Path, commit: str):
    output.mkdir(parents=True, exist_ok=True)
    records, seen = [], set()
    for root in roots:
        if not root.exists():
            continue
        label = root.name or "source"
        for p in root.rglob("*"):
            if not p.is_file() or p.is_symlink() or ".git" in p.parts:
                continue
            if not (NOTICE_NAMES.match(p.name) or (p.name.lower() == "copyright" and "share" in p.parts)):
                continue
            try:
                digest, rel = sha256(p), p.relative_to(root).as_posix()
                if (label, digest) in seen:
                    continue
                seen.add((label, digest))
                dest = output / label / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(p, dest)
                records.append({"source_root": str(root), "source_path": rel,
                    "copied_path": dest.relative_to(output).as_posix(),
                    "size_bytes": p.stat().st_size, "sha256": digest})
            except OSError:
                continue
    with (output / "NOTICE_INDEX.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["source_root","source_path","copied_path","size_bytes","sha256"])
        w.writeheader(); w.writerows(records)
    (output / "COLLECTION_METADATA.json").write_text(json.dumps({
        "upstream_commit": commit, "notice_file_count": len(records),
        "limitations": [
            "Collected files are evidence, not a legal conclusion or proof of complete notice coverage.",
            "Files with different names or embedded-only notices may not be detected.",
            "Unresolved component rights remain unresolved and are listed in UNRESOLVED_COMPONENTS.md.",
            "Build-only, test-only, optional, and shipped components are not fully distinguished."
        ]}, indent=2) + "\n", encoding="utf-8")
    (output / "UNRESOLVED_COMPONENTS.md").write_text(
        "# Licence evidence still unresolved\n\n"
        "Do not treat this notice bundle as release clearance. The audit still requires authoritative "
        "licence/provenance evidence for psvpfstools, psvpfsparser, and libzrif; root licence evidence "
        "for nested zlib; exact file-to-licence mapping for mixed-licence components; and an FFmpeg "
        "LGPL static-linking compliance review. See the platform SBOM release-gate report.\n",
        encoding="utf-8")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--apk", type=Path, required=True)
    ap.add_argument("--upstream-commit", required=True)
    ap.add_argument("--sbom-input-dir", type=Path, required=True)
    ap.add_argument("--notice-output", type=Path, required=True)
    ap.add_argument("--notice-root", type=Path, action="append", default=[])
    a = ap.parse_args()
    if not a.apk.is_file():
        raise SystemExit(f"APK not found: {a.apk}")
    with zipfile.ZipFile(a.apk) as zf:
        names = zf.namelist()
        for abi, folder in (("arm64-v8a","android-arm64"),("x86_64","android-x86_64")):
            prefix = f"lib/{abi}/"
            selected = [n for n in names if n.startswith(prefix) and not n.endswith("/")]
            if not selected:
                raise SystemExit(f"No native libraries for {abi} in {a.apk}")
            dest = a.sbom_input_dir / folder
            dest.mkdir(parents=True, exist_ok=True)
            libs = []
            for name in selected:
                rel = Path(name).relative_to(prefix)
                target = dest / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                data = zf.read(name); target.write_bytes(data)
                libs.append({"path": name, "sha256": hashlib.sha256(data).hexdigest()})
            (dest / "sbom-input-context.json").write_text(json.dumps({
                "target": abi, "upstream_commit": a.upstream_commit,
                "apk": a.apk.name, "apk_sha256": sha256(a.apk),
                "scope": "Native shared libraries extracted from the built APK; statically linked components may not be individually detectable.",
                "libraries": libs
            }, indent=2) + "\n", encoding="utf-8")
    collect_notices(a.notice_root, a.notice_output, a.upstream_commit)
    print(f"Prepared Android ABI SBOM inputs from {a.apk}")

if __name__ == "__main__":
    main()
