# To convert docs, pptx to pdf

## To convert docs to pdf

### installation

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
    lowriter --convert-to pdf sample.docx
```

#### for multiple file  conversion  (it can be doc or docx both)

```bash
    lowriter --convert-to pdf *.doc
```

## To convert pptx to pdf

```bash
    soffice --headless --convert-to pdf sample.pptx

```

## To convert txt to pdf

```bash
    soffice --headless --convert-to pdf sample.txt

    ```
