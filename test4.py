import cv2
import numpy as np


def function(k):
    for i in range(k ,rows-k):
        for j in range(k ,cols-k):
            if k == 1:
                small_img = image[i-1:i+2 , j-1:j+2]
                result[i,j] = np.sum(small_img * mask_model1)
            elif k == 2:
                small_img = image[i-2:i+3 , j-2:j+3]
                result[i,j] = np.sum(small_img * mask_model2)
            elif k == 3:
                small_img = image[i-3:i+4 , j-3:j+4]
                result[i,j] = np.sum(small_img * mask_model3)
            elif k == 7:
                small_img = image[i-7:i+8 , j-7:j+8]
                result[i,j] = np.sum(small_img * mask_model4)
                    
    return result

image = cv2.imread('imgs/coucher_le_soleil.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

result = np.zeros(image.shape)

mask_model1 = np.ones((3,3)) /9
mask_model2 = np.ones((5,5)) /25
mask_model3 = np.ones((7,7)) /49
mask_model4 = np.ones((15,15)) /225

rows , cols = image.shape

k = int(input('k=1 : 3*3\nk=2 : 5*5\nk=3 : 7*7\nk=7 : 15*15\n please inter k = '))

output = function(k)
cv2.imwrite('imgs_result/output_img'+str(k)+'.jpg', output)