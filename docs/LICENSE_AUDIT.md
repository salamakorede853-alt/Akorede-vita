# AKOREDE VITA — Third-Party Licence Audit

**Audit date:** 2026-11-26  
**Status:** Preliminary inventory only — NOT legal clearance  
**Upstream:** [Vita3K/Vita3K](https://github.com/Vita3K/Vita3K)  
**Reviewed upstream commit:** `c87e12578749d6267be9b0c669904fe22545b170`  
**Commit date:** 2026-11-26

## 1. Executive result

Vita3K's repository metadata identifies the main project as **GNU GPL version 2.0 (GPL-2.0)**. The repository includes `COPYING.txt`, containing the GPL v2 licence text.

This licence permits modification and redistribution, including commercial redistribution, but imposes conditions. In particular, distributing a covered executable requires providing the corresponding source under the GPL-compatible terms, preserving copyright/licence notices, and marking modified files and their modification dates. A distributed derivative work based on the GPL program must be licensed as a whole under GPL v2, subject to the licence's terms and exceptions.

**Current decision: conditional go for further investigation; no permission to treat the dependency stack as cleared.** No Vita3K source has been copied into AKOREDE VITA as part of this audit.

This is an engineering inventory, not legal advice. Before public or commercial distribution, obtain qualified legal review of the actual source tree, binary composition, distribution method, and applicable jurisdictions.

## 2. Main project licence

| Item | Finding |
|---|---|
| Project | Vita3K |
| Repository licence metadata | GNU GPL v2.0; SPDX reported by GitHub as `GPL-2.0` |
| Licence file | `COPYING.txt` |
| Reviewed revision | `c87e12578749d6267be9b0c669904fe22545b170` |
| Distribution consequence | If we distribute a covered Vita3K-derived executable, we must meet GPL v2 source, notice, licence, and downstream-rights requirements |

Important practical requirements to plan for:

- Include the full GPL v2 licence text with distributed copies.
- Preserve upstream copyright notices and warranty disclaimers.
- Mark modified upstream files prominently with the fact and date of modification.
- Provide the complete corresponding machine-readable source for distributed binaries, including the relevant modules, interface files, and build/install scripts as required by GPL v2.
- Do not impose extra restrictions that take away recipients' GPL rights.
- Keep a clear record of the exact upstream revision and every local patch.
- Do not assume a separate launcher, process, JNI boundary, renamed app, or new UI automatically makes the emulator code legally independent. The actual relationship and distribution arrangement need legal review.

## 3. Pinned upstream submodules and first-pass licence metadata

The following submodule commit IDs were read from the Git tree for the reviewed Vita3K commit. Licence labels below are repository-level GitHub licence metadata, not a substitute for reading the licence file at the exact pinned commit.

| Submodule | Pinned commit | Repository licence metadata | Audit status |
|---|---|---|---|
| boost | `ff5f55bd97a93b23d6e5cb6d192290fb49b3f002` | BSL-1.0 | Verify exact revision and notices |
| capstone | `022575848782a4801fd150fdbc927effcbca0864` | No SPDX licence detected | **Manual review required** |
| dirent | `31db6474b5231c180bd4618c8c90e43af50c86d0` | MIT | Verify exact revision and notices |
| dlmalloc | `e98f4ee160380d7c39dc1f04e7488bcf0770d391` | No SPDX licence detected | **Manual review required** |
| ffmpeg | `eaf918c97e76d3fa7ec5bfea63a307fced559e76` | LGPL-2.1 | Review fork changes and build configuration |
| glslang | `fc9889c889561c5882e83819dcaffef5ed45529b` | NOASSERTION | **Manual review required** |
| googletest | `52eb8108c5bdec04579160ae17225d66034bd723` | BSD-3-Clause | Verify exact revision and notices |
| libadrenotools | `8fae8ce254dfc1344527e05301e43f37dea2df80` | BSD-2-Clause | Verify exact revision and notices |
| libfat16 | `d9a890b712dcdb46d3d33230997efc59f5ad8d62` | MIT | Verify exact revision and notices |
| nativefiledialog-extended | `fc168e8605bfa51aaec22ab0c4e46b9de665a437` | Zlib | Verify exact revision and notices |
| printf | `f08e577d31a8270a14e64603ff6bfdca614ff4d3` | MIT | Verify exact revision and notices |
| psvpfstools | `e9c5c7c4489a20ce2cb1a8b517caf00556594a12` | No SPDX licence detected | **Manual review required** |
| pugixml | `c8033ce9d039e7f9d134877c363397b3cfe20816` | MIT | Verify exact revision and notices |
| SDL | `fa2c02bb6e21974a89ea9824bc53c9932abe5f9c` | Zlib | Verify exact revision and notices |
| spdlog | `d6c93f38a08b4ea0f8ffcfd7f7857307d5d5c3fa` | NOASSERTION | **Manual review required** |
| SPIRV-Cross | `d8e3e2b141b8c8a167b2e3984736a6baacff316c` | Apache-2.0 | Verify exact revision and notices |
| stb | `31c1ad37456438565541f4919958214b6e762fb4` | NOASSERTION | **Manual review required** |
| substitute | `319da6b563d8da689f3b9df2fbb839edd41a1943` | NOASSERTION | **Manual review required** |
| Tracy | `f2a4f2529e7e71844c9e434b877770a21ecf7587` | NOASSERTION | **Manual review required** |
| concurrentqueue | `9afb99746f0f5fc94ac8aef737053ae0481ba8d1` | NOASSERTION | **Manual review required** |
| cubeb | `4274d032355abe24cf6da0b35fad9b8122ea1f61` | ISC | Verify exact revision and notices |
| dynarmic | `86458a0bd369d63ba4c2ef812cacbb6c9080c065` | 0BSD | Verify exact revision and notices |
| fmt | `1be298e1bd68957e4cd352e1f676f00e07dcfb57` | MIT | Verify exact revision and notices |
| LibAtrac9 | `82767fe38823c32536726ea798f392b0b49e66b9` | MIT | Verify exact revision and notices |
| vita-toolchain | `43fc1e3c686a1fc035eca583fdfeaa5e6419a61a` | MIT | Verify exact revision and notices |
| VulkanMemoryAllocator-Hpp | `3843082eaa6a6f67e6780715fcd602fc81942c9c` | CC0-1.0 | Verify exact revision and notices |
| xxHash | `e626a72bc2321cd320e953a0ccf1584cad60f363` | NOASSERTION | **Manual review required** |
| yaml-cpp | `56e3bb550c91fd7005566f19c079cb7a503223cf` | MIT | Verify exact revision and notices |

**Important:** GitHub's `NOASSERTION` or missing licence metadata does not prove that a component is unlicensed or unusable. It means the automated repository metadata is insufficient. We must inspect the licence, copyright, and notice files at the exact pinned commit before using or redistributing it.

## 4. vcpkg manifest dependencies

The upstream `vcpkg.json` also declares:

- Boost components: `boost-icl`, `boost-program-options`, and `boost-variant`
- `curl`
- `openssl`
- `zlib`

The manifest pins a vcpkg baseline: `77df67cfff9c12ccfdb52284e07c87c75092f723`.

This is not yet a complete package inventory. We still need to resolve the exact package versions, port features, transitive dependencies, platform-specific packages, and their licence/notice obligations from that baseline. Some libraries may be supplied through both a submodule and a package manager; the actual build configuration determines which copy is used.

## 5. Special review items

### FFmpeg fork

The reviewed Vita3K tree pins `Vita3K/ffmpeg-core` at `eaf918c97e76d3fa7ec5bfea63a307fced559e76`. Its `copyright` file contains the GNU LGPL version 2.1 text. The fork's CMake file downloads prebuilt FFmpeg libraries and links `avformat`, `avcodec`, `swscale`, `avutil`, `avfilter`, and `swresample` as static archives (`.a`; Windows uses `.lib`). The renderer links the FFmpeg target, so this is a runtime dependency, not merely a build-time tool.

The pinned fork's `ffmpeg.patch` modifies the vcpkg FFmpeg port to use `--disable-everything` and explicitly enable a limited list of decoders, encoders, muxers, demuxers, parsers, a file protocol, and an MJPEG bitstream filter. Its build workflow pins a separate vcpkg revision (`34823ada10080ddca99b60e85f80f55e18a44eea`) and applies that patch. This is useful evidence about the intended codec set, but the final configure logs and actual prebuilt archives still need verification. Because the current integration links static archives, the release plan must specifically address the LGPL 2.1 requirements for a relinkable application, corresponding source, notices, and the exact build scripts. Check the selected FFmpeg source files for any additional licence notices before treating the fork as cleared.

### Components without machine-readable licence metadata

At minimum, inspect the exact pinned revision and source notices for:

- Capstone
- dlmalloc
- glslang
- psvpfstools
- spdlog
- stb
- substitute
- Tracy
- concurrentqueue
- xxHash

Do not bundle any component with unresolved rights into a release binary until its licence is established.

### Build-time and test-only components

GoogleTest and other build/test utilities may not be included in the shipped application, but their source, build scripts, generated artefacts, and distribution must still be assessed according to how we use them. Separate build-only tools from runtime dependencies in the SBOM.

## 6. Required release-compliance plan

Before any public APK or Windows release containing the Vita3K core:

1. Pin the exact Vita3K commit and every submodule commit.
2. Resolve all direct and transitive dependencies, including vcpkg packages and Android/Windows-specific libraries.
3. Read each licence and notice file at the exact revision actually built.
4. Generate an SBOM (preferably SPDX or CycloneDX) from the resolved build inputs.
5. Create a third-party notices bundle and include all required licence texts and attribution.
6. Preserve the upstream GPL notices and add modification notices to changed upstream files.
7. Publish the complete corresponding source and build/install scripts required by the applicable licences, alongside the binary distribution.
8. Check that all selected licences are compatible with the overall distribution plan.
9. Obtain qualified legal review before public/commercial release.

## 7. Current gate and next engineering task

**Gate result: NOT CLEARED FOR REDISTRIBUTION YET.**

The main GPL v2 terms are identified, and the submodule graph is pinned for one exact upstream revision. However, several components have unresolved licence metadata, the exact vcpkg resolution is not yet audited, and FFmpeg build configuration needs special review.

**Next task:** inspect the licence/notice files at the exact pinned commits for all NOASSERTION/missing-metadata components, then resolve vcpkg and platform-specific dependency licences. Only after that should we create the first reproducible Vita3K build workflow.

## 8. Source references

- Vita3K repository: https://github.com/Vita3K/Vita3K
- Reviewed Vita3K commit: https://github.com/Vita3K/Vita3K/commit/c87e12578749d6267be9b0c669904fe22545b170
- GPL v2 text in Vita3K: https://github.com/Vita3K/Vita3K/blob/c87e12578749d6267be9b0c669904fe22545b170/COPYING.txt
- Pinned submodule tree: https://github.com/Vita3K/Vita3K/tree/c87e12578749d6267be9b0c669904fe22545b170
- Submodule declarations: https://github.com/Vita3K/Vita3K/blob/c87e12578749d6267be9b0c669904fe22545b170/.gitmodules
- vcpkg manifest: https://github.com/Vita3K/Vita3K/blob/c87e12578749d6267be9b0c669904fe22545b170/vcpkg.json


## 9. Exact-revision follow-up: the ten flagged components

The licence and notice files below were inspected at the submodule commits pinned by the reviewed Vita3K revision. This narrows the uncertainty, but it does not replace checking the actual files compiled into each platform build.

| Component | Finding at pinned revision | Preliminary assessment |
|---|---|---|
| Capstone | The pinned commit `022575848782a4801fd150fdbc927effcbca0864` resolves in the canonical `capstone-engine/capstone` repository as Capstone 5.0.9. Its exact-revision `LICENSE.TXT` contains the three-condition BSD licence. The same tree also contains `LICENSE_LLVM.TXT`, which carries the University of Illinois/NCSA licence for LLVM-derived portions. | **Partially identified.** Treat the main Capstone code as BSD-3-Clause, retain `LICENSE.TXT`, and map any compiled LLVM-derived files to `LICENSE_LLVM.TXT` before release. The repository README specifically instructs redistributors to attach `LICENSE.TXT`. |
| dlmalloc | `README.md` and source headers explicitly state that Doug Lea's original allocator and Gregory Popovitch's C++ conversion are released to the public domain, referencing CC0 1.0. | **Identified as public-domain/CC0 dedication.** Retain the attribution/context and verify whether any other file has separate notices. |
| glslang | `LICENSE.txt` says glslang proper uses multiple licences: 3-clause BSD, 2-clause BSD, MIT, and Apache-2.0; it separately distinguishes preprocessor licensing and optional/external components. | **Identified as multi-licence.** Must map the actual compiled source files, especially preprocessor sources, to their applicable licence sections. Do not label the whole component with one SPDX identifier without that mapping. |
| psvpfstools | The wrapper repository itself has no top-level licence file in the pinned tree. Its CMake file adds four nested submodules: libb64, libzrif, psvpfsparser, and zlib. | **Unresolved.** The wrapper has no located licence grant at this revision; audit the nested projects and establish the wrapper's own rights before redistribution. Also review OpenSSL and system/package zlib usage selected by CMake. |
| spdlog | Pinned `LICENSE` contains the MIT licence and expressly notes dependency on fmt under MIT. | **Identified as MIT**, with fmt's separate notice retained. |
| stb | Pinned `LICENSE` offers two alternatives: MIT or public domain under The Unlicense. | **Identified as dual option.** Choose and document one option consistently for the files actually used; keep the required MIT notice if selecting MIT. Check individual header notices if present. |
| substitute | Pinned `LICENSE.txt` states most files are LGPL-2.1-or-later with a special static-linking exception; `substrate.h` is based on CydiaSubstrate and under LGPLv3; `substitute.h` and generated files are public domain. | **Copyleft component requiring file-level mapping.** Determine whether Vita3K builds/uses the substrate compatibility layer and whether it is linked statically or dynamically. Preserve the applicable LGPL notices and meet corresponding source/relinking requirements. |
| Tracy | Pinned `LICENSE` states 3-clause BSD. | **Identified as BSD-3-Clause** for Tracy itself. Audit any bundled optional third-party components separately if enabled or distributed. |
| concurrentqueue | Pinned `LICENSE.md` offers Simplified BSD and Boost Software License 1.0 as alternatives. It expressly excludes certain benchmark/test components authored by others; the semaphore implementation carries a zlib licence. | **Identified as dual-licensed.** Choose/document the applicable option for the library and separately preserve the semaphore's zlib notice if used. Do not assume benchmark/test exceptions cover runtime code. |
| xxHash | Pinned `LICENSE` states BSD 2-Clause. | **Identified as BSD-2-Clause** for the library; inspect optional CLI/test code only if included in a distribution. |

### psvpfstools nested dependency pins

The reviewed psvpfstools commit pins these nested repositories:

| Nested component | Exact commit | Next action |
|---|---|---|
| libb64 | `3896b7a74c70baed0e2f6039a1dbd723e5d5cc8f` | Inspect licence and notices |
| libzrif | `7d1e69bee7d2f08ea5754eff4463c041aacd49af` | Inspect licence and notices |
| psvpfsparser | `05d43a06a6189302d31091c65e4fc8707476eef3` | Exact tree contains no root `LICENSE`, `COPYING`, or `NOTICE` file. CMake builds its C++ source files into the `psvpfsparser` library. **Rights remain unresolved; do not infer a licence from absence of a file.** |
| zlib | `cb210089eb06453199578993566012493f6f7d21` | Inspect licence and notices |

### Updated result for the ten

- **Licence text identified:** Capstone's main code (BSD-3-Clause, with a separate LLVM-derived licence file to map), dlmalloc, glslang (multiple licence regimes), spdlog, stb, substitute (file-specific LGPL/public-domain terms), Tracy, concurrentqueue, and xxHash.
- **Still unresolved:** psvpfstools' own wrapper repository and the exact licence terms for its nested `libb64`, `libzrif`, `psvpfsparser`, and zlib submodules.
- **Additional file/build mapping required:** Capstone LLVM-derived files; glslang file-level licence mapping; substitute file/linkage mapping; optional third-party content bundled by Tracy/concurrentqueue.

The four nested repository endpoints currently redirect to renamed GitHub repository IDs that the connected GitHub reader cannot inspect. The exact commit IDs are preserved above; no licence has been guessed from repository names or current default branches. `psvpfsparser`'s pinned tree was readable and contains no root licence/notice file, while its CMake configuration compiles its C++ sources into a library linked with `libzRIF`, `libb64`, zlib, and OpenSSL Crypto. This is a concrete unresolved rights issue, not proof that the code is unlicensed.

This stage is now partially resolved: Capstone's principal licence is identified, but the dependency audit is **not complete** and the release gate remains closed. Next, obtain the exact nested repositories' source/licence records through a full recursive clone or another verifiable source, then map actual compiled files and platform build choices.


### Additional exact-revision source records

- Capstone 5.0.9 pinned commit: https://github.com/capstone-engine/capstone/commit/022575848782a4801fd150fdbc927effcbca0864
- Capstone BSD licence: https://raw.githubusercontent.com/capstone-engine/capstone/022575848782a4801fd150fdbc927effcbca0864/LICENSE.TXT
- Capstone LLVM-derived licence: https://raw.githubusercontent.com/capstone-engine/capstone/022575848782a4801fd150fdbc927effcbca0864/LICENSE_LLVM.TXT
- psvpfsparser pinned tree: https://github.com/Vita3K/psvpfsparser/tree/05d43a06a6189302d31091c65e4fc8707476eef3
- psvpfsparser CMake source list and link configuration: https://github.com/Vita3K/psvpfsparser/blob/05d43a06a6189302d31091c65e4fc8707476eef3/cmake/CMakeLists.txt
- psvpfstools pinned CMake and submodule declarations: https://github.com/Vita3K/psvpfstools/tree/e9c5c7c4489a20ce2cb1a8b517caf00556594a12


## 10. First-pass platform build graph and runtime classification

This section records what the pinned Vita3K CMake files actually select. It is a source/build-graph review, not proof that every target is present in every final binary. Final inclusion must be confirmed from platform build logs, link maps, and packaged artefacts.

### Runtime-linked components visible in the CMake graph

| Component | Evidence in pinned build files | Platform/usage note |
|---|---|---|
| Capstone | `vita3k/cpu/CMakeLists.txt` links `capstone` into the CPU library | CPU runtime dependency; main BSD licence identified, LLVM-derived files still need mapping |
| Dynarmic | CPU library links `dynarmic` and `merry::mcl` | CPU runtime dependency |
| FFmpeg | Renderer links `ffmpeg`; FFmpeg target links six static library archives | Runtime dependency; LGPL 2.1 static-link compliance needs specific review |
| psvpfstools / psvpfsparser | Main `vita3k` target links `psvpfsparser`; package library also links it | Runtime dependency; wrapper and nested dependency rights unresolved |
| SDL3 | Renderer, audio and frontend link SDL3; bundled SDL is default unless `VITA3K_USE_SYSTEM_SDL` is enabled | Runtime dependency; submodule licence and notices must match the selected system/bundled build |
| cubeb | Audio library links cubeb | Runtime audio dependency; CMake disables tests, Rust libraries and tools and bundles Speex |
| pugixml | Main Android target and app link pugixml | Runtime dependency |
| xxHash | Renderer links xxHash | Runtime dependency |
| concurrentqueue | Renderer links concurrentqueue | Runtime dependency |
| stb | Renderer links stb | Runtime dependency; identify exact headers used and selected licence option |
| substitute | Added as an external CMake subdirectory | Confirm which targets/files are actually linked; LGPL/static exception mapping remains necessary |
| OpenSSL | psvpfstools is configured after OpenSSL; crypto/SSL interface targets are created | System OpenSSL is preferred when found; platform-specific fallback builds/downloads exist |
| curl | System curl is preferred; otherwise CMake FetchContent pins curl commit `68720b4837284335b2d63cb358f8f6ce65f5bc55` | Runtime/feature dependency needs exact system-vs-fetched resolution per build |
| Boost | Header-only components; system Boost 1.82+ preferred unless options force bundled Boost | Header dependency; system/bundled source choice changes SBOM attribution |
| fmt / spdlog | fmt and spdlog are added as external targets; spdlog is configured to use external fmt | Runtime logging dependency; MIT notices required |
| libadrenotools | Added only for Android when detected architecture is `arm64` | Android arm64-specific dependency |
| Qt 6 | Qt frontend is configured and linked only when `NOT ANDROID` | Desktop UI dependency; not used by Android frontend |

### Conditional, development, or platform-only components

- **Tracy:** built only when the configuration is not Release. Its core-component linkage is controlled by `TRACY_ENABLE_ON_CORE_COMPONENTS`; the option is enabled by default in non-Release configurations. Keep it out of production Release builds unless intentionally enabled and separately documented.
- **GoogleTest:** a static test library target is declared. Confirm whether any release target links or packages it; it should normally remain test/build-only.
- **Native File Dialog Extended:** added only when `NOT ANDROID`.
- **Discord Game SDK:** enabled only on supported desktop targets when rich presence is enabled. It is downloaded as a separate archive and is not a Vita3K Git submodule; its own SDK licence and redistribution terms must be reviewed before shipping it.
- **Vulkan validation layers:** downloaded for non-Release Android configurations when the expected prebuilt layer is absent. Treat as development/debug artefacts unless a release package demonstrably includes them.
- **glslang / SPIRV-Cross:** both are added to the build. The inspected CMake disables several optional binaries, CLI targets, tests, and language backends by default; actual linked library targets still need to be mapped to source files and licence sections.
- **System-vs-bundled choices:** Boost, SDL, OpenSSL, and curl can resolve differently according to host packages and CMake options. A single generic SBOM will not be sufficient for Android and Windows; produce a resolved SBOM per target configuration.

### Android-specific observations

- The Android root CMake setup activates the vcpkg Android toolchain helper before project configuration.
- The helper maps Android ABIs to vcpkg triplets, including `arm64-v8a` to `arm64-android` and `x86_64` to `x64-android`.
- The Android build instructions call for both arm64 and x64 vcpkg triplets. The user's preferred Helio G100 target is an ARM64 device, so the arm64-v8a configuration is the relevant first device build; performance and compatibility still require real-device testing.
- Android uses the JNI shared library target and does not build the Qt desktop frontend.
- Android Release configuration excludes symbols from several static libraries, including OpenSSL and FFmpeg archives. This is a symbol-visibility/linker detail, not evidence that those libraries are absent or dynamically linked.

### Reproducibility and audit consequences

1. The dependency graph differs by platform and build type. We need separate Android arm64 Release and Windows Release inventories before generating a release SBOM.
2. We need to capture whether each system-or-bundled fallback was selected, plus exact package versions and checksums for downloaded archives.
3. FFmpeg's static archives and LGPL 2.1 compliance are a release blocker until the corresponding source, notices, build scripts, and relinking path are prepared.
4. psvpfstools remains a release blocker until its own code and all four nested submodules have established licence terms.
5. The Discord SDK must not be silently included in an SBOM as though it were part of the pinned Vita3K Git tree.
6. No Vita3K engine source has been integrated into AKOREDE VITA by this audit; the current app scaffold remains separate and reports that its emulator core is not connected.


## 11. Android vcpkg baseline: direct package inventory

The root manifest pins vcpkg baseline `77df67cfff9c12ccfdb52284e07c87c75092f723`. At that exact baseline, the six direct package manifests resolve as follows:

| Direct package | Manifest version | Licence expression | Direct dependency observations |
|---|---:|---|---|
| boost-icl | 1.90.0 (port 1) | BSL-1.0 | Depends on numerous Boost component ports, including assert, config, container, core, date-time, iterator, MPL, range, rational, type-traits, utility and headers |
| boost-program-options | 1.90.0 (port 1) | BSL-1.0 | Depends on Boost any, bind, config, core, function, iterator, lexical-cast, smart-ptr, tokenizer, type-traits and related components |
| boost-variant | 1.90.0 (port 1) | BSL-1.0 | Depends on Boost assert, config, container-hash, core, integer, MPL, preprocessor, type-index, type-traits and related components |
| curl | 8.19.0 | `curl AND ISC AND BSD-3-Clause` | Depends on zlib; default features include `non-http` and `ssl`. On non-Windows targets the default SSL feature selects OpenSSL |
| openssl | 3.6.1 (port 3) | Apache-2.0 | Its manifest uses MIT-licensed vcpkg CMake helper ports as host/build dependencies |
| zlib | 1.3.1 | Zlib | Uses the MIT-licensed vcpkg CMake helper port as a host/build dependency |

The Boost component manifests and the inspected Boost transitive manifests identify Boost Software License 1.0. This is not yet a complete transitive inventory: every resolved Boost port, host tool, and platform-conditioned dependency must be collected from the vcpkg install plan or installed package metadata before SBOM generation.

### Important platform distinction

The root CMake file activates the vcpkg Android helper only when `CMAKE_SYSTEM_NAME` is Android. The six-package vcpkg manifest is therefore directly relevant to the Android build path. Do not automatically apply this exact package resolution to Windows. The desktop path can select system libraries or source fallbacks instead.

The CMake logic prefers system curl when available and otherwise fetches curl at commit `68720b4837284335b2d63cb358f8f6ce65f5bc55` (identified in the source comment as release 8.21.0). This differs from the Android vcpkg port version 8.19.0 and must be recorded as a separate dependency route. Similarly, OpenSSL can resolve from the system or from platform-specific fallback downloads/builds. Capture the actual route for each target build rather than merging them into one assumed dependency version.

### Build-documentation mismatch

The pinned root `CMakeLists.txt` explicitly sets `CMAKE_CXX_STANDARD 23`, while the pinned `building.md` introduction describes the requirement as a C++20-compatible compiler. For reproducible builds, use the actual CMake configuration as authoritative for this revision and record C++23 as the required language standard. The upstream documentation should be clarified before treating its build instructions as fully reproducible.

### Current vcpkg result

The direct Android package versions and their manifest licence expressions are now recorded. The complete transitive closure, actual package installation plan, selected curl/OpenSSL paths, and exact package copyright/notice payloads remain to be captured. This is still a preliminary dependency inventory, not a release SBOM.
