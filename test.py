__author__ = 'skoppuravuri'

import numpy as np
import cv2

input_image = cv2.imread("mandril_color.tif", cv2.IMREAD_UNCHANGED)
print("input_image shape = ", input_image.shape)

cv2.imwrite("cropped_input_image.jpg", input_image)
input_image = cv2.imread("cropped_input_image.jpg", 1)
print("input_image shape = ", input_image.shape)

coordinates_list = []
temp_flag = 0
x, y = (0, 0)
#selects i and j
for i in range(0, input_image.shape[0] - 50):
    for j in range(0, input_image.shape[1] - 50):
        #iterates through template(white) from there
        for x in range(0, 51):
            for y in range(0, 51):
                #print(input_image[i + x, j + y])
                if ((input_image[i + x, j + y][0] == 255) and (input_image[i + x, j + y][1] == 255) and (input_image[i + x, j + y][2] == 255)) == False:
                    temp_flag = 1
                    break
        if temp_flag == 1:
            temp_flag = 0
            continue
        else:
            coordinates_list.append((i, j))

print(coordinates_list)

#showing and closing all the windows
cv2.imshow("Over the Clouds", input_image)
#cv2.imshow("Over the Clouds Grey", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
