# Native application foundation

This directory starts the platform-specific application shells and the shared C++ boundary.

## Layout

- `windows/`: Qt 6 Widgets desktop entry point.
- `android/`: Kotlin/Jetpack Compose Android application with an NDK/CMake JNI bridge.
- `shared/`: small C++ API shared by both application shells.

## Current behavior

Both apps report **Emulator core not connected**. The shared library intentionally returns a not-ready status. It does not implement Vita CPU, GPU, kernel, audio, storage, or game execution.

## Build prerequisites

### Windows
- Visual Studio 2022 with Desktop development with C++
- CMake 3.22+
- Qt 6 with the Widgets module

Configure from this directory or a separate build folder:

```powershell
cmake -S native/windows -B build/windows -DCMAKE_PREFIX_PATH="<Qt 6 install prefix>"
cmake --build build/windows --config Release
```

### Android
- JDK 17
- Android SDK platform 35
- Android NDK installed through Android Studio
- CMake 3.22.1
- Gradle 8.11.1 or a compatible wrapper

The Android project is under `native/android`. A Gradle wrapper has not yet been generated, so use an installed compatible Gradle distribution for now.

## Important

This is an initial scaffold and has not yet been compiled on Windows or Android. The Android app currently displays a status returned by the shared C++ library. The next gate is to run actual platform builds and fix any toolchain issues before connecting emulator code.
