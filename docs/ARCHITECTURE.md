# AKOREDE VITA — Architecture

**Status:** Initial native application scaffold committed; emulator core not integrated  
**Targets:** Windows and Android  
**Shared native language:** C++17 for the initial application bridge

## 1. Guiding principles

1. Keep emulator execution independent from the product interface.
2. Prefer a proven, compatible open-source emulation foundation over rewriting the console stack.
3. Keep platform-specific code behind narrow interfaces.
4. Make builds reproducible and document every dependency.
5. Preserve upstream copyright notices and comply with all applicable licences.
6. Do not bundle proprietary firmware, keys, or copyrighted game content.

## 2. Candidate emulator foundation

The initial candidate is Vita3K. Its reviewed architecture already uses a Qt desktop frontend and a Kotlin/Jetpack Compose Android application with native C++ integration. AKOREDE VITA's scaffold follows those platform conventions rather than forcing one UI toolkit onto both platforms.

No Vita3K source has been copied or modified in this repository. A pinned upstream revision, dependency inventory, and licence clearance are required before integration.

## 3. Current repository structure

```text
app-prototype/              Browser-based product UI prototype
native/
  shared/                   Shared C++ engine-status boundary
  windows/                  Qt 6 Widgets desktop shell
  android/                  Kotlin/Compose app and JNI/NDK bridge
docs/                       Architecture, audit, roadmap, build plan
.github/workflows/          Repository checks and platform build jobs
```

The shared bridge currently exposes only:
- `av_engine_is_ready()`
- `av_engine_status_message()`

It intentionally reports that the emulator core is not connected. It is a placeholder contract, not an emulator API.

## 4. Platform application layers

### Windows
- Qt 6 Widgets for the desktop application shell.
- CMake for project configuration.
- Shared C++ status library linked as a native target.
- Future platform adapter responsibilities: window/surface handling, graphics context, controller input, filesystem, packaging.

### Android
- Kotlin and Jetpack Compose for the application UI.
- Android Gradle Plugin and Gradle for application builds.
- Android NDK and CMake for native code.
- JNI bridge connects the Kotlin activity to the shared C++ status API.
- Future platform adapter responsibilities: lifecycle, native rendering surface, touch and controller input, storage access, packaging.

### Shared native layer
Keep cross-platform C++ interfaces narrow and independent of UI frameworks. The real emulator integration must follow the selected upstream project's own subsystem and frontend contracts rather than inventing a parallel emulator architecture.

## 5. Future emulator integration boundary

Potential shared responsibilities include:
- emulator lifecycle and configuration
- game/library metadata services
- logging and diagnostics
- controller/input abstraction
- per-title configuration and save-data services

CPU execution, memory, GPU/rendering, audio, kernel services, and guest OS compatibility must be supplied by the reviewed emulator core. The current repository does not implement these systems.

## 6. Build strategy

- Compile the shared C++ bridge independently in CI.
- Build the Android application with pinned Java, Gradle, Android SDK/NDK, and CMake versions.
- Build the Windows Qt shell with the matching Qt and Visual Studio toolchain.
- Establish a known-good upstream emulator build before integration.
- Keep Windows and Android build configurations explicit.
- Record build failures and limitations instead of claiming untested support.

## 7. Security, privacy, and legal boundaries

- Never commit credentials, signing keys, personal tokens, or private user data.
- Do not include copyrighted game images, game dumps, proprietary firmware, or encryption keys.
- Users are responsible for ensuring they have rights to any content they use.
- Include required licence texts, attribution, and corresponding source availability for redistributed copyleft components.
- Do not imply Sony endorsement or use Sony branding in a way that suggests an official product.

## 8. Outstanding architecture gates

1. Complete dependency and submodule licence inventory.
2. Select and pin a specific Vita3K source revision.
3. Establish reproducible upstream Windows and Android baseline builds.
4. Design the smallest stable app-to-core API after reviewing upstream frontend interfaces.
5. Test rendering-surface and lifecycle ownership on both platforms.
