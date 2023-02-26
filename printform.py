from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PyQt5.QtCore import QFileInfo
import traceback

'''
프린트(print_)는 아래만 가능
QTextDocument
QPrintPreviewWidget
QPlainTextEdit
QTextEdit
'''

class PrintForm(QDialog):
    def __init__(self, parent, receptList):
        super(PrintForm, self).__init__(parent)
        option_ui = 'pyqt/printform.ui'
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼 연결
        self.pushButton.clicked.connect(lambda: self.printFunc("print")) # 인쇄하기 ctrl+p
        self.pushButton_2.clicked.connect(lambda: self.printFunc("printpreview")) # 인쇄미리보기 ctrl+o
        self.pushButton_3.clicked.connect(lambda: self.printFunc("pdf"))  # pdf로 저장하기 ctrl+s

        # 리턴받은 리스트 넣기
        self.returnList = receptList
        for list in self.returnList:
            pass

    # 모든 기능 모음
    def printFunc(self, what):
        if what == "print":
            print("인쇄")
            self.print_file()
        elif what == "printpreview":
            print("인쇄미리보기")
            self.print_preview_dialog()
        elif what == 'pdf':
            self.pdfExport()
    
    # 프린트하기 
    def print_file(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)
    
    # 프린트미리보기
    def print_preview(self, printer):
        self.textEdit.print_(printer)
    def print_preview_dialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        previewDialog = QPrintPreviewDialog(printer, self)
        previewDialog.paintRequested.connect(self.print_preview)
        previewDialog.exec_()
        
    # pdf로 저장하기
    def pdfExport(self):
        fn, _= QFileDialog.getSaveFileName(self, "Export PDF", None, "PDF files (.pdf);;All Files()")
        if fn != '':
            if QFileInfo(fn).suffix() == "":fn += '.pdf'
            printer = QPrinter(QPrinter.HighResolution)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setOutputFileName(fn)
            self.textEdit.document().print_(printer)