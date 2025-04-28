import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('photos/zilit.png')
cv.imshow('Zilit', img)

#combo ama matplotlib dari BGR ke RGB, dan bisa di edit
# plt.imshow(img)
# plt.show()

#BGR 2 Gray
gray = cv. cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

#BGR 2 HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

#BGR 2 LAB/L*A*B
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

#BGR 2 RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
#combo ama matplotlib
plt.imshow(rgb)
plt.show()

cv.waitKey(0)