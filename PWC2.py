import cv2
import numpy as np
import os

# Input and output folders
input_folder = "D:/tesseract_ocr/PWC02/samples"
output_folder = "D:/tesseract_ocr/PWC02/samples"

os.makedirs(output_folder, exist_ok=True)

# Loop through all images
for file in os.listdir(input_folder):
    input_path = os.path.join(input_folder, file)

    # Read image
    image = cv2.imread(input_path, cv2.IMREAD_UNCHANGED)

    if image is None:
        continue

    # Convert to grayscale if needed
    if len(image.shape) == 2:
        gray = image
    else:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Otsu threshold (text mask)
    _, binary_mask = cv2.threshold(
        gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # Ensure 3-channel image
    if len(image.shape) == 2:
        image_color = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)
    else:
        image_color = image.copy()

    # Generate Gaussian noise (IMPORTANT FIX: use int16, not uint8)
    noise = np.random.normal(0, 10, image_color.shape).astype(np.uint8)

    # Convert image to int16 to avoid overflow
    image_int = image_color.astype(np.int16)

    # Add noise only on text region
    noisy = image_int.copy()
    mask_indices = binary_mask == 255
    noisy[mask_indices] = image_int[mask_indices] + noise[mask_indices]

    # Clip values to valid range
    noisy = np.clip(noisy, 0, 255).astype(np.uint8)
    img = cv2.cvtColor(noisy, cv2.COLOR_BGR2GRAY)

    # Save result
    output_path = os.path.join(output_folder, file)
    cv2.imwrite(output_path, img)

print("Processing completed successfully!")