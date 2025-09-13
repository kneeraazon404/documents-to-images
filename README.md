# Documents to Images Converter

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive Python toolkit for converting various document formats into images and other formats. This project provides a unified interface for document conversion operations including PDF generation, image extraction, and format transformation.

## 🚀 Features

### Document Conversion Support
- **PDF to Images**: Convert PDF pages to high-quality JPEG/PNG images
- **DOCX to PDF**: Convert Word documents to PDF format
- **PPTX to PDF**: Convert PowerPoint presentations to PDF
- **TXT to PDF**: Convert plain text files to formatted PDF
- **HTML to PDF**: Convert HTML files or web pages to PDF
- **DOCX to HTML**: Convert Word documents to HTML format

### Key Capabilities
- **Batch Processing**: Convert multiple files at once
- **High-Quality Output**: Configurable resolution and format options
- **Multi-page Support**: Handle documents with multiple pages efficiently
- **Cross-Platform**: Works on Linux, Windows, and macOS
- **Command-Line Interface**: Easy-to-use CLI tools
- **Programmatic API**: Import as a Python package for custom workflows

## 📋 Requirements

### System Dependencies
- Python 3.8 or higher
- LibreOffice (for DOCX, PPTX, TXT to PDF conversion)
- wkhtmltopdf (for HTML to PDF conversion)

### Python Dependencies
All Python dependencies are listed in `requirements.txt` and will be installed automatically.

## 🔧 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kneeraazon404/documents-to-images.git
cd documents-to-images
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 4. Install System Dependencies

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install libreoffice wkhtmltopdf unoconv
```

#### macOS
```bash
brew install libreoffice wkhtmltopdf
```

#### Windows
- Download and install LibreOffice from [official website](https://www.libreoffice.org/download/download/)
- Download and install wkhtmltopdf from [official website](https://wkhtmltopdf.org/downloads.html)

## 🚀 Quick Start

### Command Line Usage

#### Convert PDF to Images
```bash
python -m doc_converter.pdf_to_images input.pdf --output-dir ./images --format jpeg
```

#### Convert DOCX to PDF
```bash
python -m doc_converter.docx_to_pdf input.docx --output output.pdf
```

#### Convert HTML to PDF
```bash
python -m doc_converter.html_to_pdf https://example.com --output webpage.pdf
```

#### Batch Convert Multiple Files
```bash
python -m doc_converter.batch_convert --input-dir ./documents --output-dir ./converted --format pdf
```

### Programmatic Usage

```python
from doc_converter import DocumentConverter

# Initialize converter
converter = DocumentConverter()

# Convert PDF to images
images = converter.pdf_to_images('document.pdf', output_dir='./images')

# Convert DOCX to PDF
pdf_path = converter.docx_to_pdf('document.docx', output_path='output.pdf')

# Convert HTML to PDF
converter.html_to_pdf('https://example.com', 'webpage.pdf')

# Batch conversion
results = converter.batch_convert(
    input_dir='./documents',
    output_dir='./converted',
    target_format='pdf'
)
```

## 📁 Project Structure

```
documents-to-images/
├── doc_converter/              # Main package
│   ├── __init__.py
│   ├── core/                   # Core conversion modules
│   │   ├── __init__.py
│   │   ├── pdf_converter.py
│   │   ├── docx_converter.py
│   │   ├── html_converter.py
│   │   └── batch_processor.py
│   ├── cli/                    # Command-line interface
│   │   ├── __init__.py
│   │   └── main.py
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── file_handler.py
│       └── config.py
├── tests/                      # Test suite
│   ├── __init__.py
│   ├── test_pdf_converter.py
│   ├── test_docx_converter.py
│   └── fixtures/               # Test files
├── examples/                   # Example scripts and files
│   ├── sample_documents/
│   └── usage_examples.py
├── docs/                       # Documentation
│   ├── api_reference.md
│   └── troubleshooting.md
├── requirements.txt
├── setup.py
├── README.md
├── LICENSE
└── .gitignore
```

## 🔧 Configuration

Create a `config.yaml` file to customize default settings:

```yaml
# Default output settings
output:
  image_format: "jpeg"
  image_quality: 95
  pdf_quality: "high"
  
# Conversion settings
conversion:
  batch_size: 10
  timeout: 300
  
# Paths
paths:
  temp_dir: "./temp"
  output_dir: "./output"
```

## 📚 API Reference

### DocumentConverter Class

#### `pdf_to_images(pdf_path, output_dir=None, format='jpeg', dpi=200)`
Convert PDF pages to image files.

**Parameters:**
- `pdf_path` (str): Path to the PDF file
- `output_dir` (str, optional): Output directory for images
- `format` (str): Output format ('jpeg', 'png')
- `dpi` (int): Resolution in DPI

**Returns:**
- `List[str]`: List of created image file paths

#### `docx_to_pdf(docx_path, output_path=None)`
Convert DOCX file to PDF.

**Parameters:**
- `docx_path` (str): Path to the DOCX file
- `output_path` (str, optional): Output PDF path

**Returns:**
- `str`: Path to the created PDF file

#### `html_to_pdf(html_source, output_path, options=None)`
Convert HTML to PDF.

**Parameters:**
- `html_source` (str): HTML file path or URL
- `output_path` (str): Output PDF path
- `options` (dict, optional): Additional conversion options

**Returns:**
- `str`: Path to the created PDF file

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
python -m pytest tests/

# Run with coverage
python -m pytest tests/ --cov=doc_converter

# Run specific test file
python -m pytest tests/test_pdf_converter.py -v
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Add tests** for new functionality
5. **Run the test suite**
   ```bash
   python -m pytest tests/
   ```
6. **Commit your changes**
   ```bash
   git commit -m "Add amazing feature"
   ```
7. **Push to your branch**
   ```bash
   git push origin feature/amazing-feature
   ```
8. **Open a Pull Request**

### Development Setup

```bash
# Install development dependencies
pip install -r requirements-dev.txt

# Install pre-commit hooks
pre-commit install

# Run code formatting
black doc_converter/
isort doc_converter/

# Run linting
pylint doc_converter/
```

## 📖 Examples

Check the `examples/` directory for more detailed usage examples:

- `basic_conversion.py`: Simple conversion examples
- `batch_processing.py`: Batch conversion workflows
- `advanced_options.py`: Using advanced configuration options

## 🐛 Troubleshooting

### Common Issues

**LibreOffice not found**
```bash
# Add LibreOffice to PATH or specify full path
export PATH=$PATH:/usr/lib/libreoffice/program
```

**wkhtmltopdf permission issues**
```bash
# Install with correct permissions
sudo apt-get install wkhtmltopdf
```

**PDF conversion fails**
- Ensure input files are not corrupted
- Check file permissions
- Verify system dependencies are installed

For more troubleshooting tips, see `docs/troubleshooting.md`.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [pdf2image](https://github.com/Belval/pdf2image) for PDF to image conversion
- [python-docx](https://python-docx.readthedocs.io/) for DOCX processing
- [wkhtmltopdf](https://wkhtmltopdf.org/) for HTML to PDF conversion
- [LibreOffice](https://www.libreoffice.org/) for office document conversion

## 📞 Support

- Create an [Issue](https://github.com/kneeraazon404/documents-to-images/issues) for bug reports or feature requests
- Check existing issues before creating new ones
- Provide detailed information including error messages and system details

---

**Happy Converting! 🎉**  
