# -*- coding: utf-8 -*-
# @Time : 2022/11/13 12:02
# @Author : 江晓刚
# @File : histogram.py
# @Software: PyCharm

import cv2
import numpy as np
from matplotlib import pyplot as plt

'''
calcHist 计算图像直方图
函数原型：calcHist(images,channels,mask,histSize,ranges,hist=None,accumulate=None)
images:图像矩阵，例如：[image]
channels:通道数，例如：0
mask:掩膜，一般为：None
histSize:直方图大小，一般等于灰度级数
ranges:横轴范围
'''

# 灰度图像的直方图
img = cv2.imread("../lenna.png", 1)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("image_gray", gray)
# 灰度图像的直方图 方法一
plt.figure()
plt.hist(gray.ravel(), 256)
plt.show()
# 灰度图像的直方图 方法二
hist = cv2.calcHist([gray], [0], None,[256],[0,256])
plt.figure() # 新建一个图像
plt.title("Grayscale Histogram") # 不支持中文
plt.xlabel('Bins') # X轴标签
plt.ylabel("# of Pixels") # Y轴标签
plt.plot(hist)
plt.xlim([0,256]) # 设置X轴坐标范围
plt.show()

# 彩色直方图
cv2.imshow("Original",img)
cv2.waitKey(0)