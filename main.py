import sys
import pytesseract
import re
import cv2
import preprocessor as pp
import buttonclick as bk
from pytesseract import Output
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import Image

form_class = uic.loadUiType("pyqt/main.ui")[0]

class Main(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 버튼 클릭
        self.image_add_btn.clicked.connect(self.buttonclick("image_add_btn"))

    def buttonclick(self, name):
        if name == "image_add_btn" :
            bk.image_add_btn()


    def method1(self):
        # pytesseract 사용을 위해서 tesseract 설치가 필요
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        # 해당 언어로 이미지 열고 String 형식으로 출력
        # print(pytesseract.image_to_string(Image.open('image_step1/test.jpg'), lang='kor'))

        # -- cv2로 이미지 텍스트 추출해보기 --
        # 이미지 로드
        img = cv2.imread('image_step1/test.jpg')

        # 전처리
        #img = pp.erode(img)

        # 옵션
        custom_config = r'--oem 3 --psm 6'
        lang = 'kor'

        # 출력
        aa = pytesseract.image_to_string(img, config=custom_config, lang=lang)
        print(aa)

        '''
        # 텍스트 주위에 상자 가져오기
        h, w, c = img.shape
        boxes = pytesseract.image_to_boxes(img)
        for b in boxes.splitlines():
            b = b.split(' ')
            img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)
    
        cv2.imshow('img', img)
        cv2.waitKey(0)
    
        # 텍스트 주위에 상자 가져오기(2)
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        print(d.keys())
        
        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
        cv2.imshow('img', img)
        cv2.waitKey(0)
        '''

        # 이미지에서 특정 위치를 찾기
        d = pytesseract.image_to_data(img, output_type=Output.DICT)
        keys = list(d.keys())

        date_pattern = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

        n_boxes = len(d['text'])
        for i in range(n_boxes):
            if int(d['conf'][i]) > 60:
                if re.match(date_pattern, d['text'][i]):
                    (x, y, w, h) = (d['left'][i], d['top'][i], d['width'][i], d['height'][i])
                img = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

        cv2.imshow('img', img)
        cv2.waitKey(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = Main()
    myWindow.show()
    app.exec_()



'''
# OpenCV의 이미지는 BGR 포멧, pytesseract는 RGB 포멧
# BGR을 RGB 포멧으로 변경시켜주어야 한다.
img_cv = cv2.imread(r'image_step1/test.jpg')
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))
'''

'''
# pytesseract에서 지원하는 언어 확인
print(pytesseract.get_languages(config=''))
# Get bounding box estimates
print(pytesseract.image_to_boxes(Image.open('image_step1/test.jpg')))
# Get verbose data including boxes
print(pytesseract.image_to_data(Image.open('image_step1/test.jpg')))
# Get information about orientation and script detection
print(pytesseract.image_to_osd(Image.open('image_step1/test.jpg')))
'''

'''
# Get a searchable PDF
pdf = pytesseract.image_to_pdf_or_hocr('image_step1/test.jpg', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf) # pdf type is bytes by default
# Get HOCR output
hocr = pytesseract.image_to_pdf_or_hocr('image_step1/test.jpg', extension='hocr')
# Get ALTO XML output
xml = pytesseract.image_to_alto_xml('test.png')
'''