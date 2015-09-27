import numpy
import cv2

print('hello world')

def loadPhoto(filepath):
    #filepath is a string
    photo = cv2.imread(filepath, 1) #1 means read in color

    #cv2.imshow('stupidity', photo)
    #cv2.waitKey(0) #closes the window when key is pressed.
    #cv2.destroyAllWindows()
    height, width = photo.shape[:2] #getting the dimensions of the image
    print(height, width)


    for i in range(width-1):
        for j in range(height-1):
            blue = photo.item(j, i, 0) #blue value at this point
            green = photo.item(j, i, 1)
            red = photo.item(j, i, 2)
            '''if 120 < clr[-1] <= 255 and 150 < clr[1] <= 255 and clr[0] < 60:
                continue #this means its yellow, keep it'''
            if blue > 100 and green > 100 and red > 100: #if color is greyish to white
                photo.itemset((j, i, 0), 0) #set it to black.
                photo.itemset((j, i, 1), 0)
                photo.itemset((j, i, 2), 0)

    cv2.imwrite('edited.png', photo)

'''cv2.imwrite(String filename, img)'''
#the above will save the img file after processing
#as watever filename you provide.

loadPhoto('/Users/zhangj/Desktop/FlashLearn/flashlearn/flashcards/lib/tesseract.png')


