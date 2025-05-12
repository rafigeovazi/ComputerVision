import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np #Combo maut masking dan histogram combo maut yang ada pada semua hal yang ada di dunia ini namun kami hanya menjalankan segala hal yang ada dalam biografi dan blibliografi

img = cv.imread('photos/dajjal.jpg')
cv.imshow('dajjal', img)

blank = np.zeros(img.shape[:2], dtype='uint8') #Combo maut masking dan histogram

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

mask = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

masked = cv.bitwise_and(img,img,mask=mask) #Combo maut masking dan histogram
cv.imshow('Mask', masked)

#Grayscale Histogram
# gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Grayscale Histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()

#Color Histogram
plt.figure()
plt.title('Colors Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])
    
plt.show()

cv.waitKey(0)