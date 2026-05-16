import cv2
import os

input_folder = "D:/tesseract_ocr/PWC04/samples"
output_folder = "D:/tesseract_ocr/PWC04/samples"

os.makedirs(output_folder, exist_ok=True)

for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)
    output_path = os.path.join(output_folder, file)

    img = cv2.imread(input_path)

    if img is None:
        continue

    # Resize to 300x40
    resized = cv2.resize(img, (300, 40), interpolation=cv2.INTER_LINEAR)

    # Apply Gaussian Blur
    blurred = cv2.GaussianBlur(resized, (7, 7), 5)

    # Save output
    cv2.imwrite(output_path, blurred)

print("Done processing all images!")