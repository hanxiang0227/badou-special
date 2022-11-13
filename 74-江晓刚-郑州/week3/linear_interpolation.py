# -*- coding: utf-8 -*-
# @Time : 2022/11/12 7:03
# @Author : 江晓刚
# @File : linear_interpolation.py
# @Software: PyCharm

import numpy as np
import cv2

"""
实现双线性插值
"""


def linear_interpolation(img, out_dim):
    src_h, src_w, channel = img.shape  # 映射原图像坐标
    dst_h, dst_w = out_dim[1], out_dim[0]
    print("src_h, src_w =", src_h, src_w)
    print("dst_h,dst_w =", dst_h, dst_w)

    if src_h == dst_h and src_w == dst_w:
        return img.copy()  # 复制一个新的图像

    dst_img = np.zeros((dst_h, dst_w, 3), dtype=np.uint8)  # 将变量dst_img初始化为三维矩阵
    scale_x, scale_y = float(src_w) / dst_w, float(src_h) / dst_h

    for i in range(3):  # 设定为 3通道
        for dst_y in range(dst_h):  # 遍历图像中的每个像素点
            for dst_x in range(dst_w):
                # 1、按比例对应P点原图坐标，
                # 2、解决坐标系选择的问题，让两个图像的几何中心重合，并且都和两边有边距。
                src_x = (dst_x + 0.5) * scale_x - 0.5
                src_y = (dst_y + 0.5) * scale_y - 0.5

                # 找出邻居的 4 个像素点用于计算像素点的坐标
                src_x0 = int(np.floor(src_x))
                src_x1 = min(src_x0 + 1, src_w - 1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h - 1)

                # 计算差值
                temp0 = (src_x1 - src_x) * img[src_y0, src_x0, i] + (src_x - src_x0) * img[src_y0, src_x1, i]
                temp1 = (src_x1 - src_x) * img[src_y1, src_x0, i] + (src_x - src_x0) * img[src_y1, src_x1, i]
                dst_img[dst_y, dst_x, i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)

    return dst_img


if __name__ == '__main__':
    img = cv2.imread("../lenna.png")
    dst = linear_interpolation(img, (800, 800))
    cv2.imshow('linear_interpolation', dst)
    cv2.waitKey(0)
