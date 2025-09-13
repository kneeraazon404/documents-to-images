# API Reference

## Core Classes

### DocumentConverter

The main class for document conversion operations.

```{eval-rst}
.. autoclass:: doc_converter.core.converter.DocumentConverter
   :members:
   :undoc-members:
   :show-inheritance:
```

### BatchProcessor

Class for batch processing multiple files.

```{eval-rst}
.. autoclass:: doc_converter.core.batch_processor.BatchProcessor
   :members:
   :undoc-members:
   :show-inheritance:
```

## Converter Modules

### PDF Converter

```{eval-rst}
.. automodule:: doc_converter.core.pdf_converter
   :members:
   :undoc-members:
   :show-inheritance:
```

### Document Converters

```{eval-rst}
.. automodule:: doc_converter.core.docx_converter
   :members:
   :undoc-members:
   :show-inheritance:
```

```{eval-rst}
.. automodule:: doc_converter.core.pptx_converter
   :members:
   :undoc-members:
   :show-inheritance:
```

```{eval-rst}
.. automodule:: doc_converter.core.txt_converter
   :members:
   :undoc-members:
   :show-inheritance:
```

```{eval-rst}
.. automodule:: doc_converter.core.html_converter
   :members:
   :undoc-members:
   :show-inheritance:
```

## Utilities

### Configuration Management

```{eval-rst}
.. automodule:: doc_converter.utils.config
   :members:
   :undoc-members:
   :show-inheritance:
```

### File Operations

```{eval-rst}
.. automodule:: doc_converter.utils.file_utils
   :members:
   :undoc-members:
   :show-inheritance:
```

### Logging

```{eval-rst}
.. automodule:: doc_converter.utils.logger
   :members:
   :undoc-members:
   :show-inheritance:
```

## CLI Module

### Main CLI Interface

```{eval-rst}
.. automodule:: doc_converter.cli.main
   :members:
   :undoc-members:
   :show-inheritance:
```

### Command Handlers

```{eval-rst}
.. automodule:: doc_converter.cli.commands
   :members:
   :undoc-members:
   :show-inheritance:
```

## Exceptions

### Custom Exceptions

```{eval-rst}
.. automodule:: doc_converter.exceptions
   :members:
   :undoc-members:
   :show-inheritance:
```

## Constants and Enums

### Configuration Constants

```{eval-rst}
.. autodata:: doc_converter.config.DEFAULT_DPI
.. autodata:: doc_converter.config.SUPPORTED_FORMATS
.. autodata:: doc_converter.config.DEFAULT_OUTPUT_DIR
```