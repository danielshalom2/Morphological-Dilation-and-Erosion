# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np


def erosion(img, mask):
    # img_erosion = cv2.erode(img, kernel, iterations=1)
    imgShape = img.shape
    resultImg = np.zeros((imgShape[0], imgShape[1]))
    maskShape = mask.shape
    kernel = np.zeros((maskShape[0], maskShape[1]))
    img = img / 255
    N = np.zeros((imgShape[0] + maskShape[0] - 1, imgShape[1] + maskShape[1] - 1))

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            N[[i + np.int((maskShape[0] - 1) / 2), j + np.int((maskShape[1] - 1) / 2)]] = img[i, j]

    for i in range(imgShape[0]):
        for j in range(imgShape[1]):
            kernel = np.copy(N[i:i + maskShape[0], j:j + maskShape[1]])
            result = (kernel == mask)
            if np.all(result == True):
                resultImg[i, j] = 1

    return np.uint8(resultImg)
