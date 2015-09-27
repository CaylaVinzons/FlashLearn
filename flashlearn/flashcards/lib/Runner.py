import numpy, cv2
from preProcessing import *
try:
	from imageReader import *
except: from ImageReader import *

def run(filepath):
	aggregate(filepath)
	string = readText(filepath)
	return string
