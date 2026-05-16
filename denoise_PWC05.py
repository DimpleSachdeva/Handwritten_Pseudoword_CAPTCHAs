import glob
import cv2
for im in glob.glob("D:/tesseract_ocr/PWC05/samples/*"):  #D:/pseudowords/PWC03 PWC_D3/4
    img= cv2.imread(im.replace('/','\\'),0)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_OTSU)
    #img=cv2.resize(img,(200,40),interpolation=cv2.INTER_AREA)
    cv2.imwrite("D:\\tesseract_ocr\\PWC05\\denoised\\"+im[30:],img)
