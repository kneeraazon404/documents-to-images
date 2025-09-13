"""
Test configuration and fixtures.
"""

from pathlib import Path

import pytest


@pytest.fixture
def temp_dir(tmp_path):
    """Create a temporary directory for tests."""
    return tmp_path


@pytest.fixture
def sample_documents_dir():
    """Path to sample documents directory."""
    return Path(__file__).parent.parent / "examples" / "sample_documents"


@pytest.fixture
def fixtures_dir():
    """Path to test fixtures directory."""
    return Path(__file__).parent / "fixtures"


# Create sample test files if they don't exist
def pytest_configure():
    """Configure pytest and create test fixtures."""
    fixtures_dir = Path(__file__).parent / "fixtures"
    fixtures_dir.mkdir(exist_ok=True)

    # Create a simple text file for testing
    sample_txt = fixtures_dir / "sample.txt"
    if not sample_txt.exists():
        sample_txt.write_text(
            "This is a sample text file for testing.\nSecond line of content."
        )

    # Create a simple HTML file for testing
    sample_html = fixtures_dir / "sample.html"
    if not sample_html.exists():
        sample_html.write_text(
            "<!DOCTYPE html>\n"
            "<html>\n"
            "<head><title>Test</title></head>\n"
            "<body><h1>Test Document</h1><p>This is a test.</p></body>\n"
            "</html>"
        )
