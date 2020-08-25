import numpy as np
import cv2
from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    # Reading the input image`
    img = cv2.imread('fingerprint_1.png', 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((3, 3), np.uint8)
    img_erosion = erosion(img, kernel)
    img_dilation = dilation(img, kernel)
    plt.figure('Input')
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.subplot(132)
    plt.imshow(cv2.cvtColor(img_erosion, cv2.COLOR_BGR2RGB))
    plt.subplot(133)
    plt.imshow(cv2.cvtColor(img_dilation, cv2.COLOR_BGR2RGB))
    plt.show()

#    cv2.imshow('Input', img)
#    cv2.imshow('Erosion', img_erosion)
#    cv2.imshow('Dilation', img_dilation)

#    cv2.waitKey(0)


if __name__ == '__main__':
    main()
