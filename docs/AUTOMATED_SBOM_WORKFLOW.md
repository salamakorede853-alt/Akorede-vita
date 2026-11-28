# Automated platform SBOM workflow

The workflow is dispatched manually from GitHub Actions:

- Workflow: `.github/workflows/vita3k-platform-build-evidence.yml`
- Upstream: Vita3K commit `c87e12578749d6267be9b0c669904fe22545b170`
- SBOM format: CycloneDX JSON, generated with Anchore Syft via `anchore/sbom-action`

## Reports produced

The successful workflow run publishes a combined artifact named:

`akorede-vita-platform-sboms-and-third-party-notices`

It contains:

- `android-arm64/android-arm64.cyclonedx.json`
- `android-x86_64/android-x86_64.cyclonedx.json`
- `windows-x64/windows-x64.cyclonedx.json`
- `third-party-licence-notices/android/`
- `third-party-licence-notices/windows/`

The original Android and Windows evidence artifacts are also retained separately.

## What each SBOM scans

- Android ARM64: native shared libraries extracted from the APK's `lib/arm64-v8a/` directory.
- Android x86_64: native shared libraries extracted from the APK's `lib/x86_64/` directory.
- Windows x64: the built `Vita3K.exe` executable.

The Android reports are deliberately split by ABI rather than scanning the same universal APK twice. Each extracted ABI directory also includes a context manifest containing the upstream commit, APK hash, target ABI, and hashes of the extracted native libraries.

## Third-party licence notices

The notice collectors copy common licence/notice/copyright files from the pinned upstream source tree and, on Windows, the resolved vcpkg installed tree. The Android collector scans the upstream checkout, including the vcpkg-installed tree if it is located beneath that checkout.

Each notice directory contains:

- original notice files copied with their relative source paths preserved;
- `NOTICE_INDEX.csv` with source path, destination path, byte size, and SHA-256;
- `COLLECTION_METADATA.json` with source revision and limitations;
- `UNRESOLVED_COMPONENTS.md` listing known unresolved licence questions.

## Scope and limitations

These are **binary-focused preliminary SBOMs**, not proof of a complete dependency graph. Syft may not identify every statically linked library or source-level component from a native executable or shared object. The Android ABI reports enumerate the native shared objects extracted from the APK; statically linked code inside those objects may not appear as separate components. The Windows report scans the executable and may not reveal every static dependency.

The notice collector is an evidence-gathering utility. It does not determine which files were compiled or shipped, resolve ambiguous licence expressions, prove ownership, or certify legal compliance. Files with embedded notices or unusual names may not be discovered. Android vcpkg package notices are collected only if their installed tree is inside the upstream checkout; the Windows collector explicitly scans the x64 vcpkg installed tree.

A later release-grade SBOM pass must combine these reports with exact per-ABI vcpkg manifests, Gradle dependency resolution, build/link graphs, and final package contents. In particular, the current unresolved rights for psvpfstools, psvpfsparser, and libzrif, nested zlib licence evidence, mixed-licence source mapping, and FFmpeg LGPL static-linking obligations remain blockers.

**Release decision remains NOT CLEARED FOR REDISTRIBUTION.** This workflow automates evidence collection; it is not legal advice or release approval.
