# Vita3K platform build evidence

## Purpose

The manual workflow `.github/workflows/vita3k-platform-build-evidence.yml` checks whether the pinned Vita3K revision can resolve its native dependencies and build on Android and Windows CI runners.

It checks out Vita3K at:

`c87e12578749d6267be9b0c669904fe22545b170`

and initializes its recursive submodules. It runs the upstream build scripts rather than substituting AKOREDE VITA's native-app scaffold.

## Android job

- Runs the upstream `.ci/setup-android.sh` dependency setup.
- Captures vcpkg package lists for `arm64-android` and `x64-android`.
- Captures the Gradle dependency report.
- Runs the upstream Android `Reldebug` build path (no signing secrets are supplied).
- Retains build logs, submodule revisions, CMake caches, and an inventory of produced APK/AAB files.

## Windows job

- Uses the upstream `ci-windows-msvc` CMake preset and `x64-windows-static-md` vcpkg triplet.
- Installs Qt 6.11.0 with the multimedia module, matching the pinned upstream CI workflow.
- Runs the upstream Windows build and tests.
- Retains build logs, vcpkg package list, CMake cache, project-file inventory, and submodule revisions.

## How to run

1. Open the [workflow in GitHub Actions](https://github.com/salamakorede853-alt/Akorede-vita/actions/workflows/vita3k-platform-build-evidence.yml).
2. Select **Run workflow** on the `main` branch.
3. Wait for both platform jobs to finish.
4. Download both artifacts:
   - `vita3k-android-build-evidence-c87e125`
   - `vita3k-windows-build-evidence-c87e125`
5. Upload both ZIP files into the AKOREDE VITA conversation for inspection.

## Interpretation and limitations

- A successful job demonstrates that this pinned upstream revision built in that CI environment; it does not establish compatibility on a particular phone or Windows PC.
- A failed job is diagnostic evidence. The first failing step and its full log must be reviewed before changing code or dependencies.
- The Android build is unsigned/Reldebug unless the upstream build script's environment changes; no signing secrets are required or provided.
- This workflow builds upstream Vita3K in an isolated CI checkout. It does **not** copy or integrate Vita3K source into AKOREDE VITA.
- Build success is not licence clearance. The unresolved psvpfstools provenance/licence questions, LGPL compliance analysis, and release-specific notices/source obligations remain open.
- Build artifacts are retained only as short-lived CI evidence; they are not project releases or game-content packages.
- The Android workflow uses upstream's own setup script, which installs both Android vcpkg triplets. The Windows workflow follows the upstream MSVC CI preset.

## Current status

Not yet run. No Android or Windows Vita3K build result should be claimed until the workflow completes and its artifacts are reviewed.
