from Erosion import *
from Dilation import *
from matplotlib import pyplot as plt


def main():
    # Reading the input image
    img = cv2.imread('fingerprint_1.png')
    grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    (tresh,binarImg) = cv2.threshold(grayImg, 127, 255, cv2.THRESH_BINARY)
    # Taking a matrix of size 5 as the kernel
    mask = np.ones((3, 3), np.uint8)
    img_erosion = erosion(binarImg, mask)
    # img_dilation = dilation(img, mask)

    plt.figure('Input')
    plt.subplot(131)
    plt.imshow(cv2.cvtColor(grayImg,cv2.COLOR_GRAY2RGB))
    plt.subplot(132)
    plt.imshow(cv2.cvtColor(img_erosion, cv2.COLOR_GRAY2RGB))
    # plt.subplot(133)
    # plt.imshow(cv2.cvtColor(img_dilation, cv2.COLOR_GRAY2RGB))
    plt.show()


if __name__ == '__main__':
    main()
