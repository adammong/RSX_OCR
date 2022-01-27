from cv2 import FONT_HERSHEY_SCRIPT_SIMPLEX, FONT_HERSHEY_SIMPLEX, destroyAllWindows, imshow
import pytesseract
import cv2
import numpy as np
import matplotlib #not working idk why

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

font_scale = 1.5
font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("test.jpg")

camera = cv2.VideoCapture(1)

if not camera.isOpened():
    camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise IOError("Bruh check the cam") #if no webcam feed

cntr = 0;
while True:
    ret, frame = camera.read()
    cntr = cntr +1;
    if ((cntr%1) == 0): 
        imgH, imgW, _ = frame.shape
        x1, y1, w1, h1 = 0, 0, imgH, imgW 
        
        imgchar = pytesseract.image_to_string(frame)
        imgboxes = pytesseract.image_to_boxes(frame)
        
        for boxes in imgboxes.splitlines():
            boxes = boxes.split(' ')
            x, y, w, h = int(boxes[1]), int(boxes[2]), int(boxes[3]), int(boxes[4]) #coordinates follow: x, y, width, height
            cv2.rectangle(img, (x,imgH -y), (w, imgH-h), (255,0,242),3)  #draw rectangle around letters, colour is pinkish/purple
            font = cv2.FONT_HERSHEY_SIMPLEX
            
            print(imgchar) #continually prints out text that it sees

        cv2.putText(frame, imgchar, (x1 +int(w1/50), y1 +int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (88, 229,32), 2) #colour is green
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        cv2.imshow('Text Detection',frame)
        
        if cv2.waitKey(10) & 0xFF == ord('q'): #to exist press q or change it to whatever
            break
            
            
camera.release()
cv2.destroyAllWindows()