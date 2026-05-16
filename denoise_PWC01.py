

#input_folder = "D:/26_07/2"
#output_folder = "D:/26_07/3"

import cv2
import os

input_folder = "D:/tesseract_ocr/PWC01/samples"
output_folder = "D:/tesseract_ocr/PWC01/denoised"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)

    img = cv2.imread(input_path)

    if img is None:
        continue

    # Step 1: Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Step 2: Gaussian Blur
    blurred = cv2.GaussianBlur(gray, (3, 3), 1)

    # Step 3: Denoising
    denoised = cv2.fastNlMeansDenoising(blurred, None,
                                        h=30,
                                        templateWindowSize=7,
                                        searchWindowSize=21)

    # Step 4: Otsu's Binarization (IMPORTANT)
    _, otsu = cv2.threshold(denoised, 0, 255,
                            cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Save result
    output_path = os.path.join(output_folder, file)
    cv2.imwrite(output_path, otsu)

print("Blur + Denoise + Otsu applied to all images!")
