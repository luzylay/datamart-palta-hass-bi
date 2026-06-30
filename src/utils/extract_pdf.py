import sys
import PyPDF2

def extract_pdf_text(filename):
    with open(filename, 'rb') as f:
        reader = PyPDF2.PdfReader(f)
        text = ""
        for i, page in enumerate(reader.pages):
            text += f"\n--- Page {i+1} ---\n"
            text += page.extract_text()
    
    with open('pdf_text.txt', 'w', encoding='utf-8') as out:
        out.write(text)
    print(f"Extracted {len(reader.pages)} pages to pdf_text.txt")

if __name__ == "__main__":
    extract_pdf_text(sys.argv[1])
