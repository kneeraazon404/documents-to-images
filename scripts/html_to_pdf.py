import pdfkit

# if you want your local html file to be converted to pdf.
pdfkit.from_url("filename.html", "shaurya.pdf")

#  If you want a site page to be converted to pdf
pdfkit.from_url("https://www.google.com", "google.pdf")


# ! replace google.com with the link of your choice
