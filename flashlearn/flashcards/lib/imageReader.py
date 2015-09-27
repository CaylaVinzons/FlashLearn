try:
    import Image
except ImportError:
    from PIL import Image
import os
from pytesseract import *


def readText(filepath):
	i = Image.open(filepath)
	i.load()
	i.split()
	print(image_to_string(i))

readText("/Users/zhangj/Desktop/FlashLearn/flashlearn/flashcards/lib/edited.png")
