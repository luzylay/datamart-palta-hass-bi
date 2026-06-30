import docx
import sys

def check_dict(filename):
    try:
        doc = docx.Document(filename)
        for i, table in enumerate(doc.tables):
            if i >= 95 and i <= 106:
                header = [cell.text.strip().replace('\n', ' ') for cell in table.rows[0].cells]
                # Print the paragraph immediately preceding the table to identify it
                prev_text = ""
                # We can search through paragraphs to find the one closest before this table?
                # A simpler way is just to print the table content (first 2 rows)
                print(f"\n--- TABLE {i} ---")
                print(f"Header: {header}")
                if len(table.rows) > 1:
                    row1 = [cell.text.strip().replace('\n', ' ') for cell in table.rows[1].cells]
                    print(f"Row1: {row1}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_dict(sys.argv[1])
