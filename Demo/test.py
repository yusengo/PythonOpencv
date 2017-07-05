import cv2
import numpy as np

i = 0
img = cv2.imread("E:\\CV\\testcv\\pic.jpg")
i += 1
cv2.imshow("lena",img)
i += 1
cv2.waitKey(1000)