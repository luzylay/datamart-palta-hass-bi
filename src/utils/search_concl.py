import docx
import sys

def search_conclusions(filename):
    try:
        doc = docx.Document(filename)
        for i, p in enumerate(doc.paragraphs):
            text = p.text.strip()
            if "conclusi" in text.lower() or "recomendaci" in text.lower() or "viable" in text.lower() or "decisi" in text.lower():
                print(f"Para {i}: {text.encode('ascii', errors='ignore').decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_conclusions(sys.argv[1])
