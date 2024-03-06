import cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Actual',img)

'''
#Converting to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

'''

#How to blur an image
blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
#cv.imshow('Blur',blur)

''''''


#Edge Cascading

canny=cv.Canny(blur,150,150)
#cv.imshow('Canny',canny)

#Dialating a image-Dilation adds pixels to the boundaries of objects in an image

dialate=cv.dilate(canny,(11,11),iterations=3)
# cv.imshow('Dialated',dialate)


#Eroding a image-Eroding an image using cv2 means to shrink the foreground object in an image.

erode=cv.erode(dialate,(11,11),iterations=1)
# cv.imshow('Erode',erode)

#Resize and crop the image
reszied=cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('Resized',reszied)

crop=img[50:200 ,200:400]
cv.imshow('Crop',crop)
cv.waitKey(0)