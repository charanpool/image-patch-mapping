__author__ = 'skoppuravuri'

import numpy as np
import cv2
import sys

counter = 0

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv2.GaussianBlur(img, (3, 3), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in range(0, 255, 25):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                _retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                if len(cnt) == 4 and cv2.contourArea(cnt) > 1000 and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in range(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

if __name__ == '__main__':
    from glob import glob
    for fn in glob("cropped_input_image.jpg"):
        img = cv2.imread(fn)
        squares = find_squares(img)
        print(squares)
        cv2.drawContours( img, squares, -1, (0, 0, 255), 1 )
        cv2.imshow('squares', img)
        ch = cv2.waitKey()
        if ch == 27:
            break
        print (len(squares))
    cv2.destroyAllWindows()
