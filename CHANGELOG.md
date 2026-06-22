# Changelog

All notable changes to this project will be documented in this file.

## [v5] - 2026-06-23

### Changed
- **Consolidated Skills**: Merged separate compact and pure calculation skill files (`fwft-core-compact.md` and `fwft-pure-calculation-output.md`) into a single, unified `SKILL.md` file under `skill/fwft-core/`.
- **System Directives**: Updated `GEMINI.md` to load the unified `fwft-core` skill and enforce strict Core Worker instructions, including numeric thinking constraints and local-worker data routing.
- **Documentation**: Updated `README.md` to replace deprecated file paths with the single consolidated `SKILL.md` references.

---

## [v4] - 2026-06-02

### Added
- **Dynamic Skill Router**: Introduced `skill_router.py` to support dynamic, token-optimized skill routing (tag extraction, semantic keyword detection, dependency mapping, and token estimation).
- **Global Integration**: Updated `GEMINI.md` references and expanded `README.md` to document the new `SkillRouter` API and execution options.

---

## [v3] - 2026-06-01

### Added
- **Comparison & Proofs**: Added screenshot comparison and detailed results to `README.md` highlighting behavior with and without FWFT active.
- **Compact Rules & PCO**: Introduced the first iterations of compact rules and Pure Calculation Output instructions.
- **Cursor Integration**: Created `.cursorrules` file to support Cursor AI workspace integration.
