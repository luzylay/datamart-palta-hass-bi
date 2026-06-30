import docx
import sys

def check_end(filename):
    try:
        doc = docx.Document(filename)
        found = False
        for p in doc.paragraphs:
            if "7.6" in p.text or "7.7" in p.text or "8. CONCLUSIONES" in p.text:
                found = True
            if found:
                print(p.text.encode('ascii', errors='ignore').decode())
                if "9. REFERENCIAS" in p.text:
                    break
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_end(sys.argv[1])
