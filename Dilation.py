# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

def idx_check(kernel, mask):
    for i in range(mask.shape[0] - 1):
        for j in range(mask.shape[1] - 1):
            if int(kernel[i][j]) == mask[i][j]:
                return True
    return False


def dilation(img, mask):
    imgShape = img.shape
    img_dilation = np.zeros((imgShape[0], imgShape[1]))
    maskShape = mask.shape
    kernel = np.zeros((maskShape[0], maskShape[1]))
    img = img / 255
    N = np.zeros((imgShape[0] + maskShape[0] - 1, imgShape[1] + maskShape[1] - 1))

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            N[i + np.int((maskShape[0] - 1) / 2), j + np.int((maskShape[1] - 1) / 2)] = img[i, j]

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            kernel = N[i:i + maskShape[0] - 1, j: j + maskShape[1] - 1]
            result = idx_check(kernel, mask)
            if np.all(result == True):
                img_dilation[i, j] = 1

    return img_dilation
