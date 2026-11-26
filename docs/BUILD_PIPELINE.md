# Build Pipeline Plan

## Current repository reality

The AKOREDE VITA repository currently contains project documentation only. It does not yet contain the Vita3K emulator source, a root CMake project, an Android Gradle project, or native application source files. Therefore, an honest CI setup must not claim to compile an emulator or produce installable packages.

## Initial automation added

The GitHub Actions workflow at `.github/workflows/ci.yml` currently performs:

1. **Repository validation** — checks required project documentation and local README links.
2. **Windows toolchain readiness** — verifies Git, CMake, and a Visual Studio installation on a Windows runner.
3. **Android toolchain readiness** — verifies Java and Android SDK availability on an Ubuntu runner.

These are infrastructure/readiness checks. They are not emulator builds and do not produce an EXE, APK, or AAB.

## Build jobs to add after source integration

### Windows
- Check out the selected, pinned emulator source and recursive submodules.
- Install the exact CMake, compiler, Qt, and dependency versions required by that source revision.
- Configure using the verified Windows CMake preset.
- Compile Release.
- Run available automated tests.
- Package and upload a clearly labelled CI artifact.

### Android
- Check out the same pinned source revision and recursive submodules.
- Install the documented Android SDK/NDK, Java, Gradle, and vcpkg dependencies.
- Configure the Android native build for supported ABIs.
- Build the Android app.
- Run available unit/instrumentation tests where practical.
- Upload a debug APK as a CI artifact; release signing must use protected repository secrets and must never expose signing keys.

## Release and security rules

- Pin third-party GitHub Actions to reviewed immutable commit SHAs before production release.
- Use least-privilege workflow permissions.
- Never place signing keys, passwords, firmware, game data, or private tokens in the repository.
- Generate an SBOM and complete dependency licence review before distributing binaries.
- Preserve all upstream notices and satisfy GPL-2.0 source-distribution requirements for any covered binaries.

## Next engineering gate

Select and pin a specific Vita3K upstream commit, complete the dependency/licence inventory for that exact revision, then create a compliant downstream integration branch. Only after the source tree and build configuration are present should CI jobs be promoted from readiness checks to actual emulator compilation.
