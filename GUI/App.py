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
    setButton = None
    boundaryButton = None
    mgButton = None
    m = n = 3
    quitButton = None

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

        self.quitButton = Button(self.master, text="Exit", bg="red", fg="white", command=self.master.quit)
        self.quitButton.pack()

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
        mo_op_win = Toplevel(self.master)
        mo_op_win.title("Morphological Functions")
        intro_label = Label(mo_op_win,
                            text="Please insert the size of the Structure Element you want: (default: 3x3)")
        intro_label.grid(row=0, column=0, columnspan=8)
        m_label = Label(mo_op_win,
                        text="insert m:")
        m_label.grid(row=1, column=0)
        em = Entry(mo_op_win, width=10, border=5)
        em.grid(row=1, column=1)
        n_label = Label(mo_op_win,
                        text="insert n:")
        n_label.grid(row=1, column=2)
        en = Entry(mo_op_win, width=10, border=5)
        en.grid(row=1, column=3)
        ########### set MxN button ###########
        self.setButton = Button(mo_op_win, text="set mxn", command=lambda: self.set_m_n(em, en))
        self.setButton.grid(row=1, column=4)
        ########################################

        ########### erode button ###########
        self.erodeButton = Button(mo_op_win, text="erode image")
        self.erodeButton.bind('<Button-1>', self.erodeButtonClick)
        self.erodeButton.grid(row=5, column=0)
        ########################################

        ########### dilate button ###########
        self.dilateButton = Button(mo_op_win, text="dilate image")
        self.dilateButton.bind('<Button-1>', self.dilateButtonClick)
        self.dilateButton.grid(row=5, column=1)
        ########################################

        ########### open button ###########
        self.openButton = Button(mo_op_win, text="open image")
        self.openButton.bind('<Button-1>', self.openButtonClick)
        self.openButton.grid(row=5, column=2)
        ########################################

        ########### close button ###########
        self.closeButton = Button(mo_op_win, text="close image")
        self.closeButton.bind('<Button-1>', self.closeButtonClick)
        self.closeButton.grid(row=5, column=3)
        ########################################

        ########### boundary extraction button ###########
        self.boundaryButton = Button(mo_op_win, text="boundary extraction")
        self.boundaryButton.bind('<Button-1>', self.boundaryButtonClick)
        self.boundaryButton.grid(row=5, column=4)
        ########################################

        ########### morphological gradient  button ###########
        self.mgButton = Button(mo_op_win, text="morphological gradient")
        self.mgButton.bind('<Button-1>', self.mgButtonClick)
        self.mgButton.grid(row=5, column=5)
        ########################################

        self.quitButton = Button(mo_op_win, text="Exit", bg="red", fg="white", command=self.master.quit)
        self.quitButton.grid(row=7, column=3)

    def erodeButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_erosion = Erosion.erosion(self.binary_img, mask)
        plt.figure('Erode Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_erosion, 'gray')
        plt.title('Eroded')
        plt.show()

    def dilateButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_dilation = Dilation.dilation(self.binary_img, mask)
        plt.figure('Dilate Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_dilation, 'gray')
        plt.title('Dilated')
        plt.show()

    def openButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_opening = Dilation.dilation(Erosion.erosion(self.binary_img, mask), mask)
        plt.figure('Opened Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_opening, 'gray')
        plt.title('Opened')
        plt.show()

    def closeButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_closing = Erosion.erosion(Dilation.dilation(self.binary_img, mask), mask)
        plt.figure('Closed Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_closing, 'gray')
        plt.title('Closed')
        plt.show()

    def boundaryButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_boundary = self.binary_img - Erosion.erosion(self.binary_img, mask)
        plt.figure('Boundary Extraction Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_boundary, 'gray')
        plt.title('Boundary Extracted')
        plt.show()

    def mgButtonClick(self, event):
        self.prepare_img()
        mask = np.ones((int(self.m), int(self.n)), np.uint8)
        img_mg = Dilation.dilation(self.binary_img, mask) - Erosion.erosion(self.binary_img, mask)
        plt.figure('Morphological Gradient Result')
        plt.subplot(121)
        plt.imshow(self.gray_img, 'gray')
        plt.title('Original')
        plt.subplot(122)
        plt.imshow(img_mg, 'gray')
        plt.title('Morphological Gradient')
        plt.show()

    def prepare_img(self):
        self.img = cv2.imread(self.img_path)
        self.gray_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        (thresh, self.binary_img) = cv2.threshold(self.gray_img, 127, 255, cv2.THRESH_BINARY)  # 1D array
        self.binary_img = self.binary_img / 255

    def set_m_n(self, m, n):
        int_m = m.get()
        int_n = n.get()
        if int_m == 0:
            self.m = 3
        elif int_n == 0:
            self.n = 3

        else:
            self.m = m.get()
            self.n = n.get()


if __name__ == '__main__':
    GUI()
