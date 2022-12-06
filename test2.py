import cv2
import numpy as np

image = cv2.imread("imgs/lion.png")
image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

result = np.zeros(image.shape)

# 3*3
mask = np.array([[0, -1, 0],
                 [-1, 4, -1],
                 [0, -1, 0]])

rows, cols = image.shape

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_image = image[i-1:i+2 , j-1:j+2]
        result[i,j] = np.sum(small_image * mask)

cv2.imshow("output", result)
cv2.imwrite("imgs_result/lion_output.png", result)
cv2.waitKey()
