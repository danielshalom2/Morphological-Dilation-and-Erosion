import numpy as np
import cv2
from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    # Reading the input image
    img = cv2.imread('fingerprint2.jpg', 0)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((2, 2), np.uint8)
    img_erosion = erosion(img, kernel)
    img_dilation = dilation(img, kernel)

    cv2.imshow('Input', img)
    cv2.imshow('Erosion', img_erosion)
    cv2.imshow('Dilation', img_dilation)

    cv2.waitKey(0)


if __name__ == '__main__':
    main()
