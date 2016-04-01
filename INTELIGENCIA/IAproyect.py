# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'IAproyect.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
#Librerias a utilizar
from PyQt4 import QtCore, QtGui
import cv2
from cv2 import *
from PIL import Image, ImageTk
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

#Creacion de botton,label, frame y text que vamos a utilizar
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(672, 429)
        Dialog.setMinimumSize(QtCore.QSize(0, 429))
        Dialog.setMaximumSize(QtCore.QSize(672, 429))
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(20, 40, 321, 241))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(260, 0, 121, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.frame_2 = QtGui.QFrame(Dialog)
        self.frame_2.setGeometry(QtCore.QRect(360, 40, 301, 231))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(20, 310, 321, 80))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.pushButton = QtGui.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(20, 10, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Papyrus"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 10, 81, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Papyrus"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_4 = QtGui.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 10, 75, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Papyrus"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.line = QtGui.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(10, 65, 291, 16))
        self.line.setLineWidth(4)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(20, 290, 321, 16))
        self.line_2.setLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(360, 290, 321, 16))
        self.line_3.setLineWidth(4)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.line_4 = QtGui.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(340, 40, 20, 251))
        self.line_4.setLineWidth(5)
        self.line_4.setFrameShape(QtGui.QFrame.VLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.dial = QtGui.QDial(Dialog)
        self.dial.setGeometry(QtCore.QRect(330, 320, 50, 64))
        self.dial.setObjectName(_fromUtf8("dial"))
        self.label_2.raise_()
        self.frame_2.raise_()
        self.widget.raise_()
        self.frame.raise_()
        self.line_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.dial.raise_()
# Aqui le damos los eventos de click a los bottones
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.CargarCamara)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.MostrarImagen)
        QtCore.QObject.connect(self.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.GuardarImagenes)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600; color:#55aaff;\">Bienvenido</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.pushButton.setText(_translate("Dialog", "Capturar", None))
        self.pushButton_2.setText(_translate("Dialog", "Mostrar", None))
        self.pushButton_4.setText(_translate("Dialog", "Guardar", None))

    #Metodo para iniciar la camara.
    def CargarCamara(self):
        namedWindow("webcam")

        #Instancia para la captura de video
        vc = VideoCapture(0);

        vc.set(3,300)
        vc.set(4,300)

        while True:
            #Se captura el video de la webcam
            next, frame = vc.read()
            #Se muestra el video donde se para frame que es la lectura del video de la webcam
            imshow("webcam", frame)
            #Se captura la tecla que se presiona
            tecla = waitKey(10)
            #Si es ESC se termina el ciclo
            if tecla == 27:
                break;
                cv2.destroyAllWindows()
            #Si es "t" se toma una imagen y se guarda
            if tecla == 116:

                cv2.imwrite('Imagen.jpg',frame)
                image = cv2.imread('Imagen.jpg')
                gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                cv2.imwrite('imagenGris.jpg',gray_image)

    def MostrarImagen(self):
        #Se crea la etiqueta para la foto
        #img = cv2.imread('Imagen.jpg',0)
        #cv2.imshow('Imagen',img)
        filename = "Imagen.jpg"
        oriimage = cv2.imread(filename,0)
        newx,newy = oriimage.shape[1]/1,oriimage.shape[0]/1 #new size (w,h)
        newimage = cv2.resize(oriimage,(newx,newy))
        cv2.imshow("resize image",newimage)
        cv2.waitKey(0)

    def GuardarImagenes(self):
        namedWindow("webcam")

        #Instancia para la captura de video
        vc = VideoCapture(0);

        vc.set(3,300)
        vc.set(4,300)

        while True:
            #Se captura el video de la webcam
            next, frame = vc.read()
            #Se muestra el video donde se para frame que es la lectura del video de la webcam
            imshow("webcam", frame)
            #Se captura la tecla que se presiona
            tecla = waitKey(10)
            #Si es ESC se termina el ciclo
            if tecla == 27:
                break;
                cv2.destroyAllWindows()
            #Si es "t" se toma una imagen y se guarda
            if tecla == 116:
                time.sleep(5)
                cv2.imwrite('Img1.jpg',frame)
                time.sleep(5)
                cv2.imwrite('Img2.jpg',frame)
                time.sleep(5)
                cv2.imwrite('Img3.jpg',frame)





if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
