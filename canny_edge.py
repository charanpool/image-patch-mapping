__author__ = 'skoppuravuri'

import numpy as np
import cv2
#cv2.Sobel(original_image,ddepth,xorder,yorder,kernelsize)

img = cv2.imread("res.jpg", cv2.IMREAD_UNCHANGED)
#print("input_image shape = ", img.shape)
#cv2.imwrite("cropped_input_image.jpg", img)
#img = cv2.imread("cropped_input_image.jpg", 1)

#img = cv2.blur(img, (5,5))
#print("img shape :", img.shape)
#cv2.imshow("blurred", img)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([30,150,50])
upper_red = np.array([255,255,180])

mask = cv2.inRange(hsv, lower_red, upper_red)
res = cv2.bitwise_and(img,img, mask= mask)

cv2.imshow('Original',img)
edges = cv2.Canny(img,100,200)
cv2.imshow('Edges',edges)

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