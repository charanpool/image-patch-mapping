__author__ = 'skoppuravuri'

import cv2
import numpy as np

img = cv2.imread('cropped.png')
print(img.shape)

def rotate_clockwise(img, angle):
    rotated = img.copy()
    if angle == 180:

        rotated[:,:,0] = img[::-1,::-1, 0]
        rotated[:,:,1] = img[::-1,::-1, 1]
        rotated[:,:,2] = img[::-1,::-1, 2]

    elif angle == 90:

        rotated[:,:,0] = img[::-1,:, 0]
        rotated[:,:,1] = img[::-1,:, 1]
        rotated[:,:,2] = img[::-1,:, 2]

        rotated[:,:,0] = list(zip(*rotated[:,:,0]))
        rotated[:,:,1] = list(zip(*rotated[:,:,1]))
        rotated[:,:,2] = list(zip(*rotated[:,:,2]))

    elif angle == 270:

        rotated[:,:,0] = img[:, ::-1, 0]
        rotated[:,:,1] = img[:, ::-1, 1]
        rotated[:,:,2] = img[:, ::-1, 2]

        rotated[:,:,0] = list(zip(*rotated[:,:,0]))
        rotated[:,:,1] = list(zip(*rotated[:,:,1]))
        rotated[:,:,2] = list(zip(*rotated[:,:,2]))



    return rotated

final = rotate_clockwise(img, 180)
print(final.shape)
cv2.imshow("final", final)
cv2.imshow("img", img)
cv2.imwrite("rotated.png", final)
cv2.waitKey(0)
cv2.destroyAllWindows()
