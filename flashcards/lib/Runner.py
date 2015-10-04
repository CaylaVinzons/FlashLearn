import numpy, cv2
from preProcessing import *
from imageReader import *

import sys


aggregate(sys.argv[1])
string = readText(sys.argv[1])
print(string)
