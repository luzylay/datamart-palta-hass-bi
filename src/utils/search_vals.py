import docx
import sys

def search_values(filename):
    try:
        doc = docx.Document(filename)
        for i, p in enumerate(doc.paragraphs):
            text = p.text
            if "20.20" in text or "1847" in text or "1.72" in text or "838" in text or "2.05" in text or "Suiza e Israel" in text:
                print(f"Para {i}: {text.encode('ascii', errors='ignore').decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    search_values(sys.argv[1])
