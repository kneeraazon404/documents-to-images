# Test PyPI Publishing Guide

This guide will help you test your package before publishing to PyPI.

## 1. Build the Package

First, let's build the package to ensure everything is set up correctly:

```bash
# Activate virtual environment
source venv/bin/activate

# Install build tools
pip install build twine

# Build the package
python -m build

# This will create:
# dist/documents_to_images_converter-1.0.0.tar.gz
# dist/documents_to_images_converter-1.0.0-py3-none-any.whl
```

## 2. Test Installation Locally

Test that your package can be installed:

```bash
# Create a new test environment
python -m venv test_env
source test_env/bin/activate

# Install from the built wheel
pip install dist/documents_to_images_converter-1.0.0-py3-none-any.whl

# Test the CLI
doc-converter --version

# Test importing
python -c "import doc_converter; print('Package imported successfully!')"
```

## 3. Upload to Test PyPI

Before uploading to the real PyPI, test on Test PyPI:

```bash
# Upload to Test PyPI
twine upload --repository testpypi dist/*

# You'll be prompted for credentials:
# Username: __token__
# Password: [your TestPyPI API token]
```

## 4. Test Install from Test PyPI

```bash
# Create another test environment
python -m venv testpypi_env
source testpypi_env/bin/activate

# Install from Test PyPI
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ documents-to-images-converter

# Test the installation
doc-converter --version
```

## 5. Upload to Real PyPI

Once everything works on Test PyPI:

```bash
# Upload to real PyPI
twine upload dist/*

# You'll need your real PyPI API token
```

## API Tokens Setup

### Test PyPI Token
1. Go to https://test.pypi.org/
2. Register/Login
3. Go to Account Settings > API Tokens
4. Create a new token for this project
5. Copy the token (starts with `pypi-`)

### Real PyPI Token
1. Go to https://pypi.org/
2. Register/Login (same account as Test PyPI)
3. Go to Account Settings > API Tokens
4. Create a new token for this project
5. Copy the token

## GitHub Actions Setup

To set up automatic publishing via GitHub Actions:

1. Go to your GitHub repository
2. Settings > Secrets and Variables > Actions
3. Add these secrets:
   - `PYPI_API_TOKEN`: Your real PyPI token
   - `TEST_PYPI_API_TOKEN`: Your Test PyPI token

The GitHub Actions workflows are already configured in `.github/workflows/`

## Version Management

When releasing new versions:

1. Update version in `doc_converter/__init__.py`
2. Update `CHANGELOG.md`
3. Commit changes
4. Create a git tag: `git tag v1.0.1`
5. Push tag: `git push origin v1.0.1`
6. GitHub Actions will automatically build and publish

## Troubleshooting

### Common Issues

1. **Package already exists**: Increment version number
2. **Missing dependencies**: Check `pyproject.toml` dependencies
3. **Import errors**: Ensure all modules are properly included
4. **CLI not working**: Check `console_scripts` in `pyproject.toml`

### Manual Build Commands

```bash
# Clean previous builds
rm -rf dist/ build/

# Build source distribution and wheel
python -m build

# Check the package
twine check dist/*
```

## Next Steps

After successful publishing:

1. ✅ Package is available on PyPI
2. ✅ Users can install with `pip install documents-to-images-converter`
3. ✅ Documentation is ready for ReadTheDocs
4. ✅ CI/CD pipeline is set up

Visit your package at: `https://pypi.org/project/documents-to-images-converter/`