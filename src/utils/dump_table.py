import docx
import sys

def dump_table(filename, idx):
    try:
        doc = docx.Document(filename)
        table = doc.tables[idx]
        for row in table.rows:
            row_data = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
            print(str(row_data).encode("ascii", errors="ignore").decode())
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    dump_table(sys.argv[1], int(sys.argv[2]))
