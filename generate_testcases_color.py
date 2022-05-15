__author__ = 'skoppuravuri'

import cv2
import numpy as np
import random

ipimg = cv2.imread("messi.jpg", 1)
no_of_patches = 4
patch_size = 50
grey_color = 255

res = np.array([[[grey_color] * 3]*patch_size]*(no_of_patches * patch_size), np.uint8)

print(len(ipimg.shape)) #RowsxColumns

x_coord = []
y_coord = []

for i in range(0, no_of_patches):
    flag = 0
    y_rand = random.randint(0, 400)#ipimg.shape[0]-patch_size)
    x_rand = random.randint(0, 200)#ipimg.shape[1]-patch_size)
    print("(x, y) = ", x_rand, y_rand)

    x_coord.append(x_rand)
    y_coord.append(y_rand)
    for row in range(0, patch_size):
        for col in range(0, patch_size):
            res[col+(i*patch_size)][row][0] = ipimg[col+x_rand][row+y_rand][0]
            ipimg[col+x_rand][row+y_rand][0] = 0
            res[col+(i*patch_size)][row][1] = ipimg[col+x_rand][row+y_rand][1]
            ipimg[col+x_rand][row+y_rand][1] = 128
            res[col+(i*patch_size)][row][2] = ipimg[col+x_rand][row+y_rand][2]
            ipimg[col+x_rand][row+y_rand][2] = 255


cv2.imshow("res", res)
cv2.imshow("cropped", ipimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("coloured_patches\\res.png", res)
cv2.imwrite("coloured_patches\\cropped.png", ipimg)

