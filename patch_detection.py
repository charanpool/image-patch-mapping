__author__ = 'skoppuravuri'

import cv2
import numpy as np
import itertools

def validateRectangularFrame(image, i, j, patch_size):
    rectFrame = []
    '''
    if(i != 0):
        rectFrame.append(image[i-1][(j-1):(j+patch_size+2)])
        #rectFrame = list(itertools.chain(*rectFrame))
    if(j != 0):
        #rectFrame.append(image[i-1][(j-1):(j+patch_size+1)])
        for p in range(0, patch_size+2):
            rectFrame.append(image[i-1][p])
    rectFrame.append(image[i+patch_size+1][(j-1):(j+patch_size+2)])
    #rectFrame = list(itertools.chain(*rectFrame))
    for p in range(0, patch_size+2):
        rectFrame.append(image[i+patch_size+1][p])
    if(np.min(rectFrame) == np.max(rectFrame)):
        return False
    else:
        return True
    '''
    if((i == 0) and (j == 0)):
        for k in range(0, patch_size):
            rectFrame.append(image[k][j+patch_size])
        for k in range(0, patch_size):
            rectFrame.append(image[i+patch_size][k])
        rectFrame.append(image[i+patch_size][j+patch_size])
    elif(i == 0):
        for k in range(0, patch_size):
            rectFrame.append(image[k][j-1])
        for k in range(0, patch_size):
            rectFrame.append(image[k][j+patch_size])
        for k in range(0, patch_size):
            rectFrame.append(image[i+patch_size][k+j])
        rectFrame.append(image[i+patch_size][j-1])
        rectFrame.append(image[i+patch_size][j+patch_size])
    elif(j == 0):
        for k in range(0, patch_size):
            rectFrame.append(image[i-1][k])
        for k in range(0, patch_size):
            rectFrame.append(image[i+patch_size][patch_size])
        for k in range(0, patch_size):
            rectFrame.append(image[k][j+patch_size])



img = cv2.imread('cropped_16.png', 0)
#print(img.shape)
img_height, img_width = img.shape
patch_size = 50

#temp = np.zeros(patch_size, patch_size)
temp = [[0] * patch_size] * patch_size
#print(temp)

c_list = []

for i in range(0, img_height - patch_size):
    for j in range(0, img_width - patch_size):
        #temp = np.array(img[(i * patch_size): ((i * patch_size) + patch_size)][0:patch_size])
        #create sub array
        for k in range(patch_size):
            temp[k] = img[i][j:(j+patch_size)]
        if(np.min(temp) == np.max(temp)):
            #all the 2D array is having same values
            print((i, j))
            if(validateRectangularFrame(img, i, j, patch_size)):
                c_list.append((i, j))
        else:
            pass
print(c_list)