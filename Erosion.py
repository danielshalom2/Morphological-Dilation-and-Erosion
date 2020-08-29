# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np


def idx_check(kernel, mask):
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i][j] == 2:
                continue
            elif kernel[i][j] != mask[i][j]:
                return False
    return True


def erosion(img, mask):
    imgShape = img.shape
    resultImg = np.zeros((imgShape[0], imgShape[1]))
    maskShape = mask.shape
    kernel = np.zeros((maskShape[0], maskShape[1]))
    img = img / 255
    N = np.zeros((imgShape[0] + maskShape[0] - 1, imgShape[1] + maskShape[1] - 1))

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            N[i + np.int((maskShape[0] - 1) / 2), j + np.int((maskShape[1] - 1) / 2)] = img[i, j]

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            kernel = N[i:i + maskShape[0], j: j + maskShape[1]]
            result = idx_check(kernel, mask)
            if result:
                resultImg[i, j] = 1

    return resultImg
