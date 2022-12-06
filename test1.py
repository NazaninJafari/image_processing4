import cv2
import numpy as np

image = cv2.imread("imgs/flower_input.jpg")
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

mask = np.ones((19,19))/361

output = np.zeros(image.shape)

rows, cols = image.shape

for i in range(9,rows-9):
    for j in range(9,cols-9):
        if image[i,j] < 190:
            small_image = image[i-9:i+10 , j-9:j+10]
            output[i,j] = np.sum(small_image * mask)
        else:
            output[i,j] = image[i,j]    

cv2.imwrite('imgs_result/flower_result.jpg' , output)