# AKOREDE VITA

**An independently branded, cross-platform PlayStation Vita emulation project.**

Targets: **Windows** and **Android**  
Primary implementation language: **C++**  
Project stage: **Foundation complete; UI prototype started**

> AKOREDE VITA is an unofficial community software project and is not affiliated with, endorsed by, or sponsored by Sony Interactive Entertainment.

## Project direction

The project will investigate a hybrid development approach: build an original product experience and platform integration around a carefully reviewed, compatible open-source emulation foundation. The initial candidate for study is [Vita3K](https://github.com/Vita3K/Vita3K).

No upstream source code has been copied into this repository yet. Any future reuse or modification must comply with the upstream project's licence, notices, and source-distribution requirements.

## Product interface prototype

The first responsive, interactive interface prototype is in [app-prototype](app-prototype/). It includes a demo library, search, title details, controller settings, and application settings.

**Important:** this is a UI-only prototype. It does not emulate games, scan game folders, or connect to an emulator core. Its catalogue entries are fictional placeholders.

## Planned capabilities

- Windows and Android application targets
- Game library and per-title settings
- Controller and touchscreen input configuration
- Graphics, audio, and performance settings
- Save-data and user-data management
- Diagnostic logs and compatibility reporting

These are roadmap goals, not features currently implemented in a native application.

## Repository guide

- [Architecture](docs/ARCHITECTURE.md) — proposed system boundaries and technical decisions
- [Roadmap](docs/ROADMAP.md) — milestones and completion criteria
- [Upstream audit](docs/UPSTREAM_AUDIT.md) — initial Vita3K architecture, build, and licence review
- [Build pipeline](docs/BUILD_PIPELINE.md) — CI readiness checks and the path to real builds
- [Interface prototype](app-prototype/README.md) — prototype scope and next integration steps
- [Contributing](CONTRIBUTING.md) — contribution workflow

## Development status

**Milestone 01 — Foundation and audit**

- [x] Create project repository
- [x] Document initial architecture and roadmap
- [x] Complete initial Vita3K architecture and licence review
- [x] Select a conditional GPL-compliant downstream-fork direction
- [x] Document upstream Windows and Android build requirements
- [ ] Complete third-party dependency and submodule licence inventory
- [x] Add initial Windows and Android CI toolchain-readiness checks
- [ ] Establish reproducible Windows and Android emulator builds
- [ ] Record baseline tests and compatibility status

**Milestone 02 — Product design and interface prototype**

- [x] Build the first responsive, interactive UI prototype
- [ ] Review the prototype on phone-sized and desktop-sized screens
- [ ] Finalise visual identity, accessibility, and platform-specific interaction rules
- [ ] Complete editable design specifications for the native application screens

## Legal and safety notes

Use only software, firmware, and game data that you are legally entitled to use. Do not distribute copyrighted game files, proprietary firmware, encryption keys, or other materials without authorization. This project does not provide copyrighted game content.

## Learning approach

Development is intended to be educational and incremental. Explanations, small changes, code review, and tests should accompany implementation so contributors can understand the C++ and platform engineering involved.
