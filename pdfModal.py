from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QPdfWriter, QPagedPaintDevice, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
import traceback
import printform


class MyModal(QDialog):
    def __init__(self, parent):
        super(MyModal, self).__init__(parent)
        option_ui = 'pyqt/modal.ui'
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼 클릭
        self.pushButton.clicked.connect(lambda: self.makeForm()) # 출력 형식 만들기

    def makeForm(self):
        # 필터조건대로를 한 후 데이터를 리스트 형식으로 만들기


        # 만든 데이터를 printform에 넘겨주기
        pf = printform.PrintForm(self)

        
        