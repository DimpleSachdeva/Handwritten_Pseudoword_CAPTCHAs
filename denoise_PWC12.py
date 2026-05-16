import glob
import cv2

for im in glob.glob("D:/tesseract_ocr/PWC12/samples/*"):
    img = cv2.imread(im.replace('/', '\\'), 0)

    _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
    img = cv2.erode(img, (3, 3), iterations=3)
    cv2.imwrite("D:\\tesseract_ocr\\PWC12\\denoised\\" + im[30:], img)

