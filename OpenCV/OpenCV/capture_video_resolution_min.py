import cv2 as cv

# Function to change the resolution of the video capture
def changereso(capture, width, height):
    capture.set(3, width)  # Set width
    capture.set(4, height) # Set height

# Capture video from webcam (0)
capture = cv.VideoCapture(0)

# Change resolution (e.g., to 640x480)
changereso(capture, 640, 480)

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
