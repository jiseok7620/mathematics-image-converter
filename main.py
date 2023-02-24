import sys
import os
import menuclick as mk
import dbManual as dm
import pdfModal
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("pyqt/main2.ui")[0]

class Main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 데이터베이스 생성 및 테이블 생성
        conn = sqlite3.connect("test.db", isolation_level=None)  # isolation_level=None : 자동커밋
        cs = conn.cursor() # 커서 획득
        # 테이블 생성
        cs.execute("CREATE TABLE IF NOT EXISTS table2 \
                    (id integer PRIMARY KEY, ques text, school text, grade text, unit text, answer text, diff text, \
                    exam1 text, exam2 text, exam3 text, exam4 text, exam5 text)")
        # db close
        conn.close()

        # 시스템 환경 변수 %PATH%에 tesseract가 등록되어 있지 않다면 등록하기
        tesseract_home = "C:\\Program Files\\Tesseract-OCR"
        if tesseract_home not in os.environ["PATH"].split(os.pathsep):
            os.environ["PATH"] += os.pathsep + tesseract_home

        # 테이블 설정
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        # 테이블 이벤트
        #self.tableWidget.cellChanged.connect(self.함수) # 셀 변경 시
        #self.tableWidget.cellClicked.connect(self.함수) # 셀 클릭 시
        #self.tableWidget.cellDoubleClicked.connec(self.함수) # 셀 더블클릭 시시

        # 메뉴 클릭
        self.action_open.triggered.connect(lambda : self.menuClick("open"))
        self.action_save.triggered.connect(lambda : self.menuClick("save"))
        self.action_capture.triggered.connect(lambda: self.menuClick("capture"))
        self.action_pdf.triggered.connect(lambda: self.menuClick("pdf"))


        # 버튼 클릭
        # self.btn.clicked.connect(lambda: self.(""))

        # 데이터베이스 조작
        self.btn_db.clicked.connect(lambda: self.databaseOper("db")) # db 조작
        self.pushButton4.clicked.connect(lambda: self.databaseOper("insert")) # db 저장
        self.pushButton5.clicked.connect(lambda: self.databaseOper("select")) # db 조회

        # 라디오버튼 선택 시
        self.radioButton1.clicked.connect(lambda: self.radioClicked("elem")) # 초등 선택
        self.radioButton2.clicked.connect(lambda: self.radioClicked("midd")) # 중등 선택
        self.radioButton3.clicked.connect(lambda: self.radioClicked("high")) # 고등 선택



    def buttonClick(self, name):
        if name == "non":
            pass



    def menuClick(self, what):
        if what == "open":
            resultText = mk.openMenuClick()
            self.plainTextEdit.appendPlainText(resultText)

        elif what == "save":
            mk.saveMenuClick()

        elif what == "capture":
            resultText = "-------------------------------\n"
            resultText += mk.captureMenuClick()
            self.plainTextEdit.appendPlainText(resultText)

        elif what == "pdf":
            modal = pdfModal.MyModal(self)

    def databaseOper(self, how):
        if how == "db":
            dm.dbTest()

        elif how == "insert":
            ques = self.plainTextEdit2.toPlainText()
            if self.radioButton1.isChecked():
                school = self.radioButton1.text()
            elif self.radioButton2.isChecked():
                school = self.radioButton1.text()
            elif self.radioButton3.isChecked():
                school = self.radioButton1.text()
            grade = self.comboBox1.currentText()
            unit = self.comboBox2.currentText()
            answer = self.lineEdit1.text()
            diff = self.comboBox3.currentText()
            exam1 = self.lineEdit2.text()
            exam2 = self.lineEdit3.text()
            exam3 = self.lineEdit4.text()
            exam4 = self.lineEdit5.text()
            exam5 = self.lineEdit6.text()
            return_msg = dm.dbInsert(ques, school, grade, unit, answer, diff, exam1, exam2, exam3, exam4, exam5)
            if return_msg == 1:
                reply = QMessageBox.about(self, "알림창", "저장이 완료되었습니다.")
            else :
                reply = QMessageBox.about(self, "Error!!", return_msg)

        elif how == "select":
            return_list = dm.dbSelect()
            self.tableWidget.setRowCount(len(return_list))
            num = 0
            for row in return_list:
                self.tableWidget.setItem(num, 0, QTableWidgetItem(str(row[0])))
                self.tableWidget.setItem(num, 1, QTableWidgetItem(str(row[4])))
                self.tableWidget.setItem(num, 2, QTableWidgetItem(str(row[5])))
                self.tableWidget.setItem(num, 3, QTableWidgetItem(str(row[7])))
                self.tableWidget.setItem(num, 4, QTableWidgetItem(str(row[8])))
                self.tableWidget.setItem(num, 5, QTableWidgetItem(str(row[9])))
                self.tableWidget.setItem(num, 6, QTableWidgetItem(str(row[10])))
                self.tableWidget.setItem(num, 7, QTableWidgetItem(str(row[11])))
                self.tableWidget.setItem(num, 8, QTableWidgetItem(str(row[2])))
                self.tableWidget.setItem(num, 9, QTableWidgetItem(str(row[3])))
                self.tableWidget.setItem(num, 10, QTableWidgetItem(str(row[6])))
                num += 1


    def radioClicked(self, what):
        if what == "elem":
            self.comboBox1.clear()
            self.comboBox2.clear()
            # 학년 콤보박스
            self.comboBox1.addItem("1")
            self.comboBox1.addItem("2")
            self.comboBox1.addItem("3")
            self.comboBox1.addItem("4")
            self.comboBox1.addItem("5")
            self.comboBox1.addItem("6")
            # 단원 콤보박스
            self.comboBox2.addItem("초등단원1")
            self.comboBox2.addItem("초등단원2")
            self.comboBox2.addItem("초등단원3")

        elif what == "midd":
            self.comboBox1.clear()
            self.comboBox2.clear()
            # 학년 콤보박스
            self.comboBox1.addItem("1")
            self.comboBox1.addItem("2")
            self.comboBox1.addItem("3")
            # 단원 콤보박스
            self.comboBox2.addItem("중등단원1")
            self.comboBox2.addItem("중등단원2")
            self.comboBox2.addItem("중등단원3")

        elif what == "high":
            self.comboBox1.clear()
            self.comboBox2.clear()
            # 학년 콤보박스
            self.comboBox1.addItem("1")
            self.comboBox1.addItem("2")
            self.comboBox1.addItem("3")
            # 단원 콤보박스
            self.comboBox2.addItem("고등단원1")
            self.comboBox2.addItem("고등단원2")
            self.comboBox2.addItem("고등단원3")




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    myWindow.show()
    app.exec_()