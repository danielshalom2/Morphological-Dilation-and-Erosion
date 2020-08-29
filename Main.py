from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    img = cv2.imread('erosion.png')
    grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    (tresh, binarImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
    mask = np.ones((4,4))
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
