import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')
cv.imshow('Actual',img)


#translating a image
def translate_image(img,x,y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimension=(img.shape[1],img.shape[0]) #(width,height)
    return cv.warpAffine(img,transMat,dimension)

'''
-x --> Left
+x --> Right
-y --> Up
+y --> Down

'''

translate=translate_image(img,100,100)
#cv.imshow('Translated',translate)

#Rotation
def rotate(img,angle,rotpoint=None):
    (height,width)=img.shape[:2]

    if rotpoint==None:
        rotpoint=(width//2,height//2)

    rotMat=cv.getRotationMatrix2D(rotpoint,angle,1.0)
    dimension=(width,height)

    return cv.warpAffine(img,rotMat,dimension)


rotated=rotate(img,180) #for clockwise use (-angle)
#cv.imshow('Rotated',rotated)

#Fliping the image
'''
flipcode
0 --> vertically
1 --> horizontally
-1 --> both vertically and horizonatally
'''
flip=cv.flip(img,-1)
cv.imshow('Flip',flip)

cv.waitKey(0)