import numpy as np
import cv2
from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    # Reading the input image
    img = cv2.imread('input.png', 0)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    img_erosion = Erosion(img,kernel)
    img_dilation = Dilation(img, kernel)

    cv2.imshow('Input', img)
    cv2.imshow('Erosion', img_erosion)
    cv2.imshow('Dilation', img_dilation)

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
