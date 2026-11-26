# AKOREDE VITA — Development Roadmap

**Current stage:** Milestone 01 — Foundation and audit

## Milestone 01 — Foundation and audit

- [x] Create the GitHub repository
- [x] Add project overview
- [x] Add proposed architecture
- [x] Add roadmap and contribution guidance
- [ ] Inspect upstream repository structure
- [ ] Verify upstream licence and redistribution obligations
- [ ] Select the integration strategy
- [ ] Identify supported compiler, SDK, NDK, and CMake versions
- [ ] Establish a reproducible Windows build
- [ ] Establish a reproducible Android build
- [ ] Record baseline test results

**Completion criteria:** A documented, licence-reviewed source baseline with reproducible build instructions for at least one target and a clear plan for the second target.

## Milestone 02 — Product design

- [ ] Define visual identity and accessibility rules
- [ ] Design library, game details, settings, and controller screens
- [ ] Define shared navigation and platform-specific interaction patterns
- [ ] Review designs on phone-sized and desktop-sized screens

## Milestone 03 — Product integration

- [ ] Add the branded application shell
- [ ] Connect library discovery to supported emulator interfaces
- [ ] Add configuration and input-management UX
- [ ] Add diagnostics and compatibility presentation
- [ ] Preserve existing emulator functionality

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
