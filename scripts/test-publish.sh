#!/bin/bash
# Script to publish to Test PyPI for testing

set -e

echo "🧪 Publishing to Test PyPI"
echo "=========================="

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the project root."
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Install build dependencies
echo "📦 Installing build dependencies..."
python -m pip install --upgrade build twine

# Build package
echo "🏗️  Building package..."
python -m build

# Check the package
echo "🔍 Checking package..."
python -m twine check dist/*

# Upload to Test PyPI
echo "🧪 Publishing to Test PyPI..."
python -m twine upload --repository testpypi dist/*

echo "✅ Package successfully published to Test PyPI!"
echo "📦 View at: https://test.pypi.org/project/documents-to-images-converter/"
echo ""
echo "🧪 To test installation:"
echo "pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ documents-to-images-converter"