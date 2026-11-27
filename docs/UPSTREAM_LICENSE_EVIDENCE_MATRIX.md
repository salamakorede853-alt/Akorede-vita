# Vita3K upstream licence evidence matrix

**Status:** preliminary evidence review — **release clearance not granted**  
**Upstream repository:** `Vita3K/Vita3K`  
**Pinned upstream revision:** `c87e12578749d6267be9b0c669904fe22545b170`  
**Evidence artifact:** `vita3k-license-evidence-c87e125` (GitHub Actions; 14-day retention at time of collection)  
**Evidence inventory:** 91 licence-related files; 40 recursive submodule status entries; 27,567 source-header notice matches.

## 1. Scope and interpretation

This matrix records what the collected evidence supports. It is not a legal opinion, a complete software bill of materials (SBOM), or proof that every listed dependency is compiled into either target. A discovered licence file may belong to tests, examples, tools, optional features, or a nested dependency. Conversely, absence of a licence file in this archive does not establish that code is unlicensed.

The evidence collector records licence-like files, selected source-header notice matches, and recursive submodule revisions. It does not determine the exact source files compiled, platform-specific dependency resolution, static versus dynamic linkage, or the contents of final distributed binaries. Those require separate Android and Windows build-graph and packaging reviews.

## 2. Component evidence matrix

| Component / scope | Evidence collected at pinned revision | Preliminary interpretation | Remaining verification |
|---|---|---|---|
| Vita3K main project | Root `COPYING.txt`; source-header notices | GPL-2.0 project licence evidence | Confirm all distributed project files and notices; prepare corresponding-source and build/install-script process for any distributed covered binaries |
| Capstone | `external/capstone/LICENSE.TXT`, `LICENSE_LLVM.TXT`; pinned submodule commit `022575848782a4801fd150fdbc927effcbca0864` | Main licence evidence is 3-clause BSD; separate LLVM-derived portions have separate licence evidence | Map compiled Capstone files to the applicable licence; preserve all required notices |
| dlmalloc | Pinned submodule `e98f4ee160380d7c39dc1f04e7488bcf0770d391`; source/header evidence from prior exact-revision review | Public-domain / CC0 dedication evidence was found in upstream source documentation | Confirm which files are actually compiled and retain provenance evidence |
| glslang | `external/glslang/LICENSE.txt`; pinned commit `fc9889c889561c5882e83819dcaffef5ed45529b` | Licence file explicitly describes multiple licences for glslang proper and its preprocessor | Identify exact compiled source groups and their licence terms; exclude optional/test/tool components only when build evidence confirms exclusion |
| FFmpeg fork | `external/ffmpeg/copyright`; pinned commit `eaf918c97e76d3fa7ec5bfea63a307fced559e76` | Collected copyright file identifies LGPL-2.1 | Verify exact FFmpeg source/configuration, enabled codecs, archive contents, static-linking arrangement, relinkability materials, notices, and corresponding source for each platform |
| substitute | `external/substitute/LICENSE.txt`; pinned commit `319da6b563d8da689f3b9df2fbb839edd41a1943` | General files are LGPL-2.1-or-later with an optional static-linking exception; file header notes identify `substrate.h` as LGPLv3 and `substitute.h`/generated files as public domain | Determine which files are built and whether the optional exception is relied upon; retain the relevant licence texts and notices |
| psvpfstools | Pinned commit `e9c5c7c4489a20ce2cb1a8b517caf00556594a12`; exact Git tree contains `.gitmodules`, `CMakeLists.txt`, and four nested submodule pointers, with no root licence/notice file | Root project licence is unresolved by this evidence set | Obtain authoritative licence/provenance evidence from maintainers or rights holders before redistribution; inspect exact compiled files |
| psvpfsparser | Pinned nested commit `05d43a06a6189302d31091c65e4fc8707476eef3`; exact GitHub contents listing for this commit contains source/header files plus `cmake` and `example`, but no root licence/notice file | Rights/licence status unresolved by this evidence set | Obtain authoritative licence/provenance evidence before redistribution |
| libzrif | Pinned nested commit `7d1e69bee7d2f08ea5754eff4463c041aacd49af`; no licence file collected | Rights/licence status unresolved by this evidence set | Obtain authoritative licence/provenance evidence before redistribution |
| libb64 | Pinned nested commit `3896b7a74c70baed0e2f6039a1dbd723e5d5cc8f`; `external/psvpfstools/libb64/LICENSE` | Copyright-only public-domain dedication text collected | Verify source provenance and which files are used |
| zlib nested under psvpfstools | Pinned nested commit `cb210089eb06453199578993566012493f6f7d21`; only a nested contrib licence file was collected | The archive does not contain the nested zlib root licence evidence | Obtain the root licence at the exact commit and verify whether this nested copy or a system zlib is selected |
| Boost | `external/boost/LICENSE_1_0.txt` and component copies; pinned commit `ff5f55bd97a93b23d6e5cb6d192290fb49b3f002` | Boost Software License 1.0 evidence collected | Resolve actual Android and Windows package/source selection and transitive component set |
| SDL | `external/sdl/LICENSE.txt` plus HIDAPI and other nested licence files; pinned commit `fa2c02bb6e21974a89ea9824bc53c9932abe5f9c` | Multiple licence/notice files exist in the SDL tree; do not treat the root file as covering every nested component | Identify platform-specific SDL sources and bundled HIDAPI/video components in each build |
| cubeb | `external/cubeb/LICENSE`, AUTHORS, and nested dependency licence files; pinned commit `4274d032355abe24cf6da0b35fad9b8122ea1f61` | Licence and attribution evidence collected, including nested components | Map platform audio backends and any bundled nested code to compiled files |
| spdlog / fmt | `external/spdlog/LICENSE`, `external/fmt/LICENSE`; pinned commits recorded in `audit-evidence.json` | MIT licence evidence collected for these projects | Confirm exact fmt source selection and include notices in distributions |
| yaml-cpp | `external/yaml-cpp/LICENSE`; pinned commit `56e3bb550c91fd7005566f19c079cb7a503223cf` | Licence file collected | Confirm runtime/build inclusion and preserve notice |
| xxHash | `external/xxHash/LICENSE`; pinned commit `e626a72bc2321cd320e953a0ccf1584cad60f363` | BSD-2-Clause licence evidence from prior exact-revision inspection | Map used source files and preserve notice |
| concurrentqueue | `external/concurrentqueue/LICENSE.md`; pinned commit `9afb99746f0f5fc94ac8aef737053ae0481ba8d1` | Dual Simplified BSD / Boost Software License 1.0 evidence; nested benchmark/test licences also present | Confirm selected licence and ensure benchmark/test-only components are not accidentally shipped |
| Tracy | `external/tracy/LICENSE`; pinned commit `f2a4f2529e7e71844c9e434b877770a21ecf7587` | BSD-3-Clause evidence from prior exact-revision inspection | Confirm whether Tracy is enabled or distributed in each configuration; review nested bundled components if included |
| LibAtrac9 | `external/LibAtrac9/LICENSE`; pinned commit `82767fe38823c32536726ea798f392b0b49e66b9` | MIT licence evidence collected | Confirm build inclusion and retain copyright/permission notice |

## 3. Exact-revision follow-up checks

- The `psvpfstools` tree at `e9c5c7c4489a20ce2cb1a8b517caf00556594a12` confirms the top level contains only `.gitmodules`, `CMakeLists.txt`, and the four nested submodule pointers; no root licence/notice file is present in that tree. The nested URLs are recorded in the collected `.gitmodules` evidence.
- The `psvpfsparser` tree at `05d43a06a6189302d31091c65e4fc8707476eef3` was checked directly. Its root listing contains source/header files and the `cmake` and `example` directories, but no root licence/notice file.
- The GitHub API redirected the historical `libzrif` and nested `zlib` repository URLs to repository IDs that the connected GitHub reader could not retrieve. Their licence status therefore remains **unverified**, not presumed absent or unlicensed.

## 4. Immediate blockers

1. **psvpfstools, psvpfsparser, and libzrif:** obtain authoritative rights/licence evidence. Do not assume they are unlicensed, and do not clear redistribution without evidence.
2. **Nested zlib:** collect the root licence at the pinned nested commit; the collected dotzlib contribution licence is not a substitute.
3. **FFmpeg:** verify the actual static archives and exact configure/build inputs. The licence file alone does not establish compliance for the binary distribution.
4. **glslang, Capstone, SDL, cubeb, substitute:** map the exact compiled source files to the correct licence and notices.
5. **Android and Windows:** produce separate resolved dependency inventories because system libraries, bundled libraries, optional features, and package-manager versions can differ.

## 5. Required next engineering task

Create a reproducible dependency-resolution report for each target:

- Record the exact upstream commit, recursive submodule commits, toolchain, CMake options, package-manager baseline, and resolved package versions.
- Capture verbose build/link commands or generated build-graph output.
- Record for each dependency whether it is compiled, linked statically, linked dynamically, supplied by the operating system, or excluded.
- Capture the final package contents and generate separate Android and Windows SBOMs.
- Link each shipped component to the applicable licence text and required notices.

Do not import the Vita3K core into AKOREDE VITA or distribute a derived binary until the unresolved rights questions and applicable GPL/LGPL distribution obligations have been reviewed. This is an engineering evidence gate, not legal advice.
