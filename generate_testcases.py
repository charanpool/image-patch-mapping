__author__ = 'skoppuravuri'

import cv2
import numpy as np
import random

ipimg = cv2.imread("messi.jpg", 0)
no_of_patches = 6
patch_size = 40
grey_color = 255

res = np.array([[grey_color]*patch_size]*(no_of_patches * patch_size), np.uint8)

#print(ipimg.shape) #RowsxColumns

x_coord = []
y_coord = []

for i in range(0, no_of_patches):
    flag = 0
    y_rand = random.randint(0, 240)#ipimg.shape[0]-patch_size)
    x_rand = random.randint(0, 240)#ipimg.shape[1]-patch_size)
    print("(x, y) = ", x_rand, y_rand)
    '''
    for xval in x_coord:
        if x_rand in list(range(xval-patch_size, xval+patch_size+1)):
            flag = 1
            break
    if(flag == 1):
        no_of_patches += 1
        continue
    for yval in y_coord:
        if y_rand in list(range(yval-patch_size, yval+patch_size+1)):
            flag = 1
            break
    if(flag == 1):
        no_of_patches += 1
        continue
    '''
    x_coord.append(x_rand)
    y_coord.append(y_rand)
    for row in range(0, patch_size):
        for col in range(0, patch_size):
            res[col+(i*patch_size)][row] = ipimg[col+x_rand][row+y_rand]
            ipimg[col+x_rand][row+y_rand] = 120

#res = cv2.cvtColor(res,cv2.COLOR_GRAY2BGR)
#ipimg = cv2.cvtColor(ipimg,cv2.COLOR_GRAY2BGR)

#cv2.cvtColor(ipimg, ipimg, cv2.COLOR_GRAY2BGR)
#cv2.cvtColor(res, res, cv2.COLOR_GRAY2BGR)

cv2.imshow("res", res)
cv2.imshow("cropped", ipimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


cv2.imwrite("res.jpg", res)
cv2.imwrite("cropped.jpg", ipimg)

