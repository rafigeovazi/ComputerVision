import cv2
import numpy as np

farm_img = cv2.imread('photos/farm.png', cv2.IMREAD_UNCHANGED)
wheat_img = cv2.imread('photos/needle.png', cv2.IMREAD_UNCHANGED)

result = cv2.matchTemplate(farm_img, wheat_img, cv2.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

w = wheat_img.shape[1]
h = wheat_img.shape[0]

cv2.rectangle(farm_img, max_loc, (max_loc[0] + w, max_loc[1] + h), (0,0,255), 2)

threshold = .60
yloc, xloc = np.where(result >= threshold)

for (x, y) in zip(xloc, yloc):
    cv2.rectangle(farm_img, (x, y), (x + w, y + h), (0,0,255), 2)

cv2.imshow('Result', farm_img)
cv2.waitKey(0)
cv2.destroyAllWindows()