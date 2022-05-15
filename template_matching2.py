__author__ = 'skoppuravuri'
import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('cropped_input_image.jpg', 1)
print("img_rgb shape:", img_rgb.shape)
print("img_rgb dtype:", img_rgb.dtype)
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
print("img_gray dtype:", img_gray.dtype)
cv2.imshow('img_gray', img_gray)
print("img_gray shape:", img_gray.shape)
#template = cv2.imread('mario_coin.png',0)
template = np.array([[255]*45]*45, np.uint8)
print("template dtype:", template.dtype)
print("template shape :", template.shape)
w, h = template.shape[::-1]

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    method = eval(meth)
    res = cv2.matchTemplate(img_gray,template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(min_val, max_val, min_loc, max_loc)
    threshold = 0.8
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 1)

    cv2.imshow('res.png',img_rgb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
