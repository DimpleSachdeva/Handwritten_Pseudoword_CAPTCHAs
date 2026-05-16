import cv2
import os
import numpy as np

# -------------------------------
# Input and Output Folders
# -------------------------------
input_folder = 'D:/pseudowords/PWC16/samples'
output_folder = 'D:/pseudowords/PWC16/denoised'

os.makedirs(output_folder, exist_ok=True)

# Displacement value
displacement = 6

# -------------------------------
# Process all images
# -------------------------------
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        # Load image
        image = cv2.imread(input_path)

        if image is None:
            continue

        # Get dimensions
        height, width = image.shape[:2]
        split_line = height // 2

        # Split into halves
        top_half = image[:split_line, :]
        bottom_half = image[split_line:, :]

        # -----------------------------------
        # Repair transformation
        # (shift LEFT to fix RIGHT displacement)
        # -----------------------------------
        M = np.float32([[1, 0, -displacement], [0, 1, 0]])

        corrected_bottom = cv2.warpAffine(
            bottom_half,
            M,
            (width, bottom_half.shape[0])
        )

        # Recombine halves
        repaired_image = np.vstack((top_half, corrected_bottom))

        # Save result
        cv2.imwrite(output_path, repaired_image)

print("Done: Folder repair completed (6 px displacement)!")