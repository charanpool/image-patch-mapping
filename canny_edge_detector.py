import numpy as np
import cv2
import scipy.ndimage as ndi

sigma = 1.4

input_image = cv2.imread('cropped_16.png', 0)      #reading the image
image_data = np.array(input_image, dtype = float)
gaussian_out = ndi.filters.gaussian_filter(image_data, sigma)   #applying gaussian filter to blur which reduces the noise in image

gradient_x = np.array(image_data, dtype = float)        #creating temparory arrays by duplicating for calculating gradients
gradient_y = np.array(image_data, dtype = float)

sobel_x_filter = [[-1,0,1], [-2,0,2], [-1,0,1]]         #predefined sobel X and Y filters
sobel_y_filter = [[-1,-2,-1], [0,0,0], [1,2,1]]

width = image_data.shape[0]
height = image_data.shape[1]

for x in range(1, width-1):             #getting sobel magnitude output in both X and Y directioins
    for y in range(1, height-1):
        result_x = (sobel_x_filter[0][0] * gaussian_out[x-1][y-1]) + (sobel_x_filter[0][1] * gaussian_out[x][y-1]) + \
             (sobel_x_filter[0][2] * gaussian_out[x+1][y-1]) + (sobel_x_filter[1][0] * gaussian_out[x-1][y]) + \
             (sobel_x_filter[1][1] * gaussian_out[x][y]) + (sobel_x_filter[1][2] * gaussian_out[x+1][y]) + \
             (sobel_x_filter[2][0] * gaussian_out[x-1][y+1]) + (sobel_x_filter[2][1] * gaussian_out[x][y+1]) + \
             (sobel_x_filter[2][2] * gaussian_out[x+1][y+1])

        result_y = (sobel_y_filter[0][0] * gaussian_out[x-1][y-1]) + (sobel_y_filter[0][1] * gaussian_out[x][y-1]) + \
             (sobel_y_filter[0][2] * gaussian_out[x+1][y-1]) + (sobel_y_filter[1][0] * gaussian_out[x-1][y]) + \
             (sobel_y_filter[1][1] * gaussian_out[x][y]) + (sobel_y_filter[1][2] * gaussian_out[x+1][y]) + \
             (sobel_y_filter[2][0] * gaussian_out[x-1][y+1]) + (sobel_y_filter[2][1] * gaussian_out[x][y+1]) + \
             (sobel_y_filter[2][2] * gaussian_out[x+1][y+1])
        gradient_x[x][y] = result_x
        gradient_y[x][y] = result_y

sobel_out_magnitude = np.hypot(gradient_x, gradient_y)
sobel_out_direction = np.arctan2(gradient_y, gradient_x)

for x in range(width):                          #getting sobel direction output
    for y in range(height):
        if (sobel_out_direction[x][y]<22.5 and sobel_out_direction[x][y]>=0) or \
           (sobel_out_direction[x][y]>=157.5 and sobel_out_direction[x][y]<202.5) or \
           (sobel_out_direction[x][y]>=337.5 and sobel_out_direction[x][y]<=360):
            sobel_out_direction[x][y]=0
        elif (sobel_out_direction[x][y]>=22.5 and sobel_out_direction[x][y]<67.5) or \
             (sobel_out_direction[x][y]>=202.5 and sobel_out_direction[x][y]<247.5):
            sobel_out_direction[x][y]=45
        elif (sobel_out_direction[x][y]>=67.5 and sobel_out_direction[x][y]<112.5)or \
             (sobel_out_direction[x][y]>=247.5 and sobel_out_direction[x][y]<292.5):
            sobel_out_direction[x][y]=90
        else:
            sobel_out_direction[x][y]=135

maximum_suppression = sobel_out_magnitude.copy()

for x in range(1, width-1):                 #non_max_supressing the sobel output
    for y in range(1, height-1):
        if sobel_out_direction[x][y]==0:
            if (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x][y+1]) or (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x][y-1]):
                maximum_suppression[x][y]=0
        elif sobel_out_direction[x][y]==45:
            if (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x-1][y+1]) or (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x+1][y-1]):
                maximum_suppression[x][y]=0
        elif sobel_out_direction[x][y]==90:
            if (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x+1][y]) or (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x-1][y]):
                maximum_suppression[x][y]=0
        else:
            if (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x+1][y+1]) or (sobel_out_magnitude[x][y]<=sobel_out_magnitude[x-1][y-1]):
                maximum_suppression[x][y]=0

max_val = np.max(maximum_suppression)       #assigning max and min threshold values
thresold_high = 0.2*max_val
thresold_low = 0.1*max_val

generated_high = np.zeros((width, height))  #dummying arrays for getting sizes
generated_low = np.zeros((width, height))

for x in range(width):                      #non_max_suppression of obtained matrix values
    for y in range(height):
        if maximum_suppression[x][y]>=thresold_high:
            generated_high[x][y]=maximum_suppression[x][y]
        if maximum_suppression[x][y]>=thresold_low:
            generated_low[x][y]=maximum_suppression[x][y]

generated_low = generated_low-generated_high

for i in range(1, width-1):                 #accomodating generated_low in generating_high which makes total output in generated_high
    for j in range(1, height-1):
        #if generated_high[i][j]:
            #generated_high[i][j]=1
        if generated_low[i][j]:
            generated_high[i][j] = 1

cv2.imshow("edge_detected", generated_high)     #displaying the original and edge detected outputs
#cv2.imshow("gen2", generated_low)
cv2.imshow("orginal", input_image)
cv2.waitKey(0)
cv2.destroyAllWindows()