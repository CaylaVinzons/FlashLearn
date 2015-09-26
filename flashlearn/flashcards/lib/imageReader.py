try:
    import Image
except ImportError:
    from PIL import Image
import os
import pytesseract

print(os.listdir())
i=Image.open("tesseract.png")
pytesseract.image_to_string(i)
#print(pytesseract.image_to_string(Image.open('tesseract.png')))