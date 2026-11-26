# AKOREDE VITA

**An independently branded, cross-platform PlayStation Vita emulation project.**

Targets: **Windows** and **Android**  
Primary implementation language: **C++**  
Project stage: **Native application scaffold implemented; emulator core not integrated**

> AKOREDE VITA is an unofficial community software project and is not affiliated with, endorsed by, or sponsored by Sony Interactive Entertainment.

## Project direction

The project is investigating a product experience and platform integration around a reviewed open-source emulation foundation. The candidate technical base is [Vita3K](https://github.com/Vita3K/Vita3K).

No Vita3K source code has been copied into this repository. Any future reuse or modification must comply with upstream licensing, notices, and source-distribution requirements. The dependency and licence review is not yet complete.

## Current application work

- [Browser interface prototype](app-prototype/) — responsive product UI demonstration.
- [Native application scaffold](native/) — Windows Qt entry point, Android Kotlin/Jetpack Compose application, and shared C++ status bridge.

The native apps currently display **Emulator core not connected**. The shared C++ bridge intentionally reports that the engine is not ready. These are application foundations, not playable emulators. The shared C++ bridge, Windows Qt shell, and Android debug APK have all passed the current GitHub Actions build pipeline. These checks validate the scaffolds only; physical-device testing and emulator-core integration remain outstanding.

## Planned capabilities

- Windows and Android application targets
- Game library and per-title settings
- Controller and touchscreen input configuration
- Graphics, audio, and performance settings
- Save-data and user-data management
- Diagnostic logs and compatibility reporting

These are roadmap goals, not currently completed features.

## Repository guide

- [Architecture](docs/ARCHITECTURE.md) — system boundaries and platform choices
- [Roadmap](docs/ROADMAP.md) — milestones and completion criteria
- [Upstream audit](docs/UPSTREAM_AUDIT.md) — initial Vita3K architecture and build review\n- [Licence audit](docs/LICENSE_AUDIT.md) — pinned Vita3K revision, preliminary dependency inventory, and outstanding compliance checks
- [Build pipeline](docs/BUILD_PIPELINE.md) — CI jobs and build status
- [Browser prototype](app-prototype/README.md) — UI-only prototype scope
- [Native scaffold](native/README.md) — platform app build instructions
- [Contributing](CONTRIBUTING.md) — contribution workflow

## Development status

**Milestone 01 — Foundation and audit**
- [x] Create project repository and initial documentation
- [x] Complete preliminary Vita3K architecture and licence review
- [ ] Complete dependency and submodule licence inventory
- [ ] Establish reproducible upstream emulator builds

**Milestone 02 — Product design and interface**
- [x] Build responsive browser UI prototype
- [x] Add initial native Windows and Android application shells
- [x] Define a small shared C++ status API for both platform shells
- [ ] Review native screens on physical phone and desktop
- [ ] Finalise detailed product design specifications

**Milestone 03 — Build and integration**
- [x] Add CI compilation of the shared C++ bridge
- [ ] Confirm Android debug APK build in CI
- [ ] Compile and package the Windows Qt application
- [ ] Complete upstream dependency/licence gate
- [ ] Establish a pinned, reproducible Vita3K baseline
- [ ] Integrate the emulator core and replace placeholder status API

## Legal and safety notes

Use only software, firmware, and game data that you are legally entitled to use. Do not distribute copyrighted game files, proprietary firmware, encryption keys, or other materials without authorization. This project does not provide copyrighted game content.

## Learning approach

Development is intended to be educational and incremental. Explanations, small changes, code review, and tests should accompany implementation so contributors can understand the C++ and platform engineering involved.
