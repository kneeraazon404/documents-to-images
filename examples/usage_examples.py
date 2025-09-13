"""
Basic usage examples for the document converter.
"""

from pathlib import Path

from doc_converter import DocumentConverter


def example_pdf_to_images():
    """Example: Convert PDF to images."""
    converter = DocumentConverter()

    # Convert PDF to JPEG images
    pdf_path = "sample_documents/example.pdf"
    output_dir = "output/images"

    try:
        image_files = converter.pdf_to_images(
            pdf_path=pdf_path, output_dir=output_dir, format="jpeg", dpi=300
        )

        print(f"✅ Converted PDF to {len(image_files)} images")
        for img in image_files:
            print(f"   📷 {img}")

    except Exception as e:
        print(f"❌ Error: {e}")


def example_docx_to_pdf():
    """Example: Convert DOCX to PDF."""
    converter = DocumentConverter()

    docx_path = "sample_documents/document.docx"
    pdf_path = "output/converted_document.pdf"

    try:
        result = converter.docx_to_pdf(docx_path, pdf_path)
        print(f"✅ Converted DOCX to PDF: {result}")

    except Exception as e:
        print(f"❌ Error: {e}")


def example_html_to_pdf():
    """Example: Convert HTML/URL to PDF."""
    converter = DocumentConverter()

    # Convert local HTML file
    html_path = "sample_documents/webpage.html"
    pdf_path = "output/webpage.pdf"

    try:
        result = converter.html_to_pdf(html_path, pdf_path)
        print(f"✅ Converted HTML to PDF: {result}")

    except Exception as e:
        print(f"❌ Error: {e}")

    # Convert URL to PDF
    try:
        url = "https://www.python.org"
        pdf_path = "output/python_org.pdf"

        result = converter.html_to_pdf(url, pdf_path)
        print(f"✅ Converted URL to PDF: {result}")

    except Exception as e:
        print(f"❌ Error converting URL: {e}")


def example_batch_conversion():
    """Example: Batch convert multiple files."""
    from doc_converter.core.batch_processor import BatchProcessor

    processor = BatchProcessor(max_workers=2)

    input_dir = "sample_documents"
    output_dir = "output/batch_converted"

    def progress_callback(current, total, filename):
        percentage = (current / total) * 100
        print(f"Progress: {current}/{total} ({percentage:.1f}%) - {filename}")

    try:
        results = processor.convert_directory(
            input_dir=input_dir,
            output_dir=output_dir,
            target_format="pdf",
            recursive=True,
            progress_callback=progress_callback,
        )

        print(f"\n📊 Batch conversion results:")
        print(f"   ✅ Successful: {results['successful']}")
        print(f"   ❌ Failed: {results['failed']}")
        print(f"   📈 Total: {results['total_files']}")

        if results["errors"]:
            print(f"\nErrors:")
            for error in results["errors"]:
                print(f"   - {error['file']}: {error['error']}")

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    print("🚀 Document Converter Examples\n")

    # Create output directory
    Path("output").mkdir(exist_ok=True)

    print("1. Converting PDF to images...")
    example_pdf_to_images()

    print("\n2. Converting DOCX to PDF...")
    example_docx_to_pdf()

    print("\n3. Converting HTML to PDF...")
    example_html_to_pdf()

    print("\n4. Batch conversion...")
    example_batch_conversion()

    print("\n✨ Examples completed!")
