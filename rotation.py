__author__ = 'skoppuravuri'


import cv2
import numpy as np
import imutils
from skimage.measure import compare_ssim

img = cv2.imread('cropped_16.png')
#img2 = cv2.imread('mandril_color - Copy.tif')

def rotate_clockwise(img, angle):
    #rotated =  imutils.rotate_bound(img, angle)
    M = cv2.getRotationMatrix2D((img.shape[0]/2,img.shape[1]/2),90,1)
    rotated = cv2.warpAffine(img, M, (int(img.shape[0]),int(img.shape[1])))
    #cv2.imshow("rotated", rotated)
    #cv2.waitKey(0)
    #cv2.imwrite("rotated.jpg", rotated)
    return rotated


final = np.array(rotate_clockwise(img, 90), np.uint8)
cv2.imshow("final", final)
cv2.imwrite("rotated.png", final)#, [int(cv2.IMWRITE_JPEG_QUALITY), 0])
#print(cv2.ssim(img, final))
#(score, diff) = compare_ssim(img, final, full=True, multichannel=True)
#print((score, diff) )
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
