# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np


def dilation(img, kernel):
    img_dilation = cv2.dilate(img, kernel, iterations=1)
    return img_dilation
