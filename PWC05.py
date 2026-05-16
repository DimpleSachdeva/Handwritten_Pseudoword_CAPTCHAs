
import cv2
import numpy as np
import random
import os

# Input and Output folders
input_folder = "D:/tesseract_ocr/PWC05/samples"  #D:/pseudowords/PWC03 PWC_D3/2
output_folder = "D:/tesseract_ocr/PWC05/samples"

os.makedirs(output_folder, exist_ok=True)

# Process all images in folder
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)

    image = cv2.imread(input_path)
    if image is None:
        continue

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Binary mask (text detection)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Get bounding box of full text
    x_min, y_min, x_max, y_max = float('inf'), float('inf'), 0, 0
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x + w)
        y_max = max(y_max, y + h)

    # Skip if no text found
    if x_min == float('inf'):
        continue

    # Create zig-zag path
    zigzag_path = []
    step = random.randint(10, 20)  # random step for variation

    mid_y = y_min + (y_max - y_min) // 2

    for i in range(x_min, x_max, step):
        amplitude = random.randint(-10, 10)
        zigzag_path.append((i, mid_y + amplitude))

    # Draw zig-zag line
    for i in range(len(zigzag_path) - 1):
        cv2.line(image, zigzag_path[i], zigzag_path[i + 1], (10, 10, 10), 1)

    # Save output
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, image)

print("Processing completed.")