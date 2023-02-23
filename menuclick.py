from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import ImageGrab
from functools import partial
import cv2
import pytesseract
import preprocessor as pp
import pyautogui # mouse, keyboard 관련 도구함 끌어오기
import pyperclip # 클립보드에 저장 또는 불러오기 위함

def mouse_event(action, x, y, flags, *userdata):
    global lfx, lfy, rfx, rfy

    if action == cv2.EVENT_LBUTTONDOWN:
        lfx = x
        lfy = y

    elif action == cv2.EVENT_LBUTTONUP:
        rfx = x
        rfy = y

        # 이미지를 자르고 저장해주기
        image = cv2.imread("capture.png")
        cv2.imwrite("image_capture/capture.png", image[lfy:rfy, lfx:rfx])
        cv2.destroyWindow("Capture") # 창 닫기

def extractText(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

    # 이미지 로드 및 전처리
    img = cv2.imread(image)
    img = pp.get_grayscale(img) # GrayScale 변환
    #img = pp.remove_noise(img) # 노이즈 제거

    # 옵션
    custom_config = r'--oem 3 --psm 6'
    lang = 'kor+eng'

    # 출력
    resultText = pytesseract.image_to_string(img, config=custom_config, lang=lang)

    return resultText

def openMenuClick():
    fname = QFileDialog.getOpenFileNames()
    resultString = ""

    for fn in fname[0]:
        print(fn)
        resultString += extractText(fn) + "\n"
        resultString += "-------------------------------\n"

    return resultString

def saveMenuClick():
    print("save")

def captureMenuClick():
    # 먼저 전체화면을 캡쳐하기
    captureImg = "capture.png"
    # ImageGrab.grab = partial(ImageGrab.grab, all_screens=True) # 더블모니터일 때
    fulImg = ImageGrab.grab()
    fulImg.save(captureImg)

    # 캡쳐한 전체화면을 cv2 윈도우폼에 띄우기
    img = cv2.imread(captureImg)
    cv2.imshow("Capture", img)
    cv2.moveWindow("Capture",0,0)
    cv2.setMouseCallback("Capture", mouse_event)
    cv2.waitKey(0)

    # 자른 이미지의 텍스트를 추출하여 표시하기
    return extractText("image_capture/capture.png")
