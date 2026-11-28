# AKOREDE VITA — Platform SBOM and release gate

**Status:** preliminary platform SBOM evidence captured; **not cleared for redistribution**  
**Upstream:** `Vita3K/Vita3K`  
**Pinned upstream revision:** `c87e12578749d6267be9b0c669904fe22545b170`  
**Evidence:** GitHub Actions run #4, commit `fa235085e1176f36cbc4ed5ad6a7c4d8a21f53f5`  
**Evidence artifacts:** `vita3k-android-build-evidence-c87e125` and `vita3k-windows-build-evidence-c87e125`

## 1. Build verification result

The uploaded evidence archives support these conclusions:

| Target | Evidence | Result |
|---|---|---|
| Android ARM64 | Gradle task `buildCMakeRelWithDebInfo[arm64-v8a]`; linked `libVita3K.so`; APK packaging completed | Passed |
| Android x86_64 | Gradle task `buildCMakeRelWithDebInfo[x86_64]`; linked `libVita3K.so`; APK packaging completed | Passed |
| Android package | `assembleReldebug`; `BUILD SUCCESSFUL`; inventory reports `app-reldebug.apk` (104,442,510 bytes) | Passed; RelDebug, not a production Release |
| Windows x64 | Linked `bin/Release/Vita3K.exe` | Passed |
| Windows tests | `cheat`, `mem`, `module`, `util` | 4/4 passed |

These are upstream build results. They do not demonstrate runtime compatibility on a physical device, Helio G100 performance, game compatibility, or integration into AKOREDE VITA. The uploaded archives contain build evidence, not the APK/EXE binaries themselves.

## 2. Resolved package-manager dependencies

The vcpkg output from both platforms reports the same direct package families and versions:

| Package | Resolved version in build evidence | Licence expression reported by vcpkg |
|---|---:|---|
| Boost modules (including icl, program-options, variant and transitive Boost modules) | 1.90.0#1 | BSL-1.0 |
| curl | 8.19.0 | curl AND ISC AND BSD-3-Clause |
| OpenSSL | 3.6.1#3 | Apache-2.0 |
| zlib | 1.3.1 | Zlib |

The vcpkg install output also reports helper ports such as `vcpkg-cmake`, `vcpkg-cmake-config`, `vcpkg-cmake-get-vars`, and `vcpkg-boost`. These are build/package-management support ports and must be distinguished from runtime components in a formal SBOM.

**Important Android architecture detail:** the build log separately shows vcpkg resolving `arm64-android` and `x64-android` triplets. Gradle's native build tasks compile both `arm64-v8a` and `x86_64`. The standalone `vcpkg-installed-packages.txt` snapshot is not a complete per-ABI pair of manifests; it shows only one installed-tree snapshot. Therefore it must not be treated as the complete Android dependency inventory for both ABIs.

**Important Windows detail:** the Windows package inventory uses `x64-windows-static-md`. The log includes a warning that the vcpkg executable detected `C:\\vcpkg` and ignored a mismatched `VCPKG_ROOT` value. The build completed, but the environment should be normalized in a later reproducibility pass.

The evidence files do not provide a complete per-component license-text archive or a full mapping from every resolved package to final linked objects. The table above is a resolved package summary, not a claim that the full dependency graph is cleared.

## 3. Pinned upstream components requiring licence mapping

The recursive submodule evidence records 40 entries including nested submodules. The following components are known to be relevant to the prior licence review and must remain in the platform SBOM/notice mapping:

| Component | Pinned revision | Current evidence status |
|---|---|---|
| Vita3K main project | `c87e12578749d6267be9b0c669904fe22545b170` | GPL-2.0; corresponding-source and notice obligations must be planned |
| FFmpeg fork | `eaf918c97e76d3fa7ec5bfea63a307fced559e76` | LGPL-2.1 evidence; static archives are linked; relinkability/source/notice compliance unresolved |
| psvpfstools | `e9c5c7c4489a20ce2cb1a8b517caf00556594a12` | Root licence/provenance unresolved |
| psvpfsparser | `05d43a06a6189302d31091c65e4fc8707476eef3` | Root licence/provenance unresolved |
| libzrif | `7d1e69bee7d2f08ea5754eff4463c041aacd49af` | Licence not verified at pinned revision |
| nested zlib | `cb210089eb06453199578993566012493f6f7d21` | Root licence evidence not captured; confirm nested versus system selection |
| libb64 | `3896b7a74c70baed0e2f6039a1dbd723e5d5cc8f` | Public-domain dedication text found; confirm provenance and use |
| substitute | `319da6b563d8da689f3b9df2fbb839edd41a1943` | Mixed LGPL/public-domain file notices; map exact compiled files and exception use |
| glslang | `fc9889c889561c5882e83819dcaffef5ed45529b` | Multiple licence sections; map compiled source groups |
| Capstone | `022575848782a4801fd150fdbc927effcbca0864` | BSD-3-Clause and separate LLVM-derived licence evidence; map compiled files |

Other reviewed components and evidence are recorded in [UPSTREAM_LICENSE_EVIDENCE_MATRIX.md](UPSTREAM_LICENSE_EVIDENCE_MATRIX.md). The matrix is an evidence inventory, not a complete SPDX/CycloneDX SBOM.

## 4. FFmpeg special review

The pinned FFmpeg fork identifies LGPL-2.1. The upstream build configuration downloads prebuilt FFmpeg libraries and links static archives, including `avformat`, `avcodec`, `swscale`, `avutil`, `avfilter`, and `swresample`. The current evidence also shows FFmpeg prebuilt archives being downloaded during Android and Windows builds.

Before redistributing either platform binary, the compliance review must establish:
- the exact FFmpeg source revision and patch set used to create the archives;
- the exact configure options and enabled codecs/features;
- the complete corresponding FFmpeg source and build scripts;
- how recipients can relink the application with a modified LGPL library, or another compliant arrangement;
- all required notices and licence texts; and
- whether any optional FFmpeg build choices introduce additional licence terms.

The current logs alone do not prove that these requirements have been met.

## 5. SBOM completeness assessment

**What is complete enough to record now**
- Exact upstream Vita3K commit.
- Recursive submodule commit inventory.
- Android and Windows build outcomes.
- Android ABIs built and Windows target architecture.
- Resolved vcpkg package versions shown in the logs.
- Initial licence evidence and named unresolved licence blockers.

**What is still missing for a release-grade SBOM**
- A complete dependency graph per target and per Android ABI, including non-vcpkg dependencies.
- Exact versions/commits for every fetched or bundled dependency and build tool.
- A reliable distinction between build-only, test-only, optional, and shipped runtime components.
- Per-component licence expressions linked to the exact licence text and copyright notices.
- A final link/package manifest showing which libraries are statically or dynamically included in each binary.
- A machine-readable SPDX or CycloneDX document generated from and checked against the final release artifacts.

Accordingly, this document is a **preliminary SBOM and release-readiness report**, not a claim of complete SBOM generation or legal clearance.

## 6. Release gate

**Decision: NOT CLEARED FOR REDISTRIBUTION.**

Blocking items:
1. Obtain authoritative licence/provenance evidence for psvpfstools, psvpfsparser, and libzrif at the exact pinned revisions.
2. Capture the root licence for the nested zlib revision and determine whether that copy is used.
3. Complete FFmpeg LGPL static-linking compliance review for Android and Windows.
4. Map exact compiled source files for mixed-licence components such as glslang, Capstone, and substitute.
5. Generate final per-platform/per-ABI SBOMs from the resolved build graph and release binaries.
6. Prepare GPL-2.0 corresponding-source, modification notices, licence bundle, and build/install scripts for any distributed Vita3K-derived binaries.
7. Obtain qualified legal review before public or commercial distribution.

This is an engineering evidence gate, not legal advice. Do not distribute a Vita3K-derived APK or EXE until the applicable rights and licence obligations are resolved.

## 7. Automated SBOM workflow

An automated CycloneDX JSON workflow has been added to `.github/workflows/vita3k-platform-build-evidence.yml`. It generates separate Android ARM64 and Android x86_64 reports from native shared libraries extracted from the built APK, plus a Windows x64 report from the built `Vita3K.exe`. It also collects third-party licence/notice files and packages all three reports with the notice directories into the `akorede-vita-platform-sboms-and-third-party-notices` artifact.

See [AUTOMATED_SBOM_WORKFLOW.md](AUTOMATED_SBOM_WORKFLOW.md) for the exact scope, outputs, and limitations. These are binary-focused preliminary SBOMs: statically linked components may not be individually discoverable, and the notice collection does not establish which components were shipped or clear their licences.

The workflow must be run successfully before treating the three reports and notice bundle as generated evidence. The release gate remains **NOT CLEARED FOR REDISTRIBUTION**.
