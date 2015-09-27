try:
    import Image
except ImportError:
    from PIL import Image
import os
from pytesseract import *


i = Image.open("/Users/zhangj/Desktop/FlashLearn/flashlearn/flashcards/lib/edited.png")
print(image_to_string(i))
