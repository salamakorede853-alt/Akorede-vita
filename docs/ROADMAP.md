# AKOREDE VITA — Development Roadmap

**Current stage:** Native application scaffold and first build validation

## Milestone 01 — Foundation and audit

- [x] Create the GitHub repository and initial documentation
- [x] Complete preliminary Vita3K architecture and licence review
- [ ] Complete third-party dependency and submodule licence inventory
- [ ] Select and pin a Vita3K baseline commit
- [ ] Establish reproducible upstream emulator builds

## Milestone 02 — Product design and interface

- [x] Build the responsive browser UI prototype in `app-prototype/`
- [x] Create Windows Qt application entry point
- [x] Create Android Kotlin/Jetpack Compose application entry point
- [x] Add shared C++ engine-status API used by both app shells
- [ ] Review native screens on phone-sized and desktop-sized displays
- [ ] Finalise accessibility, navigation, and platform interaction specifications

**Current boundary:** The browser and native apps are shells only. They do not execute Vita software, load game files, or implement Vita hardware/system APIs.

## Milestone 03 — Build and integration

- [x] Add a CMake build for the shared C++ status bridge
- [x] Add CI job to compile the shared C++ library
- [x] Add Android Gradle/NDK project and CI debug-APK build job
- [ ] Confirm Android debug APK build passes on CI
- [ ] Add Windows Qt dependencies to CI and compile the desktop shell
- [ ] Generate Gradle wrapper and document pinned SDK/NDK versions
- [ ] Complete upstream dependency/licence review
- [ ] Select and pin a reviewed Vita3K revision
- [ ] Establish a reproducible baseline emulator build
- [ ] Define and implement the compliant emulator-core integration boundary

## Milestone 04 — Windows quality

- [ ] Build and package a Windows development version
- [ ] Test window resizing, controller input, graphics, and audio
- [ ] Add automated regression checks

## Milestone 05 — Android quality

- [ ] Build and package an Android development version
- [ ] Test touch and external controller input
- [ ] Test app lifecycle, graphics surfaces, storage permissions, and performance
- [ ] Test on representative Android devices

## Milestone 06 — Release readiness

- [ ] Complete licence, attribution, and SBOM review
- [ ] Publish corresponding source for covered copyleft components
- [ ] Create reproducible release builds
- [ ] Publish known-issues and compatibility documentation

## Working rules

- Never mark a task complete without evidence.
- Keep upstream changes traceable and preserve required notices.
- Make small, reviewable commits.
- Do not commit proprietary firmware, encryption keys, copyrighted game files, or secrets.
- Do not describe a shell or CI toolchain check as a working emulator.
