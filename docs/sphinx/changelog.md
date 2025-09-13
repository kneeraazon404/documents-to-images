# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Initial release of Documents to Images Converter
- PDF to images conversion (JPEG, PNG)
- DOCX to PDF conversion
- PPTX to PDF conversion
- TXT to PDF conversion
- HTML to PDF conversion
- DOCX to HTML conversion
- Batch processing capabilities
- Command line interface
- Configuration management
- Comprehensive error handling
- Parallel processing support
- High-quality image output options
- Progress tracking for batch operations

### Features
- Support for multiple input formats
- Configurable output settings (DPI, format, page ranges)
- Robust error handling and logging
- Cross-platform compatibility (Windows, macOS, Linux)
- Memory-efficient processing
- CLI with comprehensive options
- Python API for programmatic use
- Batch conversion with progress tracking

## [1.0.0] - 2024-01-XX

### Initial Release
- Core document conversion functionality
- PDF to images conversion
- Document to PDF conversions (DOCX, PPTX, TXT, HTML)
- DOCX to HTML conversion
- Command line interface
- Python API
- Batch processing
- Configuration management
- Comprehensive documentation
- Test suite with high coverage

### System Requirements
- Python 3.8+
- Poppler (for PDF processing)
- LibreOffice (optional, for enhanced DOCX/PPTX conversion)

### Supported Formats

#### Input Formats
- PDF
- DOCX (Microsoft Word)
- PPTX (Microsoft PowerPoint)
- TXT (Plain text)
- HTML (Local files and URLs)

#### Output Formats
- JPEG images
- PNG images
- PDF
- HTML

### Breaking Changes
- None (initial release)

### Known Issues
- Large PDF files may require substantial memory
- HTML to PDF conversion depends on web rendering engine
- Some complex DOCX formatting may not be preserved perfectly

---

## Development

### How to Contribute

See [Contributing Guidelines](contributing.md) for details on:
- Setting up development environment
- Code style and testing requirements
- Submitting pull requests

### Release Process

1. Update version number in `doc_converter/__init__.py`
2. Update this CHANGELOG.md with release notes
3. Create and merge release PR
4. Tag release on main branch
5. GitHub Actions automatically publishes to PyPI

### Version History

- **1.0.0**: Initial public release with core functionality
- **Future releases**: See [Unreleased] section above