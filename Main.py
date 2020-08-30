from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    img = cv2.imread('circles.jpeg')
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (thresh, binarImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)  # 1D array
    mask = np.ones((12, 12), np.uint8)
    #mask = np.array([[1, 1, 1],
                     # [1, 1, 1],
                     # [1, 1, 1]
                     # ])
    binarImg = binarImg / 255
    img_erosion = erosion(binarImg, mask)
    img_dilation = dilation(binarImg, mask)
    plt.figure('Input')
    plt.subplot(131)
    plt.imshow(grayImg, 'gray')
    plt.subplot(132)
    plt.imshow(img_erosion, 'gray')
    plt.subplot(133)
    plt.imshow(img_dilation, 'gray')
    plt.show()


if __name__ == '__main__':
    main()
