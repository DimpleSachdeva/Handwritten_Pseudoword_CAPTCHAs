import cv2
import os

# Input and Output folders
input_folder = "D:/tesseract_ocr/PWC09/samples"  #D:/pseudowords/PWC09/1
output_folder = "D:/tesseract_ocr/PWC09/samples"

# Create output folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Process all images in folder
for file_name in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file_name)

    # Read image
    img = cv2.imread(input_path)

    if img is None:
        continue

    # Flip vertically (along x-axis)
    flipped_img = cv2.flip(img, 0)

    # Save output
    output_path = os.path.join(output_folder, file_name)
    cv2.imwrite(output_path, flipped_img)

print("All images flipped vertically and saved.")