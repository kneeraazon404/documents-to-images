"""
Advanced usage examples demonstrating the full capabilities of the document converter.
"""

from pathlib import Path

from doc_converter import DocumentConverter
from doc_converter.core.batch_processor import BatchProcessor
from doc_converter.utils.config import Config


def advanced_pdf_processing():
    """Advanced PDF processing with configuration and error handling."""

    print("🔧 Advanced PDF Processing Example")

    # Create custom configuration
    config = Config()
    config.set("output.image_dpi", 300)
    config.set("output.image_quality", 95)

    converter = DocumentConverter()

    pdf_path = "examples/sample_documents/example.pdf"

    try:
        # Get page count first
        from doc_converter.core.pdf_converter import PDFConverter

        pdf_conv = PDFConverter()
        page_count = pdf_conv.get_page_count(pdf_path)
        print(f"📖 PDF has {page_count} pages")

        # Convert specific page range
        if page_count > 1:
            images = converter.pdf_to_images(
                pdf_path=pdf_path,
                output_dir="output/specific_pages",
                format="png",
                dpi=300,
            )
            print(f"✅ Converted pages to {len(images)} PNG images")

    except Exception as e:
        print(f"❌ Error processing PDF: {e}")


def batch_processing_with_progress():
    """Demonstrate batch processing with detailed progress tracking."""

    print("\n📦 Batch Processing with Progress Tracking")

    processor = BatchProcessor(max_workers=2)

    # Custom progress callback with more details
    def detailed_progress(current, total, filename):
        percentage = (current / total) * 100
        bar_length = 30
        filled_length = int(bar_length * current // total)
        bar = "█" * filled_length + "-" * (bar_length - filled_length)

        print(
            f"\r|{bar}| {current}/{total} ({percentage:.1f}%) - {filename[:30]:<30}",
            end="",
            flush=True,
        )
        if current == total:
            print()  # New line when complete

    try:
        results = processor.convert_directory(
            input_dir="examples/sample_documents",
            output_dir="output/batch_advanced",
            target_format="pdf",
            file_patterns=["*.docx", "*.txt", "*.html"],  # Specific patterns
            recursive=False,
            progress_callback=detailed_progress,
        )

        print("\n📊 Detailed Results:")
        print(f"   📁 Total files found: {results['total_files']}")
        print(f"   ✅ Successfully converted: {results['successful']}")
        print(f"   ❌ Failed conversions: {results['failed']}")

        if results["successful"] > 0:
            print("\n✨ Successful conversions:")
            for result in results["results"][:3]:  # Show first 3
                input_file = Path(result["input_file"]).name
                output_file = Path(result["output_file"]).name
                print(f"   📄 {input_file} → {output_file}")

        if results["errors"]:
            print("\n💥 Errors encountered:")
            for error in results["errors"][:3]:  # Show first 3
                filename = Path(error["file"]).name
                print(f"   ❌ {filename}: {error['error'][:60]}...")

    except Exception as e:
        print(f"❌ Batch processing error: {e}")


def html_to_pdf_with_options():
    """Demonstrate HTML to PDF conversion with custom options."""

    print("\n🌐 HTML to PDF with Custom Options")

    converter = DocumentConverter()

    # Custom wkhtmltopdf options
    options = {
        "page-size": "A4",
        "margin-top": "1in",
        "margin-right": "0.75in",
        "margin-bottom": "1in",
        "margin-left": "0.75in",
        "encoding": "UTF-8",
        "no-outline": None,
        "enable-local-file-access": None,
        "print-media-type": None,
        "disable-smart-shrinking": None,
    }

    try:
        # Convert local HTML file
        html_file = "examples/sample_documents/sample.html"
        pdf_output = "output/styled_webpage.pdf"

        result = converter.html_to_pdf(
            html_source=html_file, output_path=pdf_output, options=options
        )

        print(f"✅ HTML converted to PDF with custom styling: {result}")

        # Convert a URL (if internet is available)
        try:
            url_output = "output/python_docs.pdf"
            converter.html_to_pdf(
                html_source="https://docs.python.org/3/tutorial/",
                output_path=url_output,
                options={"page-size": "A4", "load-error-handling": "ignore"},
            )
            print(f"✅ URL converted to PDF: {url_output}")

        except Exception as url_error:
            print(f"⚠️  URL conversion skipped: {url_error}")

    except Exception as e:
        print(f"❌ HTML to PDF error: {e}")


def demonstrate_format_support():
    """Show all supported format conversions."""

    print("\n🔄 Format Support Demonstration")

    converter = DocumentConverter()
    formats = converter.get_supported_formats()

    print(f"📥 Supported input formats: {', '.join(formats['input'])}")
    print(f"📤 Supported output formats: {', '.join(formats['output'])}")

    # Try different conversions
    conversions = [
        (
            "examples/sample_documents/sample.docx",
            "docx_to_pdf",
            "output/demo_docx.pdf",
        ),
        (
            "examples/sample_documents/sample.txt",
            "txt_to_pdf",
            "output/demo_txt.pdf",
        ),
        (
            "examples/sample_documents/sample.docx",
            "docx_to_html",
            "output/demo_docx.html",
        ),
    ]

    for input_file, conversion_type, output_file in conversions:
        if not Path(input_file).exists():
            print(f"⚠️  Skipping {conversion_type}: input file not found")
            continue

        try:
            Path(output_file).parent.mkdir(parents=True, exist_ok=True)

            if conversion_type == "docx_to_pdf":
                result = converter.docx_to_pdf(input_file, output_file)
            elif conversion_type == "txt_to_pdf":
                result = converter.txt_to_pdf(input_file, output_file)
            elif conversion_type == "docx_to_html":
                result = converter.docx_to_html(input_file, output_file)

            print(
                f"✅ {conversion_type}: {
                    Path(input_file).name} → {
                    Path(result).name}"
            )

        except Exception as e:
            print(f"❌ {conversion_type} failed: {e}")


def configuration_example():
    """Demonstrate custom configuration usage."""

    print("\n⚙️  Configuration Management Example")

    # Create custom config
    config = Config()

    # Show default settings
    print("📋 Default Configuration:")
    print(f"   Image DPI: {config.get('output.image_dpi')}")
    print(f"   Max workers: {config.get('conversion.max_workers')}")
    print(f"   Timeout: {config.get('conversion.timeout')}")

    # Modify settings
    config.set("output.image_dpi", 300)
    config.set("conversion.max_workers", 2)
    config.set("conversion.timeout", 600)

    print("\n🔧 Modified Configuration:")
    print(f"   Image DPI: {config.get('output.image_dpi')}")
    print(f"   Max workers: {config.get('conversion.max_workers')}")
    print(f"   Timeout: {config.get('conversion.timeout')}")

    # Save configuration
    config_file = "output/custom_config.yaml"
    config.save_to_file(config_file)
    print(f"💾 Configuration saved to: {config_file}")

    # Load configuration to demonstrate usage
    Config(config_file)  # Demonstrate loading config
    DocumentConverter(config_file)  # Demonstrate with config
    print("✅ Loaded custom configuration for converter")


def error_handling_example():
    """Demonstrate proper error handling."""

    print("\n🛡️  Error Handling Examples")

    converter = DocumentConverter()

    # Test with non-existent file
    try:
        converter.pdf_to_images("non_existent.pdf")
    except FileNotFoundError as e:
        print(f"✅ Caught expected error: {e}")

    # Test with invalid format
    try:
        converter.pdf_to_images(
            "examples/sample_documents/example.pdf", format="invalid"
        )
    except ValueError as e:
        print(f"✅ Caught validation error: {e}")

    # Test batch processing with mixed results
    processor = BatchProcessor()

    # Create a mix of valid and invalid files
    test_files = [
        "examples/sample_documents/sample.docx",  # Valid
        "non_existent.docx",  # Invalid
        "examples/sample_documents/sample.txt",  # Valid
    ]

    try:
        results = processor.convert_file_list(
            file_list=test_files,
            output_dir="output/error_test",
            target_format="pdf",
        )

        print(
            f"📊 Mixed results: {
                results['successful']} success, {
                results['failed']} failures"
        )

    except Exception as e:
        print(f"⚠️  Batch processing handled errors gracefully: {e}")


def main():
    """Run all advanced examples."""
    print("🚀 Advanced Document Converter Examples\n")

    # Create output directory
    Path("output").mkdir(exist_ok=True)

    # Run examples
    advanced_pdf_processing()
    batch_processing_with_progress()
    html_to_pdf_with_options()
    demonstrate_format_support()
    configuration_example()
    error_handling_example()

    print("\n🎉 All advanced examples completed!")
    print("📁 Check the 'output' directory for generated files")


if __name__ == "__main__":
    main()
