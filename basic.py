import cv2 as cv

img = cv.imread('photos/niggers.jpg')

cv.imshow('HappyFamily', img)

#Converting to grayscale or another color
# rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('RGB Duajjalz', rgb)

#Blur 
# blur = cv.GaussianBlur(img, (5,5), cv.BORDER_DEFAULT)
# cv.imshow('Blur Duajjalz', blur)

#Edge Cascade
# edges = cv.Canny(img, 100, 100)
# cv.imshow('Canny Edges Duajjalz', edges) 

#Dilating the Edges
# dilated = cv.dilate(edges, (9,9), iterations=3)
# cv.imshow('Dilated Duajjalz', dilated)

#Eroding the Edges
# eroded = cv.erode(dilated, (9,9), iterations=3)
# cv.imshow('Eroded Duajjalz', eroded)

#Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized Duajjalz', resized)
#Crop
cropped = img[50:200, 200:400]
cv.imshow('Cropped Duajjalz', cropped)

cv.waitKey(0)
