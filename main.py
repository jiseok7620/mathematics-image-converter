import sys
import pytesseract
import re
import cv2
import os
import preprocessor as pp
import buttonclick as bk
import menuclick as mk
from pytesseract import Output
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import Image

form_class = uic.loadUiType("pyqt/main.ui")[0]

class Main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 시스템 환경 변수 %PATH%에 tesseract가 등록되어 있지 않다면 등록하기
        tesseract_home = "C:\\Program Files\\Tesseract-OCR"
        if tesseract_home not in os.environ["PATH"].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + tesseract_home

        # 메뉴 클릭
        self.action_open.triggered.connect(lambda : self.menuClick("open"))
        self.action_save.triggered.connect(lambda : self.menuClick("save"))
        self.action_capture.triggered.connect(lambda: self.menuClick("capture"))

        # 버튼 클릭
        #self.<버튼명>.clicked.connect(lambda: self.buttonClick(<이름>))

    def buttonClick(self, name):
        if name == "1":
            pass

    def menuClick(self, what):
        if what == "open":
            resultText = mk.openMenuClick()
            self.plainTextEdit.appendPlainText(resultText)
        elif what == "save":
            mk.saveMenuClick()
        elif what == "capture":
            resultText = "-------------------------------"
            resultText += mk.captureMenuClick()
            self.plainTextEdit.appendPlainText(resultText)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    myWindow.show()
    app.exec_()