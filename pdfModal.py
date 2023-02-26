from PyQt5.QtWidgets import *
from PyQt5 import uic
import traceback
import printform
import sqlite3

class MyModal(QDialog):
    def __init__(self, parent):
        super(MyModal, self).__init__(parent)
        option_ui = 'pyqt/modal.ui'
        uic.loadUi(option_ui, self)
        self.show()

        # 버튼 클릭
        self.pushButton.clicked.connect(lambda: self.makeForm()) # 출력 형식 만들기

        # 콤보박스 변경 시
        self.comboBox.currentTextChanged.connect(lambda: self.comboBoxEvent())  # 초,중,고 선택

        # 체크박스 체크 변경시
        self.checkBox.stateChanged.connect(lambda : self.checkboxChange())

    def makeForm(self):
        # db connect
        conn = sqlite3.connect("test.db", isolation_level=None)
        cs = conn.cursor()

        # 데이터 가져오기
        school = self.comboBox.currentText()
        select_list = (
            (school,)
        )
        cs.execute("SELECT * FROM table2 WHERE school =?", select_list)
        returnList = cs.fetchall()

        # 프린트 창 열기
        pf = printform.PrintForm(self, returnList)

    def checkboxChange(self):
        if self.checkBox.isChecked():
            self.label_5.setEnabled(True)
            self.label_6.setEnabled(True)
            self.label_7.setEnabled(True)
            self.lineEdit_2.setEnabled(True)
            self.lineEdit_3.setEnabled(True)
            self.lineEdit_4.setEnabled(True)
            self.checkBox_2.setEnabled(True)
            self.checkBox_3.setEnabled(True)
            self.checkBox_4.setEnabled(True)
        else :
            self.label_5.setEnabled(False)
            self.label_6.setEnabled(False)
            self.label_7.setEnabled(False)
            self.lineEdit_2.setEnabled(False)
            self.lineEdit_3.setEnabled(False)
            self.lineEdit_4.setEnabled(False)
            self.checkBox_2.setEnabled(False)
            self.checkBox_3.setEnabled(False)
            self.checkBox_4.setEnabled(False)
    
    def comboBoxEvent(self):
        what = self.comboBox.currentText()
        if what == "초등학교":
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

        elif what == "중학교":
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

        elif what == "고등학교":
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
