import re
import pypdf

with open(r"../../docs/Offer_letter_signed.pdf", "rb") as file:
    reader = pypdf.PdfReader(file)
    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()
        pattern = r"\b[\d,]+(?:\.\d{2})?\b"
        amounts = re.findall(pattern,text)
        print(f"Page {page_num}: {amounts}")
        # print(text)

