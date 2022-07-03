# setup the convert_client
convert_client = ConvertClient(pdf4me_client)

# create the convert_to_pdf object
convert_to_pdf = ConvertToPdf(
    document=Document(
        doc_data=FileReader().get_file_data("my_word_doc.docx"), name="my_word_doc.docx"
    ),
    convert_to_pdf_action=ConvertToPdfAction(),
)

# conversion
res = convert_client.convert_to_pdf(convert_to_pdf=convert_to_pdf)

# extracting the generated PDF
generated_pdf = base64.b64decode(res["document"]["doc_data"])
# writing it to disk
with open("generated_pdf.pdf", "wb") as f:
    f.write(generated_pdf)
