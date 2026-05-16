import glob
import cv2
import numpy as np
for im in glob.glob("D:/tesseract_ocr/PWC03/samples/*"):  #D:/pseudowords/PWC03 PWC_D3/3
    img = cv2.imread(im.replace('/', '\\'))

    img = cv2.GaussianBlur(img, (3, 3), 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, img = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.waitKey()
    cv2.destroyAllWindows()
    cv2.imwrite("D:\\tesseract_ocr\\PWC03\\denoised\\"+im[30:], img)

#D:/tesseract_ocr/PWC03/sample