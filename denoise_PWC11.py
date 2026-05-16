import glob
import cv2
for im in glob.glob("D:/tesseract_ocr/PWC11/samples/*"): #D:/20/04/   D:/pseudowords/PWC09/samples
     img = cv2.imread(im.replace('/', '\\'))
     img = cv2.flip(img, -1)
     img = cv2.blur(img, (3, 3), 1)
     _, img = cv2.threshold(img, 128, 255, cv2.THRESH_BINARY)
     cv2.imwrite("D:\\tesseract_ocr\\PWC11\\denoised\\" + im[30:], img)