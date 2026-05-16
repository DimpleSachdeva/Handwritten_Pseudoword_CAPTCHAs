import cv2
import os
import numpy as np
source_folder = 'D:/tesseract_ocr/PWC14/samples'
destination_folder = 'D:/tesseract_ocr/PWC14/samples'

for filename in os.listdir(source_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(source_folder, filename)


        image1 = cv2.imread(image_path)

        image2 = cv2.imread(image_path)

        image1 = cv2.resize(image1, (200, 40), interpolation=cv2.INTER_AREA)
        image2 = cv2.resize(image2, (200, 40), interpolation=cv2.INTER_AREA)
        height, width = image2.shape[:2]
        t = np.float32([[1, 0, 0], [0, 1, 6]])
        image2 = cv2.warpAffine(image2, t, (width, height))
        blend = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)
        cropped_image = blend[8:40, 0:200]

        Final = cv2.resize(cropped_image, (200, 40), interpolation=cv2.INTER_AREA)
        destination_path = os.path.join(destination_folder, filename)
        cv2.imwrite(destination_path, Final),