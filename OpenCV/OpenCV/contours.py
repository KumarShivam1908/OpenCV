import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Actual',img)

blank=np.zeros(img.shape,'uint8')
cv.imshow('Blank',blank)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

# blur=cv.GaussianBlur(img,(5,5),cv.BORDER_DEFAULT)
# cv.imshow('Blur',blur)
#
# canny=cv.Canny(blur,125,175)
# cv.imshow('Cascaded',canny)

ret,thresh=cv.threshold(gray,125,255,cv.THRESH_BINARY)
cv.imshow('Thresholded Image',thresh)

contours, hierarchies = cv.findContours(thresh,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
#contours is a list .
print(f"{len(contours)} coutour(s) were found!!")

cv.drawContours(blank,contours,-1,(0,0,255),2)
cv.imshow('Contours_inBalck',blank)
cv.waitKey(0)

'''
canny --> then get contours using that
threshold --> tehn get contours using the above function

'''