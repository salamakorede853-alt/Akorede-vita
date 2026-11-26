# Build Pipeline Plan

## Current repository reality

The repository now contains:
- a browser-only interface prototype;
- a Windows Qt application shell;
- an Android Kotlin/Jetpack Compose application shell;
- a small shared C++ status library;
- no Vita3K source and no emulator implementation.

The native application shells report that the emulator core is not connected. An Android debug APK is a shell build, not an emulator release.

## CI jobs

The workflow at `.github/workflows/ci.yml` currently includes:

1. **Repository validation** — checks core project files and prototype JavaScript syntax.
2. **Shared C++ build** — configures and compiles `native/shared` with CMake on Ubuntu.
3. **Android debug build** — installs Java, Android SDK/NDK/CMake and Gradle, then assembles a debug APK and uploads it as an artifact.
4. **Windows toolchain readiness** — checks for Visual Studio and CMake. Qt desktop compilation is not yet configured in CI.

## Local development

### Shared C++ bridge

```sh
cmake -S native/shared -B build/shared -DCMAKE_BUILD_TYPE=Release
cmake --build build/shared --config Release
```

### Windows Qt shell

Requirements: Visual Studio 2022 C++ workload, CMake 3.22+, and Qt 6 Widgets.

```powershell
cmake -S native/windows -B build/windows -DCMAKE_PREFIX_PATH="<Qt 6 install prefix>"
cmake --build build/windows --config Release
```

### Android shell

Requirements: JDK 17, Gradle 8.11.1, Android SDK platform 35, Android NDK, and CMake 3.22.1.

The Android project is under `native/android`. A Gradle wrapper has not yet been generated.

```sh
cd native/android
gradle --no-daemon :app:assembleDebug
```

The CI workflow uses the same declared toolchain versions to create a debug APK. A successful APK build proves the app shell compiles; it does not prove Vita game compatibility or core integration.

## Next build tasks

- Confirm Android CI build passes and inspect the generated APK artifact.
- Generate and commit the Gradle wrapper.
- Add Qt installation and a real Windows desktop build job.
- Add Android lint/unit tests and Windows smoke tests where practical.
- Complete the dependency and licence inventory before bringing in upstream source.

## Release and security rules

- Pin third-party GitHub Actions to reviewed immutable commit SHAs before production release.
- Use least-privilege workflow permissions.
- Never place signing keys, passwords, firmware, game data, or private tokens in the repository.
- Generate an SBOM and complete dependency licence review before distributing binaries.
- Preserve all upstream notices and satisfy GPL-2.0 source-distribution requirements for any covered binaries.
