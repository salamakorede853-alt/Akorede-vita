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

Vita3K's FFmpeg submodule points to a Vita3K-maintained fork, and repository metadata reports LGPL-2.1. We must inspect the exact fork revision, local patches, enabled/disabled codecs and libraries, and final link configuration. FFmpeg licensing can depend on build options and included components; do not treat the repository-level label alone as final clearance.

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
