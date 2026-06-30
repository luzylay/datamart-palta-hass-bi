import docx
import os
import hashlib

def get_image_hashes():
    hashes = {}
    for filename in ['regression_plot.png', 'seasonality_plot.png', 'ttest_plot.png']:
        if os.path.exists(filename):
            with open(filename, 'rb') as f:
                hashes[hashlib.md5(f.read()).hexdigest()] = filename
    return hashes

doc = docx.Document('Proyecto_IB_Grupo01.docx')
count = 0
found_hashes = set()

for rel in doc.part.rels.values():
    if "image" in rel.target_ref:
        blob = rel.target_part.blob
        count += 1
        h = hashlib.md5(blob).hexdigest()
        found_hashes.add(h)

print(f'Total images in docx: {count}')
expected_hashes = get_image_hashes()
for h, name in expected_hashes.items():
    if h in found_hashes:
        print(f"Found {name} in the document.")
    else:
        print(f"MISSING: {name} is NOT in the document.")
