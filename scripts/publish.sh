#!/bin/bash
# Script to build and publish the package to PyPI

set -e

echo "🚀 Building and Publishing Documents to Images Converter to PyPI"
echo "================================================================"

# Check if we're in the right directory
if [ ! -f "pyproject.toml" ]; then
    echo "❌ Error: pyproject.toml not found. Please run this script from the project root."
    exit 1
fi

# Check if git working directory is clean
if [ -n "$(git status --porcelain)" ]; then
    echo "⚠️  Warning: Git working directory is not clean. Uncommitted changes:"
    git status --short
    read -p "Do you want to continue? (y/n) " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        exit 1
    fi
fi

# Get current version
current_version=$(python -c "import doc_converter; print(doc_converter.__version__)")
echo "📦 Current version: $current_version"

# Ask for version bump
echo "Select version bump type:"
echo "1) Patch (e.g., 1.0.0 -> 1.0.1)"
echo "2) Minor (e.g., 1.0.0 -> 1.1.0)" 
echo "3) Major (e.g., 1.0.0 -> 2.0.0)"
echo "4) Use current version"
read -p "Choice (1-4): " version_choice

case $version_choice in
    1)
        echo "🔧 Patch version bump selected"
        # You would implement version bumping logic here
        ;;
    2)
        echo "🔧 Minor version bump selected"
        ;;
    3)
        echo "🔧 Major version bump selected"
        ;;
    4)
        echo "🔧 Using current version: $current_version"
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Install build dependencies
echo "📦 Installing build dependencies..."
python -m pip install --upgrade build twine

# Run tests
echo "🧪 Running tests..."
python -m pytest tests/ -x -v

# Build package
echo "🏗️  Building package..."
python -m build

# Check the package
echo "🔍 Checking package..."
python -m twine check dist/*

# List built files
echo "📁 Built files:"
ls -la dist/

# Ask for confirmation
echo ""
echo "🤔 Ready to publish to PyPI?"
echo "Files to upload:"
ls -1 dist/
echo ""
read -p "Publish to PyPI? (y/n) " -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "❌ Publication cancelled"
    exit 1
fi

# Upload to PyPI
echo "🚀 Publishing to PyPI..."
python -m twine upload dist/*

echo "✅ Package successfully published to PyPI!"
echo "📦 View at: https://pypi.org/project/documents-to-images-converter/"
echo ""
echo "🎉 Don't forget to:"
echo "   - Create a git tag for this version"
echo "   - Update the CHANGELOG.md"
echo "   - Create a GitHub release"