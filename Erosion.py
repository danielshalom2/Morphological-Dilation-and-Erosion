# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np

def Erosion(img,kernel):
    img_erosion = cv2.erode(img, kernel, iterations=1)
    return img_erosion


