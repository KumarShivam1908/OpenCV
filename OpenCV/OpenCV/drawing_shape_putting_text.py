import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# #Paint the image in certain colour
# blank[200:300,300:400]=0,255,0
# # cv.imshow('Green',blank)
#  #draw a rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=2)  #cv.fill or -1 will fill the solid also rather than (250,250) blank.shape[0]//2 can also be written for all
# # cv.imshow('Rectangle',blank)
#
# #draw circle
#
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),40,(0,0,255),thickness=-1)
# # cv.imshow('Circle',blank)
#
# #draw a line
# cv.line(blank,(100,250),(500,500),(255,255,255),thickness=3)
# cv.imshow('Line',blank)


#How to write in a image using opencv

cv.putText(blank,'Hello my name is shivam',(0,225),cv.FONT_HERSHEY_TRIPLEX,1,(0,255,0),thickness=3)
cv.imshow('Text',blank)

cv.waitKey(0)