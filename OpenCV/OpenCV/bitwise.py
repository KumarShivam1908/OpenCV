import cv2 as cv
import numpy as np

blank=np.zeros((400,400),'uint8')
cv.imshow('blank',blank)

rectangle=cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle=cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise And (intersecting)
bit_wise_and=cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise and',bit_wise_and)

#bitwise or (both non intersecting and intersecting)
bitwise_or=cv.bitwise_or(rectangle,circle)
cv.imshow('bitwise_or',bitwise_or)

#bitwise_xor (non intersectiong region)
bitwise_xor=cv.bitwise_xor(circle,rectangle)
cv.imshow('bitwise xor',bitwise_xor)

#bitwise not

bitwise_not=cv.bitwise_not(rectangle)
cv.imshow('rectangle not',bitwise_not)

cv.waitKey(0)