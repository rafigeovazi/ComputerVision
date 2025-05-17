import cv2 as cv
import numpy as np

img = cv.imread('photos/dajjal.jpg')
cv.imshow('Dajjal', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank Image', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30,30),(370,370), 255, -1)

and_shape = cv.bitwise_and(circle, rectangle)
cv.imshow('AND Mask', and_shape)

masked = cv.bitwise_and(img, img, mask=and_shape)
cv.imshow('AND Masked Image', masked)

cv.waitKey(0)