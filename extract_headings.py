import pdfplumber
import json
from utils import remove_headers_footers, extract_headings

def extract_text_from_pdf(pdf_path):
    pages_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
    return pages_text

if __name__ == "__main__":
    # Step 1: Extract raw text
    pdf_path = "/Users/hp/pdf_heading_extractor/normal_6203618ab0b7d.pdf"
    raw_pages = extract_text_from_pdf(pdf_path)

    # Step 2: Remove headers and footers
    cleaned_pages = remove_headers_footers(raw_pages)

    # Step 3: Extract hierarchical headings
    headings = extract_headings(cleaned_pages)

    # Step 4: Print result as JSON structure
    print("\n--- STRUCTURED HEADINGS ---\n")
    print(json.dumps(headings, indent=2))

    # Step 5: Save to JSON file
    with open("structured_headings.json", "w") as f:
        json.dump(headings, f, indent=2)
