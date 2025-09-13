# Command Line Interface

The Documents to Images Converter provides a comprehensive CLI for all conversion operations.

## Installation Verification

Check if the CLI is installed correctly:

```bash
doc-converter --version
doc-converter --help
```

## Global Options

Available for all commands:

- `--verbose, -v`: Enable verbose logging
- `--quiet, -q`: Suppress output except errors
- `--config`: Specify custom config file
- `--output-dir`: Set output directory

## Commands

### pdf-to-images

Convert PDF pages to image files.

```bash
doc-converter pdf-to-images [OPTIONS] INPUT_FILE
```

**Options:**
- `--format`: Output image format (`jpeg`, `png`) [default: jpeg]
- `--dpi`: Image resolution in DPI [default: 200]
- `--first-page`: First page to convert [default: 1]
- `--last-page`: Last page to convert [default: all]
- `--output-dir`: Output directory [default: current directory]

**Examples:**
```bash
# Basic conversion
doc-converter pdf-to-images document.pdf

# High resolution JPEG
doc-converter pdf-to-images document.pdf --format jpeg --dpi 300

# Convert specific pages
doc-converter pdf-to-images document.pdf --first-page 5 --last-page 10

# Custom output directory
doc-converter pdf-to-images document.pdf --output-dir ./images
```

### docx-to-pdf

Convert Word documents to PDF.

```bash
doc-converter docx-to-pdf [OPTIONS] INPUT_FILE
```

**Options:**
- `--output`: Output PDF file path
- `--output-dir`: Output directory

**Examples:**
```bash
# Basic conversion
doc-converter docx-to-pdf document.docx

# Custom output file
doc-converter docx-to-pdf document.docx --output report.pdf
```

### pptx-to-pdf

Convert PowerPoint presentations to PDF.

```bash
doc-converter pptx-to-pdf [OPTIONS] INPUT_FILE
```

**Options:**
- `--output`: Output PDF file path
- `--output-dir`: Output directory

**Examples:**
```bash
# Basic conversion
doc-converter pptx-to-pdf presentation.pptx

# Custom output directory
doc-converter pptx-to-pdf presentation.pptx --output-dir ./pdfs
```

### txt-to-pdf

Convert text files to formatted PDF.

```bash
doc-converter txt-to-pdf [OPTIONS] INPUT_FILE
```

**Options:**
- `--output`: Output PDF file path
- `--font-size`: Font size for text [default: 12]
- `--font-family`: Font family [default: Arial]
- `--margins`: Page margins in points [default: 72]

**Examples:**
```bash
# Basic conversion
doc-converter txt-to-pdf notes.txt

# Custom formatting
doc-converter txt-to-pdf notes.txt --font-size 14 --font-family "Times New Roman"
```

### html-to-pdf

Convert HTML files or web pages to PDF.

```bash
doc-converter html-to-pdf [OPTIONS] INPUT_FILE_OR_URL
```

**Options:**
- `--output`: Output PDF file path [required]
- `--page-size`: Page size (A4, Letter, etc.) [default: A4]
- `--orientation`: Page orientation (portrait, landscape) [default: portrait]
- `--margins`: Page margins
- `--wait-time`: Wait time for page loading (for URLs)

**Examples:**
```bash
# Convert HTML file
doc-converter html-to-pdf report.html --output report.pdf

# Convert web page
doc-converter html-to-pdf https://example.com --output webpage.pdf

# Custom page settings
doc-converter html-to-pdf report.html --output report.pdf --page-size A4 --orientation landscape
```

### docx-to-html

Convert Word documents to HTML.

```bash
doc-converter docx-to-html [OPTIONS] INPUT_FILE
```

**Options:**
- `--output`: Output HTML file path
- `--extract-images`: Extract embedded images [default: true]
- `--image-dir`: Directory for extracted images

**Examples:**
```bash
# Basic conversion
doc-converter docx-to-html document.docx

# Extract images to custom directory
doc-converter docx-to-html document.docx --image-dir ./images
```

### batch-convert

Process multiple files at once.

```bash
doc-converter batch-convert [OPTIONS]
```

**Options:**
- `--input-dir`: Input directory [required]
- `--output-dir`: Output directory [required]
- `--operation`: Conversion operation [required]
- `--pattern`: File pattern to match [default: *]
- `--recursive`: Process subdirectories recursively
- `--parallel`: Number of parallel processes [default: 1]

**Supported Operations:**
- `pdf_to_images`
- `docx_to_pdf`
- `pptx_to_pdf`
- `txt_to_pdf`
- `html_to_pdf`
- `docx_to_html`

**Examples:**
```bash
# Convert all PDFs to images
doc-converter batch-convert --input-dir ./docs --output-dir ./images --operation pdf_to_images

# Convert all DOCX files to PDF
doc-converter batch-convert --input-dir ./word_docs --output-dir ./pdfs --operation docx_to_pdf

# Process with specific pattern
doc-converter batch-convert --input-dir ./docs --output-dir ./output --operation pdf_to_images --pattern "*.pdf"

# Parallel processing
doc-converter batch-convert --input-dir ./docs --output-dir ./output --operation pdf_to_images --parallel 4
```

## Configuration File

Create a YAML configuration file for default settings:

```yaml
# doc_converter_config.yaml
pdf_to_images:
  format: jpeg
  dpi: 300

html_to_pdf:
  page_size: A4
  orientation: portrait

output:
  base_dir: ./output
  create_subdirs: true

logging:
  level: INFO
  file: converter.log
```

Use with the CLI:

```bash
doc-converter --config doc_converter_config.yaml pdf-to-images document.pdf
```

## Exit Codes

- `0`: Success
- `1`: General error
- `2`: Invalid arguments
- `3`: File not found
- `4`: Conversion failed
- `5`: Permission denied

## Environment Variables

- `DOC_CONVERTER_CONFIG`: Default config file path
- `DOC_CONVERTER_OUTPUT_DIR`: Default output directory
- `DOC_CONVERTER_LOG_LEVEL`: Default logging level