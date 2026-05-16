import cv2
import numpy as np
import os
import random

input_folder = "D:/tesseract_ocr/PWC03/samples"
output_folder = "D:/tesseract_ocr/PWC03/samples"

os.makedirs(output_folder, exist_ok=True)

# -------- Random Stroke --------
def add_random_stroke(image):
    h, w = image.shape[:2]
    stroke_img = image.copy()

    x1, y1 = random.randint(0, w-1), random.randint(0, h-1)
    x2, y2 = random.randint(0, w-1), random.randint(0, h-1)

    color = random.choice([(10, 10, 10), (20, 20, 20)])
    thickness = 1

    cv2.line(stroke_img, (x1, y1), (x2, y2), color, thickness)

    return stroke_img

# -------- Salt & Pepper Noise --------
def add_salt_pepper_noise(image, prob):
    noisy = np.copy(image)

    # Create random matrix for height x width
    rand = np.random.rand(image.shape[0], image.shape[1])

    # Apply noise to all 3 channels
    noisy[rand < prob / 2] = [255, 255, 255]   # Salt
    noisy[rand > 1 - prob / 2] = [0, 0, 0]     # Pepper

    return noisy

# -------- Processing --------
for file in os.listdir(input_folder):
    path = os.path.join(input_folder, file)

    img = cv2.imread(path)   # Keep color
    if img is None:
        continue

    img = cv2.resize(img, (200, 40))

    # Step 1: Add random stroke (same as your code: 1 stroke)
    for _ in range(random.randint(1, 1)):
        img = add_random_stroke(img)

    # Step 2: Add salt & pepper noise (same prob = 0.2)
    img = add_salt_pepper_noise(img, prob=0.15)

    # Save output
    out_path = os.path.join(output_folder, file)
    cv2.imwrite(out_path, img)

print("Random strokes + Salt & Pepper noise added to all images.")