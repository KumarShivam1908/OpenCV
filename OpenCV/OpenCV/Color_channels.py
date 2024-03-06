import  cv2 as cv
import numpy as np

img=cv.imread('Photos/park.jpg')
cv.imshow('Actual',img)

blank=np.zeros(img.shape[:2],'uint8')

b,g,r=cv.split(img)

blue=cv.merge([b,blank,blank])
green=cv.merge([blank,g,blank])
red=cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('Red',red)
cv.imshow('Green',green)


# cv.imshow('Blue',b)
# cv.imshow('Green',g)
# cv.imshow('Red',r)

print(f"{img.shape} is the actual image shape")
print(f"{b.shape} is the b image shape")
print(f"{g.shape} is the g image shape")
print(f"{r.shape} is the r image shape")

# merge_image=cv.merge([b,g,r])
# cv.imshow('Merged Image',merge_image)

# print(f"{merge_image.shape}is the shape of the merged image")
cv.waitKey(0)