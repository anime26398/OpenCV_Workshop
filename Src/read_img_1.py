import cv2
import numpy as np
from matplotlib import pyplot as plt
#IMREAD_GRAYSCALE
#IMREAD_COLOR
#IMREAD_UNCHANGED
img = cv2.imread('/home/aniruddha/Documents/Aries/Workshops/Workshop1_Image_Processing/Data/lenna.jpg',cv2.IMREAD_GRAYSCALE)
print(img.shape)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
