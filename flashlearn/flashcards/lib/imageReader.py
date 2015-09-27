try:
    import Image
except ImportError:
    from PIL import Image
import os
from pytesseract import *


def readText(filepath): #returns string
	i = Image.open(filepath)
	i.load()
	i.split()
	return image_to_string(i)

