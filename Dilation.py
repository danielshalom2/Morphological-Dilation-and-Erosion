# Python program to demonstrate erosion and
# dilation of images.
import cv2
import numpy as np


def idx_check(index):
    if index < 0:
        return 0
    else:
        return index


# # def idx_check(kernel, mask):
# #     for i in range(mask.shape[0]):
# #         for j in range(mask.shape[1]):
# #             if mask[i][j] == 2:
# #                 continue
# #             elif kernel[i][j] != mask[i][j]:
# #                 return False
# #     return True
#
#
# def dilation(img, mask):
#     imgShape = img.shape
#     # print(imgShape)
#     # resultImg = np.zeros((imgShape[0], imgShape[1]))
#     # print(resultImg)
#     maskShape = mask.shape
#     # print(maskShape)
#     # kernel = np.zeros((maskShape[0], maskShape[1]))
#     # print(kernel)
#     # img = img / 255 #binary image
#     # print(img)
#     R = imgShape[0] + maskShape[0] - 1
#     C = imgShape[1] + maskShape[1] - 1
#     N = np.zeros((R, C))
#
#     ######## padding the image #######
#     for i in range(imgShape[0]):
#         for j in range(imgShape[1]):
#             N[i + 1, j + 1] = img[i, j]
#             # N[i + np.int((maskShape[0] - 1) / 2), j + np.int((maskShape[1] - 1) / 2)] = img[i, j]
#             # print(N[i + np.int((maskShape[0] - 1) / 2), j + np.int((maskShape[1] - 1) / 2)])
#
#     for i in range(imgShape[0]):
#         for j in range(imgShape[1]):
#             kernel = N[i:i + maskShape[0], j:j + maskShape[1]]
#             result = (kernel == mask)
#             final = np.any(result == True)
#             if final:
#                 img[i, j] = 1
#             else:
#                 img[i, j] = 0
#
#             # result = idx_check(kernel, mask)
#             # if result:
#             #     resultImg[i, j] = 1
#
#     return img

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
