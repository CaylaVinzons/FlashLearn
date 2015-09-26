try:
    import Image
except ImportError:
    from PIL import Image
import os
from pytesseract import *

print(os.listdir())
i = Image.open("/Users/zhangj/Desktop/FlashLearn/flashlearn/flashcards/lib/tesseract.png")
print(image_to_string(i))
#print(pytesseract.image_to_string(Image.open('tesseract.png')))
