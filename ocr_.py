import cv2
import re 
import numpy as np
import pytesseract
import os

# Adding custom options
custom_config = r'--oem 3 --psm 1 -c preserve_interword_spaces=1'
UPLOAD_FOLDER = 'static/uploads/'
#ocr_.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#ans=pytesseract.image_to_string(img, config=custom_config)

#print(ans[:-1])

# noise removal
def remove_noise(image):
    return cv2.medianBlur(image,7)

#opening - erosion followed by dilation
def opening(image):
    kernel = np.ones((7,7),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)

#closing -  dilation followed by erosion
def closing(image):
    kernel = np.ones((5,5),np.uint8)
    return cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)


def ocr_driver(fname):
    image = cv2.imread(os.path.join(UPLOAD_FOLDER, fname))
    ocr1=pytesseract.image_to_string(image, config=custom_config)
    image_med=remove_noise(image)
    #cv2.imshow('img',image_med)
    #cv2.waitKey(0)
    ocr2=pytesseract.image_to_string(image_med, config=custom_config)
    image_op=opening(image)
    #cv2.imshow('img',image_op)
    #cv2.waitKey(0)
    ocr3=pytesseract.image_to_string(image_op, config=custom_config)
    image_cl=closing(image)
    #cv2.imshow('img',image_cl)
    #cv2.waitKey(0)
    ocr4=pytesseract.image_to_string(image_cl, config=custom_config)
    return ocr1[:-1],ocr2[:-1],ocr3[:-1]

def ocr_fun(fname):
    image = cv2.imread(os.path.join(UPLOAD_FOLDER, fname))
    ocr1=pytesseract.image_to_string(image, config=custom_config)
    print(ocr1)
    return ocr1


# ans=ocr_driver(img)
# for _ in ans:
#     print(_)

cv2.destroyAllWindows()


