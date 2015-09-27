import numpy
import cv2

'''This is an image processing framework for python. It uses opencv and numpy. loadPhoto edits
a photo from a specified path and identifies the highlighting on the text.

getContours will form a contour around the highlighted portions to mark where to crop the highlighted
text.

Finally, aggregate will make a blank image and transfer all the pixels within the contours we found
over from the edited photo to the blank image, cropping out any unhighlighted text.

To use: Pass in a file path to aggregate and call the method to generate the image. Then
ImageReader.py will run tesseract on the image to extract the text.'''

def getContours(filepath): #filepath should be string
#filepath is a string
    photo = cv2.imread(filepath, 1) #1 means read in color

    height, width = photo.shape[:2] #getting the dimensions of the image

    for i in range(width-1):
        for j in range(height-1):
            blue = photo.item(j, i, 0) #blue value at this point
            green = photo.item(j, i, 1)
            red = photo.item(j, i, 2)

            if blue > 240 and green > 240 and red > 240: #if color is white
                photo.itemset((j, i, 0), 0) #set it to black
                photo.itemset((j, i, 1), 0)
                photo.itemset((j, i, 2), 0)

    photo = cv2.cvtColor(photo, cv2.COLOR_BGR2GRAY)
    photo = cv2.equalizeHist(photo)
    kernel1 = numpy.ones((0,0),numpy.uint8) #defining kernely for morphology
    kernel2 = numpy.ones((1,1),numpy.uint8)
    photo = cv2.morphologyEx(photo, cv2.MORPH_CLOSE, kernel2)
    photo = cv2.morphologyEx(photo, cv2.MORPH_OPEN, kernel1)

    ret, photo = cv2.threshold(photo, 0, 10, cv2.THRESH_BINARY)
    photo, contours, hierarchy = cv2.findContours(photo,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    finalconts = []
    for i in range(len(contours)):
        if cv2.arcLength(contours[i], True) > 300:
            finalconts.append(contours[i])

    return finalconts
    #photo = cv2.drawContours(photo, finalconts, -1,(255,0,0),3)
    #cv2.imwrite('edited.png', photo)


def loadPhoto(filepath):
    #filepath is a string
    photo = cv2.imread(filepath, 1) #1 means read in color

    height, width = photo.shape[:2] #getting the dimensions of the image

    for i in range(width-1):
        for j in range(height-1):
            blue = photo.item(j, i, 0) #blue value at this point
            green = photo.item(j, i, 1)
            red = photo.item(j, i, 2)

            if blue < 140 and green > 190 and red > 210: #if color is yellowish
                photo.itemset((j, i, 0), 255) #set it to white.
                photo.itemset((j, i, 1), 255)
                photo.itemset((j, i, 2), 255)
    
    return photo

def aggregate(filepath):
    contours = getContours(filepath) #get list of contours
    photo = loadPhoto(filepath) #this gives us very clean photo
    height, width = photo.shape[:2]

    blank_image = numpy.zeros((height,width,3), numpy.uint8)
    blank_image[:, 0:width] = (255,255,255)

    for k in range(len(contours)):
        for i in range(width-1):
            for j in range(height-1):
                if cv2.pointPolygonTest(contours[k], (i, j), False) == 1:
                    blank_image.itemset((j, i, 0), photo.item(j, i, 0))
                    blank_image.itemset((j, i, 1), photo.item(j, i, 1))
                    blank_image.itemset((j, i, 2), photo.item(j, i, 2))

    blank_image = cv2.cvtColor(blank_image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('edited.png', blank_image) #saves to working directory
    
aggregate("/Users/zhangj/Desktop/stuff.png")
