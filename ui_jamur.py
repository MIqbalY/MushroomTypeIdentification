# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tugasakhir.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import pickle
import imutils
import cv2 as cv
from skimage.feature import local_binary_pattern
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from warnings import simplefilter

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 550)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #Header (1,2,3)
        #1
        self.label_Judul1 = QtWidgets.QLabel(self.centralwidget)
        self.label_Judul1.setGeometry(QtCore.QRect(250, 50, 381, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_Judul1.setFont(font)
        self.label_Judul1.setObjectName("label_Judul1")
        #2
        self.label_Judul2 = QtWidgets.QLabel(self.centralwidget)
        self.label_Judul2.setGeometry(QtCore.QRect(100, 70, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        self.label_Judul2.setFont(font)
        self.label_Judul2.setObjectName("label_Judul2")
        #3
        self.label_Judul3 = QtWidgets.QLabel(self.centralwidget)
        self.label_Judul3.setGeometry(QtCore.QRect(190, 70, 401, 16))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(8)
        font.setItalic(True)
        self.label_Judul3.setFont(font)
        self.label_Judul3.setObjectName("label_Judul3")

        #Citra Jamur
        self.groupBox_CitraJamur = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_CitraJamur.setGeometry(QtCore.QRect(70, 110, 150, 160))
        self.groupBox_CitraJamur.setObjectName("groupBox_CitraJamur")
        self.label_CitraJamur = QtWidgets.QLabel(self.groupBox_CitraJamur)
        self.label_CitraJamur.setGeometry(QtCore.QRect(10, 20, 128, 128))
        self.label_CitraJamur.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_CitraJamur.setText("")
        self.label_CitraJamur.setObjectName("label_CitraJamur")

        #Citra Grayscale
        self.groupBox_Grayscale = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Grayscale.setGeometry(QtCore.QRect(270, 110, 150, 160))
        self.groupBox_Grayscale.setObjectName("groupBox_Grayscale")
        self.label_Grayscale = QtWidgets.QLabel(self.groupBox_Grayscale)
        self.label_Grayscale.setGeometry(QtCore.QRect(10, 20, 128, 128))
        self.label_Grayscale.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Grayscale.setText("")
        self.label_Grayscale.setObjectName("label_Grayscale")

        #Citra LBP
        self.groupBox_LBP = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_LBP.setGeometry(QtCore.QRect(470, 110, 150, 160))
        self.groupBox_LBP.setObjectName("groupBox_LBP")
        self.label_LBP = QtWidgets.QLabel(self.groupBox_LBP)
        self.label_LBP.setGeometry(QtCore.QRect(10, 20, 128, 128))
        self.label_LBP.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_LBP.setText("")
        self.label_LBP.setObjectName("label_LBP")

        #Tabel Nilai Ekstraksi
        self.groupBox_NilaiEkstraksi = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_NilaiEkstraksi.setGeometry(QtCore.QRect(70, 290, 551, 111))
        self.groupBox_NilaiEkstraksi.setObjectName("groupBox_NilaiEkstraksi")
        self.tableWidget_NilaiEkstraksi = QtWidgets.QTableWidget(self.groupBox_NilaiEkstraksi)
        self.tableWidget_NilaiEkstraksi.setGeometry(QtCore.QRect(10, 20, 531, 71))
        self.tableWidget_NilaiEkstraksi.setObjectName("tableWidget_NilaiEkstraksi")
        self.tableWidget_NilaiEkstraksi.setColumnCount(10)
        self.tableWidget_NilaiEkstraksi.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_NilaiEkstraksi.setHorizontalHeaderItem(9, item)

        #Tombol Input
        self.pushButton_Input = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Input.setGeometry(QtCore.QRect(70, 410, 75, 70))
        self.pushButton_Input.setObjectName("pushButton_Input")

        #Tombol Reset
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Reset.setGeometry(QtCore.QRect(550, 410, 75, 70))
        self.pushButton_Reset.setObjectName("pushButton_Reset")

        #Tombol Pre-Pro Grayscale
        self.groupBox_Grayscl = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Grayscl.setGeometry(QtCore.QRect(150, 410, 70, 70))
        self.groupBox_Grayscl.setObjectName("groupBox_Grayscl")
        self.pushButton_Grayscale = QtWidgets.QPushButton(self.groupBox_Grayscl)
        self.pushButton_Grayscale.setGeometry(QtCore.QRect(5, 30, 61, 23))
        self.pushButton_Grayscale.setObjectName("pushButton_Grayscale")

        #Tombol Ekstraksi LBP
        self.groupBox_lbp = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_lbp.setGeometry(QtCore.QRect(220, 410, 70, 70))
        self.groupBox_lbp.setObjectName("groupBox_lbp")
        self.pushButton_LBP = QtWidgets.QPushButton(self.groupBox_lbp)
        self.pushButton_LBP.setGeometry(QtCore.QRect(5, 30, 61, 23))
        self.pushButton_LBP.setObjectName("pushButton_LBP")

        #Tombol Klasifikasi SVM
        self.groupBox_Klasifikasi = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Klasifikasi.setGeometry(QtCore.QRect(290, 410, 70, 70))
        self.groupBox_Klasifikasi.setObjectName("groupBox_Klasifikasi")
        self.pushButton_SVM = QtWidgets.QPushButton(self.groupBox_Klasifikasi)
        self.pushButton_SVM.setGeometry(QtCore.QRect(5, 30, 61, 23))
        self.pushButton_SVM.setObjectName("pushButton_SVM")

        #Label Output
        self.groupBox_Output = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_Output.setGeometry(QtCore.QRect(360, 410, 185, 70))
        self.groupBox_Output.setObjectName("groupBox_Output")
        self.label_Output = QtWidgets.QLabel(self.groupBox_Output)
        self.label_Output.setGeometry(QtCore.QRect(10, 28, 165, 25))
        self.label_Output.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_Output.setText("")
        self.label_Output.setObjectName("label_Output")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Tugas Akhir Jamur"))
        self.label_Judul1.setText(_translate("MainWindow", "IDENTIFIKASI JENIS JAMUR"))
        self.label_Judul2.setText(_translate("MainWindow", "Studi Kasus   : "))
        self.label_Judul3.setText(_translate("MainWindow", "Amanita Bisporigera, Amanita Citrina, Gyromitra Esculenta, Morchella Deliciosa"))
        self.groupBox_CitraJamur.setTitle(_translate("MainWindow", "Citra Jamur"))
        self.groupBox_Grayscale.setTitle(_translate("MainWindow", "Grayscale"))
        self.groupBox_LBP.setTitle(_translate("MainWindow", "Local Binary Pattern"))
        self.groupBox_NilaiEkstraksi.setTitle(_translate("MainWindow", "Nilai Ekstraksi"))
        item = self.tableWidget_NilaiEkstraksi.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "No"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "2"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "3"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "4"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "5"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "6"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "7"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "8"))
        item = self.tableWidget_NilaiEkstraksi.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "9"))
        self.pushButton_Input.setText(_translate("MainWindow", "Input"))
        self.groupBox_Grayscl.setTitle(_translate("MainWindow", "Grayscale"))
        self.pushButton_Grayscale.setText(_translate("MainWindow", "Grayscale"))
        self.groupBox_lbp.setTitle(_translate("MainWindow", "LBP"))
        self.pushButton_LBP.setText(_translate("MainWindow", "LBP"))
        self.groupBox_Klasifikasi.setTitle(_translate("MainWindow", "Klasifikasi"))
        self.pushButton_SVM.setText(_translate("MainWindow", "SVM"))
        self.groupBox_Output.setTitle(_translate("MainWindow", "Output"))
        self.pushButton_Reset.setText(_translate("MainWindow", "Reset"))

        #Button Action
        self.pushButton_Input.clicked.connect(self.InputImages)
        self.pushButton_Grayscale.clicked.connect(self.ConvertToGrayscale)
        self.pushButton_LBP.clicked.connect(self.ExtractLBP)
        self.pushButton_SVM.clicked.connect(self.ClassifiedBySVM)
        self.pushButton_Reset.clicked.connect(self.ResetFunction)

    def InputImages(self):
        fileName,_= QtWidgets.QFileDialog.getOpenFileName(None, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if fileName:
            pixmap = QtGui.QPixmap(fileName)
            pixmap = pixmap.scaled(self.label_CitraJamur.width(), self.label_CitraJamur.height())
            self.label_CitraJamur.setPixmap(pixmap)
            self.label_CitraJamur.setAlignment(QtCore.Qt.AlignCenter)
            self.file = fileName

            self.image = cv.imread(self.file, cv.IMREAD_ANYCOLOR)
            self.processedImage = self.image.copy()

            self.previewImage = imutils.resize(self.processedImage, width=128, height=128)
            self.displayImage()

    def displayImage(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len(self.previewImage.shape) == 3:
            if(self.previewImage.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888

        img1 = QtGui.QImage(self.previewImage, self.previewImage.shape[1], self.previewImage.shape[0], self.previewImage.strides[0], qFormat)
        img1 = img1.rgbSwapped()

        self.label_CitraJamur.setPixmap(QtGui.QPixmap.fromImage(img1))
        self.label_CitraJamur.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def ConvertToGrayscale(self):
        self.previewGrayscale = cv.cvtColor(self.previewImage, cv.COLOR_BGR2GRAY)
        self.displayGrayscale()

    def displayGrayscale(self):
        qFormat = QtGui.QImage.Format_Indexed8
        if len(self.previewGrayscale.shape) == 3:
            if(self.previewGrayscale.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888

        self.img1 = QtGui.QImage(self.previewGrayscale, self.previewGrayscale.shape[1], self.previewGrayscale.shape[0], self.previewGrayscale.strides[0], qFormat)
        self.img1 = self.img1.rgbSwapped()

        self.label_Grayscale.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.label_Grayscale.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

    def ExtractLBP(self):
        radius = 1
        n_points = 8*radius
        method = 'uniform'

        lbp = local_binary_pattern(self.previewGrayscale, n_points, radius, method)
        n_bins = int(lbp.max()+1)
        self.features, _ = np.histogram(lbp, density=True, bins=n_bins, range=(0, n_bins))
        self.previewLBP = lbp
        self.displayLBP()

    def displayLBP(self):
        fig = Figure((2,1.75))
        canvas = FigureCanvas(fig)
        ax = fig.add_subplot(111)
        ax.imshow(self.previewLBP)
        canvas.draw()
        size = canvas.size()
        width, height = size.width(), size.height()

        qFormat = QtGui.QImage.Format_Indexed8
        if len(self.previewLBP.shape) == 3:
            if(self.previewLBP.shape[2]) == 4:
                qFormat = QtGui.QImage.Format_RGBA8888
            else:
                qFormat = QtGui.QImage.Format_RGB888

        self.img1 = QtGui.QImage(canvas.buffer_rgba(), width, height, QtGui.QImage.Format_ARGB32)
        self.img1 = self.img1.rgbSwapped()

        self.label_LBP.setPixmap(QtGui.QPixmap.fromImage(self.img1))
        self.label_LBP.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.displayTableLBP()

    def displayTableLBP(self):
        self.tableWidget_NilaiEkstraksi.setItem(0, 0, QtWidgets.QTableWidgetItem(str(self.features[0])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 1, QtWidgets.QTableWidgetItem(str(self.features[1])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 2, QtWidgets.QTableWidgetItem(str(self.features[2])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 3, QtWidgets.QTableWidgetItem(str(self.features[3])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 4, QtWidgets.QTableWidgetItem(str(self.features[4])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 5, QtWidgets.QTableWidgetItem(str(self.features[5])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 6, QtWidgets.QTableWidgetItem(str(self.features[6])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 7, QtWidgets.QTableWidgetItem(str(self.features[7])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 8, QtWidgets.QTableWidgetItem(str(self.features[8])))
        self.tableWidget_NilaiEkstraksi.setItem(0, 9, QtWidgets.QTableWidgetItem(str(self.features[9])))

    def ClassifiedBySVM(self):
        simplefilter(action='ignore', category=UserWarning)
        model = pickle.load(open('modellbpsvm.sav','rb'))
        data = [self.features[:10]]
        hasil = model.predict(data)

        if hasil[0] == 0:
            self.label_Output.setText("Amanita Bisporigera (Poisonous)")
        if hasil[0] == 1:
            self.label_Output.setText("Amanita Citrina (Edible)")
        if hasil[0] == 2:
            self.label_Output.setText("Gyromitra Esculenta (Poisonous)")
        if hasil[0] == 3:
            self.label_Output.setText("Morchella Deliciosa (Edible)")

    def ResetFunction(self):
        self.label_CitraJamur.clear()
        self.label_Grayscale.clear()
        self.label_LBP.clear()
        self.tableWidget_NilaiEkstraksi.clearContents()
        self.label_Output.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())