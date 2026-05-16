import cv2
import numpy as np
import os
import random

input_folder = "D:/tesseract_ocr/PWC01/samples"    #D:/pseudowords/PWC01 PWC_D1/1
output_folder = "D:/tesseract_ocr/PWC01/samples"

os.makedirs(output_folder, exist_ok=True)


def add_interference(bg, num_lines=2, num_arcs=2):
    h, w = bg.shape

    overlay = bg.copy()

    # ---- Random Straight Lines ----
    for _ in range(num_lines):
        x1, y1 = random.randint(0, 80), random.randint(0, 20)
        x2, y2 = random.randint(0, 120), random.randint(0, h)

        color = random.randint(20, 50)  # dark gray/black
        thickness = 1

        cv2.line(overlay, (x1, y1), (x2, y2), color, thickness)

    # ---- Random Arcs (elliptical curves) ----
    for _ in range(num_arcs):
        center = (random.randint(0, w), random.randint(0, h))
        axes = (random.randint(20, 80), random.randint(10, 40))
        angle = random.randint(0, 180)

        startAngle = random.randint(0, 90)
        endAngle = startAngle + random.randint(90, 140)

        color = random.randint(40, 60)
        thickness = 1

        cv2.ellipse(overlay, center, axes, angle,
                    startAngle, endAngle, color, thickness)

    return overlay


def add_captcha_background(image):
    # Ensure grayscale
    if len(image.shape) == 3:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray = image.copy()

    h, w = gray.shape

    # Step 1: Text mask
    _, text_mask = cv2.threshold(gray, 0, 255,
                                 cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Step 2: Light gray background
    base_bg = np.full((h, w), 220, dtype=np.uint8)

    # Step 3: Gaussian noise
    noise = np.random.normal(0, 50, (h, w)).astype(np.int16)
    noisy_bg = base_bg.astype(np.int16) + noise
    noisy_bg = np.clip(noisy_bg, 0, 255).astype(np.uint8)

    # Step 4: Blur
    noisy_bg = cv2.GaussianBlur(noisy_bg, (3, 3), 0)

    # 🔥 Step 5: Add strokes + arcs
    noisy_bg = add_interference(noisy_bg)

    # Step 6: Extract text
    text = cv2.bitwise_and(gray, gray, mask=text_mask)

    # Step 7: Background without text
    bg_only = cv2.bitwise_and(noisy_bg, noisy_bg,
                             mask=cv2.bitwise_not(text_mask))

    # Step 8: Combine
    final = cv2.add(text, bg_only)

    return final


# Process folder
for file in os.listdir(input_folder):
    path = os.path.join(input_folder, file)

    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    result = add_captcha_background(img)

    cv2.imwrite(os.path.join(output_folder, file), result)

print("CAPTCHA-style noise + strokes + arcs added!")