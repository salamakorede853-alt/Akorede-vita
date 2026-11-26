# AKOREDE VITA — Architecture

**Status:** Proposed architecture (not yet implemented)  
**Targets:** Windows and Android  
**Primary language:** C++

## 1. Guiding principles

1. Keep the emulation engine independent from the user interface.
2. Prefer a proven, compatible open-source emulation foundation over rewriting the entire console stack.
3. Keep platform-specific code behind narrow interfaces.
4. Make builds reproducible and document every dependency.
5. Preserve upstream copyright notices and comply with all applicable licences.
6. Do not bundle proprietary firmware, keys, or copyrighted game content.

## 2. Strategy decision

The initial candidate for technical evaluation is Vita3K. Before integrating or modifying it, review its current source tree, licence, contribution guidance, build requirements, platform support, and upstream development status.

The project must choose one of these approaches after the audit:

- **Upstream-based product layer:** maintain a clearly documented downstream integration and add original UI/product features.
- **Contributed upstream changes:** submit generally useful emulator improvements upstream where practical, keeping original branding and product work separate.
- **Independent implementation:** only consider this if the audit identifies a compelling technical and licensing reason. This is the most expensive option and is not the default recommendation.

No upstream code has been vendored or modified in this repository at this stage.

## 3. Logical components

### Product experience
- Game library and metadata presentation
- Per-title configuration
- Controller mapping and input preferences
- Save-data and user-data management
- Settings, diagnostics, and compatibility reporting

### Shared application services
- Configuration persistence
- Input abstraction
- Logging and diagnostics
- File and directory access abstraction
- Update and build information

### Emulation integration
- CPU execution
- Memory and address-space management
- GPU and rendering
- Audio
- Operating-system and service API compatibility
- Timing and synchronization

These are conceptual boundaries. Exact module names and ownership must follow the selected upstream architecture rather than forcing an incompatible folder layout.

### Platform adapters
- Windows: windowing, graphics context, input, filesystem, packaging
- Android: lifecycle, surface management, touch input, controller input, storage permissions, packaging

## 4. Proposed repository organisation

The repository structure should evolve after the upstream audit. A possible product-layer layout is:

```text
Akorede-vita/
├── docs/
│   ├── ARCHITECTURE.md
│   └── ROADMAP.md
├── app/
│   ├── shared/
│   ├── windows/
│   └── android/
├── tests/
├── scripts/
├── assets/
├── CONTRIBUTING.md
├── LICENSES/
└── README.md
```

This is illustrative, not a requirement to relocate upstream files. If the project becomes a downstream fork, retain upstream structure and make product-specific additions clearly identifiable.

## 5. Build strategy

- Establish a known-good upstream build before making changes.
- Record compiler, SDK, NDK, CMake, and dependency versions.
- Automate builds and tests with CI where supported.
- Keep Windows and Android build configurations explicit.
- Separate third-party dependencies from original project code.
- Record build failures and known limitations rather than claiming untested support.

## 6. Security, privacy, and legal boundaries

- Never commit credentials, signing keys, personal tokens, or private user data.
- Do not include copyrighted game images, game dumps, proprietary firmware, or encryption keys.
- Users are responsible for ensuring they have the rights to any content they use.
- Include required licence texts, attribution, and corresponding source availability for redistributed copyleft components.
- Do not imply Sony endorsement or use Sony branding in a way that suggests an official product.

## 7. Immediate architecture questions

1. Which upstream revision is the baseline?
2. What exact licence and obligations apply to each reused component?
3. Which UI and rendering components can be shared across Windows and Android?
4. Which Android build dependencies and minimum OS versions are supported upstream?
5. What baseline tests can be run without proprietary game content?
