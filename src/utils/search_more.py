import docx
import sys

def search_more(filename):
    try:
        doc = docx.Document(filename)
        for i, p in enumerate(doc.paragraphs):
            text = p.text
            if "838" in text or "1.7" in text or "Drokasa" in text or "Westfalia" in text or "DROKASA" in text or "WESTFALIA" in text:
                print(f"Para {i}: {text.encode('ascii', errors='ignore').decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_more(sys.argv[1])
