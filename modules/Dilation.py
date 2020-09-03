# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np


def dilation(img, mask):
    imgshape = img.shape
    maskshape = mask.shape
    dilate_img = np.zeros((imgshape[0], imgshape[1]))
    pad_img = np.zeros((imgshape[0] + maskshape[0] - 1, imgshape[1] + maskshape[1] - 1))
    for i in range(imgshape[0]):
        for j in range(imgshape[1]):
            pad_img[i + np.int((maskshape[0] - 1) / 2), j + np.int((maskshape[1] - 1) / 2)] = img[i, j]

    for i in range(imgshape[0]):
        for j in range(imgshape[1]):
            kernel = pad_img[i:i + maskshape[0], j:j + maskshape[1]]
            result = (kernel == mask)
           # print(kernel)
            final = np.any(result == True)
            if final:
                dilate_img[i, j] = 1
            else:
                dilate_img[i, j] = 0
    return dilate_img
