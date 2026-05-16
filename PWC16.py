import cv2
import os
import numpy as np

# -------------------------------
# Input and Output Folders
# -------------------------------
input_folder = 'D:/pseudowords/PWC16/1'
output_folder = 'D:/pseudowords/PWC16/samples'

os.makedirs(output_folder, exist_ok=True)

shift = 6

# -------------------------------
# Process all images
# -------------------------------
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):

        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        img = cv2.imread(input_path)

        if img is None:
            continue

        h, w = img.shape[:2]

        # -----------------------------------
        # Split into halves
        # -----------------------------------
        top_half = img[0:h // 2, :]
        bottom_half = img[h // 2:h, :]

        # -----------------------------------
        # Shift BOTTOM half RIGHT by 6 pixels
        # -----------------------------------
        bottom_shifted = np.zeros_like(bottom_half)
        bottom_shifted[:, shift:w] = bottom_half[:, 0:w - shift]

        # -----------------------------------
        # Combine image
        # -----------------------------------
        combined = np.vstack((top_half, bottom_shifted))

        # -----------------------------------
        # Remove 6 pixels from LEFT side
        # -----------------------------------
        cropped = combined[:, shift:w]

        # -----------------------------------
        # Resize to 200x40
        # -----------------------------------
        final_img = cv2.resize(cropped, (200, 40), interpolation=cv2.INTER_AREA)

        # Save result
        cv2.imwrite(output_path, final_img)

print("Done: Bottom RIGHT shift + LEFT crop + Resize completed!")