import re, pypdf

with open("Offer_letter_signed.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    for page_number, page in enumerate(reader.pages):
        text = page.extract_text()
        company = re.findall(r"Infocepts", text)
        print(f"Page {page_number+1}: {company}")