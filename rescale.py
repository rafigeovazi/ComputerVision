import cv2 as cv

#Reading photos
img = cv.imread('photos/zilit.png')

cv.imshow('zilit', img)

def rescaleFrame(frame, scale=0.75):
    #Can use this for Images, Videos and live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height) 
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)
resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

def changeRes(width,height):
    #Only can use for Live Video
    capture.set(3,width)
    capture.set(4,height)

#Reading videos
capture = cv.VideoCapture('Videos/blew.mp4')

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame)
    
    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows() 