#Rescaling a video is modifiying its height and width to a particlar height or width.
import cv2 as cv

def changereso(capture, width, height):
    capture.set(3, width)  # Set width
    capture.set(4, height) # Set height

capture=cv.VideoCapture(0)
changereso(capture, 640, 480)



def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)

    dimensions = (width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

# #Resize images
# img = cv.imread('Photos/cat_large.jpg')
# resize_img=rescaleFrame(img,scale=0.2)
# cv.imshow('Cat',resize_img)
# cv.waitKey(0)

#Resize videos
while True:
    # Read a frame from the video capture
    isTrue, frame = capture.read()

    # Display the frame
    cv.imshow('Video', frame)

    # Break the loop if 'd' key is pressed
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

# Release the video capture object
capture.release()

cv.waitKey(0)