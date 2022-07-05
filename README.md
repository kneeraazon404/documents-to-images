# DocumentsToImages

Converting Documents to Images using Python

## Clone the repo and  cd into DocumentsToImages

```bash
cd DocumentsToImages
```

## Create a virtual env for DocumentsToImages

```bash
python -m venv venv
```

## Activate the virtual env for linux and mac

```bash
source venv/bin/activate
```

## Install the dependencies with

```bash
pip install -r requirements.txt
```

## Copy your pdf file to the DocumentsToImages/Scripts/documents  folder

### replace the file name with your pdf file name

```bash
python pdf_to_img.py
```

## Converting html, either local or site to pdf

## for this you need pdfkit and wkhtmltopdf

### to install wkhtmltopdf on linux

```bash
sudo apt-get install wkhtmltopdf
```

### Finally run the following command to convert but make sure to change the file names in the script

```bash
python html_to_pdf.py
```
