"""
Documents to Images Converter

A comprehensive Python toolkit for converting various document formats
into images and other formats.
"""

__version__ = "1.0.0"
__author__ = "Kiran Raj Baral"
__email__ = "kneeraazon404@gmail.com"

from .core.batch_processor import BatchProcessor
from .core.document_converter import DocumentConverter
from .core.docx_converter import DOCXConverter
from .core.html_converter import HTMLConverter
from .core.pdf_converter import PDFConverter

__all__ = [
    "DocumentConverter",
    "PDFConverter",
    "DOCXConverter",
    "HTMLConverter",
    "BatchProcessor",
]
