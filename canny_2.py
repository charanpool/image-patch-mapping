__author__ = 'skoppuravuri'

import cv2
import numpy as np
from scipy import ndimage

#img = cv2.imread("cropped_input_image.png", 0)
img = cv2.imread("messi.jpg")
#print(img.shape)
height, width = img.shape[0], img.shape[1]

imgdata = np.array(img)

sigma = 1.4

img = cv2.GaussianBlur(imgdata,(5,5), 0)

#performing gradient

kernel_x = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], np.float32)
kernel_y = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], np.float32)

intermediate_x = ndimage.filters.convolve(img, kernel_x)
intermediate_y = ndimage.filters.convolve(img, kernel_y)

gradient_intensity = np.hypot(intermediate_x, intermediate_y)
gradient_intensity = gradient_intensity / gradient_intensity.max() * 255    #Gradient Intensity matrix after appyling sobel filters
gradient_direction = np.arctan2(intermediate_y, intermediate_x)             #Gradient Direction matrix after appyling sobel filters

#non-max supression
Z = np.zeros((height, width), dtype=np.int32)
angle = gradient_direction * 180. / np.pi
angle[angle < 0] += 180

for i in range(1,height-1):
    for j in range(1,width-1):
        try:
            q = 255
            r = 255

           #angle 0
            if (0 <= angle[i,j] < 22.5) or (157.5 <= angle[i,j] <= 180):
                q = img[i, j+1]
                r = img[i, j-1]
            #angle 45
            elif (22.5 <= angle[i,j] < 67.5):
                q = img[i+1, j-1]
                r = img[i-1, j+1]
            #angle 90
            elif (67.5 <= angle[i,j] < 112.5):
                q = img[i+1, j]
                r = img[i-1, j]
            #angle 135
            elif (112.5 <= angle[i,j] < 157.5):
                q = img[i-1, j-1]
                r = img[i+1, j+1]

            if (img[i,j] >= q) and (img[i,j] >= r):
                Z[i,j] = img[i,j]
            else:
                Z[i,j] = 0

        except IndexError as e:
            pass


cv2.imshow("blurred", img)
cv2.imshow("original", imgdata)

cv2.waitKey(0)
cv2.destroyAllWindows()