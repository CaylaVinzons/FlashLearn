import numpy, cv2
from preProcessing import *
try:
	from imageReader import *
except: from ImageReader import *

import sys


aggregate(sys.argv[1])
string = readText(sys.argv[1])
print(string)
