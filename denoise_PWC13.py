import glob
import cv2
import numpy as np
for im in glob.glob("D:/PC_1000/PCS_13/1/*"):
    #img= cv2.imread(im.replace('/','\\'),0)
    image = cv2.imread(im.replace('/', '\\'), cv2.IMREAD_GRAYSCALE)
    _, binary = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY_INV)
    column_sums = np.sum(binary, axis=0)
    gap_columns = np.where(column_sums < 7)
    mask = np.zeros_like(image)
    mask[:, gap_columns] = 255
    img = cv2.inpaint(image, mask, inpaintRadius=5, flags=cv2.INPAINT_TELEA)
    img = cv2.GaussianBlur(img, (3, 3), 1)
    _, img = cv2.threshold(img, 200, 255, cv2.THRESH_OTSU)
    cv2.imwrite("D:\\PC_1000\\PCS_13\\denoise\\"+im[19:],img)
