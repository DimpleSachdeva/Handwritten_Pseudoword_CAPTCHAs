import cv2
import os
import numpy as np

source_folder = 'D:/tesseract_ocr/PWC15/samples'
destination_folder = 'D:/tesseract_ocr/PWC15/samples'

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(source_folder, filename)

        image1 = cv2.imread(image_path)
        image2 = cv2.imread(image_path)

        # Resize
        image1 = cv2.resize(image1, (200, 40), interpolation=cv2.INTER_AREA)
        image2 = cv2.resize(image2, (200, 40), interpolation=cv2.INTER_AREA)

        height, width = image2.shape[:2]

        # 🔥 Horizontal shift (right by 6 pixels)
        t = np.float32([[1, 0, 6], [0, 1, 0]])
        image2 = cv2.warpAffine(image2, t, (width, height))

        # Blend images
        blend = cv2.addWeighted(image1, 0.5, image2, 0.5, 0)

        # Crop left side (remove blank region due to shift)
        cropped_image = blend[0:40, 6:200]

        # Resize back
        Final = cv2.resize(cropped_image, (200, 40), interpolation=cv2.INTER_AREA)

        destination_path = os.path.join(destination_folder, filename)
        cv2.imwrite(destination_path, Final)

print("Horizontal overlap images generated!")