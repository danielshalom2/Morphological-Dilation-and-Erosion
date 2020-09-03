from tkinter import *
from tkinter import filedialog
import cv2
from tkinter import messagebox
from modules import Erosion
from modules import Dilation
from matplotlib import pyplot as plt
import numpy as np


class GUI:
    img_path = None
    img = None
    gray_img = None
    binary_img = None
    master = None
    main_window = None
    loadfileButton = None
    erodeButton = None
    dilateButton = None
    openButton = None
    closeButton = None

    def __init__(self):
        self.master = Tk()
        self.master.title("Morphological Operation Project")
        ####### create a welcome text ##########
        welcomeLabel = Label(self.master, text="Welcome to Erosion and Dilation Program", font="Arial 32 bold")
        welcomeLabel.pack()
        usLabel = Label(self.master, text="Made by Vlad Gasin & Daniel Shalom", font="Arial 22 bold")
        usLabel.pack()
        ########################################

        ########### load file button ###########
        self.loadfileButton = Button(self.master, text="Load file")
        self.loadfileButton.bind('<Button-1>', self.loadfileButtonClick)
        self.loadfileButton.pack()
        ########################################

        self.master.mainloop()

    def loadfileButtonClick(self, event):
        self.img_path = filedialog.askopenfilename()
        img = cv2.imread(self.img_path)
        if img is not None:
            self.add_morphological_functions()
        if img is None:
            messagebox.showerror('Wrong File', 'can not read file, please choose an Image file!')
            self.img_path = None

    def add_morphological_functions(self):
        mo_oper_win = Toplevel(self.master)
        mo_oper_win.title("New Window")
        mo_oper_win.geometry("200x200")

        ########### erode button ###########
        self.erodeButton = Button(mo_oper_win, text="erode image")
        self.erodeButton.bind('<Button-1>', self.erodeButtonClick)
        self.erodeButton.pack()
        ########################################

        ########### dilate button ###########
        self.dilateButton = Button(mo_oper_win, text="dilate image")
        self.dilateButton.bind('<Button-1>', self.dilateButtonClick)
        self.dilateButton.pack()
        ########################################

        ########### open button ###########
        self.openButton = Button(mo_oper_win, text="open image")
        self.openButton.bind('<Button-1>', self.openButtonClick)
        self.openButton.pack()
        ########################################

        ########### close button ###########
        self.closeButton = Button(mo_oper_win, text="close image")
        self.closeButton.bind('<Button-1>', self.closeButtonClick)
        self.closeButton.pack()
        ########################################

    def erodeButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((12, 12), np.uint8)
        img_erosion = Erosion.erosion(self.binary_img, mask)
        plt.figure('Input')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.subplot(122)
        plt.imshow(img_erosion, 'gray')
        plt.show()

    def dilateButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((12, 12), np.uint8)
        img_dilation = Dilation.dilation(self.binary_img, mask)
        plt.figure('Input')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.subplot(122)
        plt.imshow(img_dilation, 'gray')
        plt.show()

    def openButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((12, 12), np.uint8)
        img_opening = Dilation.dilation(Erosion.erosion(self.binary_img, mask), mask)
        plt.figure('Input')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.subplot(122)
        plt.imshow(img_opening, 'gray')
        plt.show()

    def closeButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((12, 12), np.uint8)
        img_closing = Erosion.erosion(Dilation.dilation(self.binary_img, mask), mask)
        plt.figure('Input')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.subplot(122)
        plt.imshow(img_closing, 'gray')
        plt.show()

    def prepare_img(self):
        self.img = cv2.imread(self.img_path)
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        (thresh, self.binary_img) = cv2.threshold(self.gray_img, 127, 255, cv2.THRESH_BINARY)  # 1D array
        self.binary_img = self.binary_img / 255


if __name__ == '__main__':
    GUI()
