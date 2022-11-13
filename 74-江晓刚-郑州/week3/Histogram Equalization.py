# -*- coding: utf-8 -*-
# @Time : 2022/11/12 21:47
# @Author : 江晓刚
# @File : Histogram Equalization.py
# @Software: PyCharm

import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
实现直方图均衡化
函数原型：equalizeHist(src, dst=None)
src:图像矩阵（单通道图像）
dst: 默认即可
"""

# 获取灰度图像
img = cv2.imread("../lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 把BRG转换为RPG格式
cv2.imshow("image_gray", gray)

# 灰度图像均衡化
dst = cv2.equalizeHist(gray)

# 直方图
hist = cv2.calcHist([dst], [0], None, [256], [0, 256])
plt.figure()
plt.hist(dst.ravel(), 256)
plt.show()
cv2.imshow('Histogram Equalization', np.hstack([gray, dst]))
cv2.waitKey(0)
