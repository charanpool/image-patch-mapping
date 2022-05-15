__author__ = 'skoppuravuri'

import numpy as np
import cv2
#cv2.Sobel(original_image,ddepth,xorder,yorder,kernelsize)

img = cv2.imread("cropped_input_image.png", cv2.IMREAD_UNCHANGED)
print("input_image shape = ", img.shape)
cv2.imwrite("cropped_input_image.jpg", img)
img = cv2.imread("cropped_input_image.jpg", 1)

#hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

#laplacian = cv2.Laplacian(img, cv2.CV_64F)

sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

laplacian = cv2.Laplacian(img, cv2.CV_64F)

#print("sobelx :\n", sobelx)
#print('-----')
#print("sobely :\n", sobely)

cv2.imshow("sobelx", sobelx)
cv2.imshow("sobely", sobely)
cv2.imshow("laplacian", laplacian)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()



'''
def sobel(A):      #A is two dimensional image array
	Gx=[[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
	Gy=[[-1, -2, -1][0, 0, 0], [1, 2, 1]]

	rows = len(A)#size(A,1)
	columns = len(A[0])#size(A,2)
	mag=np.zeros((rows, columns))

	for i in range(1, rows-1):#i=1:rows-2
		for j in range(1, columns-1):#j=1:columns-2
			S1=sum(sum(Gx.*A[i:i+2][j:j+2]))
			S2=sum(sum(Gy.*A(i:i+2,j:j+2)))

			mag(i+1,j+1)=sqrt(S1.^2+S2.^2)
		end for
	end for

	threshold = 70 %varies for application [0 255]
	output_image = max(mag,threshold)
	output_image(output_image==round(threshold))=0;
	return output_image
end function
'''