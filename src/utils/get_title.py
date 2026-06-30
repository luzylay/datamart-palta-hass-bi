import docx
import sys

def get_title(filename):
    try:
        doc = docx.Document(filename)
        for i in range(20):
            print(f"P{i}: {doc.paragraphs[i].text.encode('ascii', errors='ignore').decode()}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_title(sys.argv[1])
