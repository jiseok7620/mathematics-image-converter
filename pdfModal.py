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
        pf = printform.PrintForm(self)

        '''
        # pdf 생성
        pdf = QPdfWriter('test.pdf')
        pdf.setPageSize(QPagedPaintDevice.A4)

        # 화면 캡쳐
        screen = QApplication.primaryScreen()
        img = screen.grabWindow(self.winId(), 0, 0, self.rect().width(), self.rect().height())

        # 3항 연산자 (a if test else b, 만약 test가 참이면 a, 아니면 b)
        # 이미지 크기는 큰 값 기준, PDF 크기는 작은값 기준(화면 초과 방지)
        #img_size = img.width() if img.width() - img.height() > 0 else img.height()
        #pdf_size = pdf.width() if pdf.width() - pdf.height() < 0 else pdf.height()

        # 최적 비율 얻기
        #ratio = pdf_size / img_size

        # pdf에 쓰기
        qp = QPainter()
        qp.begin(pdf)
        #qp.drawPixmap(0, 0, img.width() * ratio, img.height() * ratio, img)
        qp.drawPixmap(0, 0, img)
        qp.end()
        '''