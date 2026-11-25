import json
import logging
from pathlib import Path
from pypdf import PdfReader

def extract_pdf_text(pdf_path: Path) -> str:
    reader = PdfReader(pdf_path)
    
    if reader.is_encrypted:
        reader.decrypt("")

    pages_text = []
    for page_num, page in enumerate(reader.pages, start=1):
        try:
            text = page.extract_text() or ""
            pages_text.append(f"--- Page {page_num} --- \n {text}")
        except Exception as exc:
            logging.warning(f"Page {page_num} failed in {pdf_path.name}: {exc}")

    return "\n\n".join(pages_text)


def process_folder(input_dir: str, output_json: str) -> None:
    input_path = Path(input_dir)
    pdf_files = sorted(p for p in input_path.rglob("*") 
                       if p.is_file() and p.suffix.lower() == ".pdf")
    success_count = 0
    failed_count = 0

    with open(output_json, "w") as out_file:
        for pdf_path in pdf_files:
            try:
                content = extract_pdf_text(pdf_path)
                record = {
                        "file_name":pdf_path.name,
                        "relative_path":str(pdf_path.relative_to(input_path)),
                        "text":content
                        }
                out_file.write(json.dumps(record) + "\n")
                success_count += 1
            except Exception as exc:
                failed_count += 1
                logging.error(f"Skipped corrupted/unreadable PDF '{pdf_path}':{exc}")
                continue

        print(f"Done. Extracted:{success_count}|Skipped/Failed:{failed_count}")


if __name__ == "__main__":
    process_folder(input_dir="sample",output_json="sample.json")
