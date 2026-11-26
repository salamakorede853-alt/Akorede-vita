# Upstream Technical Audit — Vita3K

**Audit date:** 2026-11-26  
**Status:** Initial repository and build-configuration review; no source code copied or built.

## Executive finding

Vita3K is a technically credible candidate foundation for AKOREDE VITA because its upstream project already targets Windows and Android and is predominantly C++. This makes a reviewed downstream adaptation substantially more realistic than implementing the entire PlayStation Vita hardware/software environment from scratch.

This is a preliminary engineering review, not a complete security, dependency, compatibility, or legal audit.

## Verified upstream facts

- Upstream repository: https://github.com/Vita3K/Vita3K
- Upstream project describes itself as an experimental PlayStation Vita emulator.
- Upstream README identifies Windows, Linux, macOS, and Android as supported targets.
- Upstream declares GPL-2.0 licensing and includes the full GPL version 2 text in `COPYING.txt`.
- Root CMake configuration sets the language standard to **C++23**.
- The build guide documents CMake-based builds and recursive Git submodules.
- Windows instructions currently describe Visual Studio 2022, the Desktop development with C++ workload, Git, and Qt 6.11 or later.
- Android uses Android Studio/SDK/NDK, vcpkg dependencies, Gradle, and CMake.
- The Android Gradle configuration currently declares minSdk 28 and ABI filters `arm64-v8a` and `x86_64`.
- The Android Gradle file currently specifies NDK 30.0.16248370 and compile SDK 37.2.
- The Android native build links the Vita3K core as a shared library and uses Android-specific JNI/platform source files.
- The desktop build includes the Qt frontend; Android excludes that Qt frontend and has its own Android integration.

Sources reviewed:
- https://github.com/Vita3K/Vita3K
- https://github.com/Vita3K/Vita3K/blob/master/COPYING.txt
- https://github.com/Vita3K/Vita3K/blob/master/building.md
- https://github.com/Vita3K/Vita3K/blob/master/CMakeLists.txt
- https://github.com/Vita3K/Vita3K/blob/master/vita3k/CMakeLists.txt
- https://github.com/Vita3K/Vita3K/blob/master/android/app/build.gradle
- https://github.com/Vita3K/Vita3K/blob/master/.ci/build-android.sh

## Architecture observations

The upstream codebase separates many emulator subsystems into distinct CMake targets, including CPU, kernel, memory, renderer, audio, input, packages, and platform frontends.

The Android application uses a native C++ shared library with JNI integration and a Kotlin/Jetpack Compose Android application layer. Desktop uses a separate Qt frontend. This confirms that the project already has platform-specific presentation/integration around shared emulator subsystems.

## Licence and redistribution gate

Vita3K states that it is licensed under **GNU GPL version 2**. Before incorporating or distributing upstream code, AKOREDE VITA must complete a dependency-by-dependency licence review and define a compliant distribution model.

At minimum, the project must plan for:
- retaining copyright, licence, and warranty-disclaimer notices;
- clearly marking modified upstream files and the dates of changes;
- supplying or providing compliant access to the complete corresponding source when distributing covered binaries;
- licensing covered derivative work under GPL-2.0-compatible terms;
- reviewing third-party dependencies and their separate notices and obligations.

Do not assume that renaming the application or placing a new interface around the emulator removes GPL obligations. Whether separately distributed components form a combined or derivative work can depend on the technical design and applicable law. Obtain qualified legal review before public distribution or commercial plans.

## Recommended integration direction

**Preferred starting point: a transparent, GPL-compliant downstream fork with an original AKOREDE VITA product identity and carefully separated platform/UI work.**

Keep the emulator core and platform-specific frontends clearly separated. Maintain upstream attribution and a documented change history. Do not copy source until the repository's licence, submodules, and third-party dependency licences have been reviewed.

A standalone launcher or companion UI may be evaluated as an alternative, but its legal separation must not be assumed; review the actual process/API boundary and distribution arrangement first.

## Build feasibility

### Windows
A reproducible Windows build requires a Windows-capable build runner or PC, Git with submodule support, Visual Studio 2022 C++ tools, CMake, and the Qt version stated by the current upstream build guide. The guide's example uses the `windows-vs2022` CMake preset.

### Android
A reproducible Android build requires Android Studio or the Android SDK/NDK toolchain, vcpkg, the repository's Gradle wrapper, and native CMake build support. The current upstream configuration targets Android API 28 minimum and includes arm64-v8a and x86_64 ABIs.

These requirements are not satisfied by this chat alone. We can prepare source changes, workflows, and build configuration here, but actual compilation and device testing must run on a suitable build runner or computer.

## Risks and unknowns still requiring work

1. Full third-party dependency and submodule licence inventory.
2. Current upstream build workflow and CI matrix review.
3. Android device/GPU compatibility and performance baseline.
4. Windows runtime packaging and dependency validation.
5. Emulator compatibility and regression test strategy.
6. Save-data, user-data, and configuration migration strategy.
7. Security review of package installation, file access, and update mechanisms.
8. Branding and trademark review; the project must remain clearly unofficial.

## Decision

**Proceed with Vita3K as the candidate technical base, conditionally.** The next gate is a dependency/licence inventory and a minimal reproducible build in CI. Do not yet merge upstream emulator source into the AKOREDE VITA repository or claim a working emulator build.
