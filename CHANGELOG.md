# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.0] - 2024-03-21

### Added
- Initial release of RTVA Downloader
- Automatic extraction of m3u8 URLs from Canal Sur and RTVA websites
- Direct m3u8 URL support for manual downloads
- Multi-platform support (Linux, macOS, Windows)
- Automatic filename sanitization from page titles
- Progress display during downloads
- Quality selection support (1080p, 720p, etc.)
- Command-line interface with argparse
- Error handling and user-friendly messages
- MIT License
- Comprehensive README with examples
- GitHub Actions CI/CD pipeline
- setup.py for PyPI distribution

### Features
- Cross-platform compatibility
- No re-encoding (preserves original quality)
- Support for HLS streams
- Configurable output directory
- Option to hide progress output

[Unreleased]: https://github.com/joseluismolina/rtva-downloader/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/joseluismolina/rtva-downloader/releases/tag/v1.0.0
