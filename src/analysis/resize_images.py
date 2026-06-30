import docx
from docx.shared import Inches
import sys

def resize_images(filename):
    doc = docx.Document(filename)
    for shape in doc.inline_shapes:
        # standard width 6.0 inches
        target_width = Inches(6.0)
        
        # calculate aspect ratio
        ratio = shape.height / float(shape.width)
        
        # set new dimensions
        shape.width = int(target_width)
        shape.height = int(target_width * ratio)
        
    doc.save(filename)
    print("Images resized successfully.")

if __name__ == "__main__":
    resize_images(sys.argv[1])
