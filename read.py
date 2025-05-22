import cv2 as cv

#Reading photos
img = cv.imread('photos/zilit2.png')

cv.imshow('zilit', img)
cv.waitKey(0)  

#Reading videos
capture = cv.VideoCapture('Videos/blew.mp4')

while True:
    isTrue, frame = capture.read()
    
    cv.imshow('Video', frame)
    
    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()