# to convert docs, pptx to pdf with

## installation

### install cups-pdf

```bash
    sudo apt-get install cups-pdf
```

### install libreoffice

```bash
    sudo apt-get install libreoffice
```

### Now run the command to convert the docs to pdf

#### for single file conversion

```bash
    lowriter --convert-to pdf filename.docx
```

#### for multiple file  conversion  (it can be doc or docx both)

```bash
    lowriter --convert-to pdf *.doc
```
