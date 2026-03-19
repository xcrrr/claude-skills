# Changelog

All notable changes to this project will be documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).
This project uses [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- GitHub Actions CI workflow to validate all skills on every PR
- `generate_readme.py` script to auto-generate README skill tables from frontmatter
- `requirements.txt` with PyYAML dependency
- Broken relative link validation in `validate_skills.py`
- CHANGELOG.md

### Fixed
- Badge URLs in README.md now point to correct repository (xcrrr/claude-skills)
- GitHub Discussions and Issues links in CONTRIBUTING.md now point to correct repository
- YAML frontmatter parsing now uses PyYAML for robustness
