# AKOREDE VITA — Development Roadmap

**Current stage:** Milestone 02 — Product design and interface prototype

## Milestone 01 — Foundation and audit

- [x] Create the GitHub repository
- [x] Add project overview, architecture, roadmap, and contribution guidance
- [x] Complete initial Vita3K architecture and licence review
- [x] Select a conditional GPL-compliant downstream-fork direction
- [x] Document upstream Windows and Android build requirements
- [ ] Complete third-party dependency and submodule licence inventory
- [x] Add initial Windows and Android CI toolchain-readiness checks
- [ ] Establish reproducible Windows and Android emulator builds
- [ ] Record baseline tests and compatibility status

**Completion criteria:** A documented, licence-reviewed source baseline with reproducible build instructions for at least one target and a clear plan for the second target.

## Milestone 02 — Product design and interface prototype

- [x] Build the first responsive, interactive UI prototype in `app-prototype/`
- [ ] Review the prototype on phone-sized and desktop-sized screens
- [ ] Define visual identity, accessibility, and interaction rules
- [ ] Complete editable design specifications for library, game details, settings, and controller screens
- [ ] Define shared navigation and platform-specific interaction patterns

**Prototype boundary:** The current browser prototype is a UI demonstration only. It does not emulate games, access local game folders, configure physical controllers, or communicate with Vita3K.

## Milestone 03 — Product integration

- [ ] Complete the upstream dependency and licence gate before source integration
- [ ] Establish a reproducible upstream baseline build
- [ ] Choose and document native UI integration boundaries for Windows and Android
- [ ] Add the branded application shell without removing existing emulator functionality
- [ ] Connect library discovery to supported emulator interfaces
- [ ] Add configuration and input-management UX
- [ ] Add diagnostics and compatibility presentation

## Milestone 04 — Windows quality

- [ ] Build and package a Windows development version
- [ ] Test controller input and window resizing
- [ ] Test graphics and audio configuration
- [ ] Add automated regression checks

## Milestone 05 — Android quality

- [ ] Build and package an Android development version
- [ ] Test touch and external controller input
- [ ] Test app lifecycle and graphics surfaces
- [ ] Test storage and permissions
- [ ] Profile performance on representative devices

## Milestone 06 — Release readiness

- [ ] Complete licence and attribution review
- [ ] Publish corresponding source for covered copyleft components
- [ ] Create reproducible release builds
- [ ] Publish known-issues and compatibility documentation
- [ ] Prepare release notes and support guidance

## Working rules

- Never mark a task complete without evidence.
- Keep upstream changes traceable.
- Make small, reviewable commits.
- Do not commit proprietary firmware, encryption keys, copyrighted game files, or secrets.
- Prefer upstream contributions for generally useful emulator fixes.
