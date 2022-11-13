# -*- coding: utf-8 -*-
# @Time : 2022/11/13 17:45
# @Author : 江晓刚
# @File : nearest interp.py.py
# @Software: PyCharm

import cv2
import numpy as np


def function(img):
    h, w, channels = img.shape
    empty_image = np.zeros((800, 800, channels), np.uint8)
    sh = 800 / h
    sw = 800 / w
    for i in range(800):
        for j in range(800):
            x = int(i / sh + 0.5)
            y = int(j / sw + 0.5)
            empty_image[i, j] = img[x, y]
    return empty_image


img = cv2.imread("../lenna.png")
zoom = function(img)
print(zoom)
print(zoom.shape)
cv2.imshow("nearest interp", zoom)
cv2.imshow("image", img)
cv2.waitKey(0)
