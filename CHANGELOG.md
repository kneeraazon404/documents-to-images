# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2025-01-XX

### Initial Release

#### Added
- Core document conversion functionality
- PDF to images conversion (JPEG, PNG)
- Document to PDF conversions (DOCX, PPTX, TXT, HTML)
- DOCX to HTML conversion
- Command line interface
- Python API
- Batch processing
- Configuration management
- Comprehensive documentation
- Test suite with high coverage

#### System Requirements
- Python 3.8+
- Poppler (for PDF processing)
- LibreOffice (optional, for enhanced DOCX/PPTX conversion)

#### Supported Formats

##### Input Formats
- PDF
- DOCX (Microsoft Word)
- PPTX (Microsoft PowerPoint)
- TXT (Plain text)
- HTML (Local files and URLs)

##### Output Formats
- JPEG images
- PNG images
- PDF
- HTML

#### Breaking Changes
- None (initial release)

#### Known Issues
- Large PDF files may require substantial memory
- HTML to PDF conversion depends on web rendering engine
- Some complex DOCX formatting may not be preserved perfectly
- wkhtmltopdf dependency deprecated on macOS (functionality limited)