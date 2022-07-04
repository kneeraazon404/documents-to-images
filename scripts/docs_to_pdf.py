from docx2pdf import convert

convert("input.docx")  # to convert a single file
convert("input.docx", "output.pdf")  # to convert a single file to a pdf named
convert("my_docx_folder/")  # to convert all files in a folder
