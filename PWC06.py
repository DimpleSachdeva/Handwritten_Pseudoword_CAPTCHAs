import cv2
import os
import numpy as np
import random

input_folder = 'D:/pseudowords/PWC06/1'
output_folder = 'D:/pseudowords/PWC06/samples'

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):

        path = os.path.join(input_folder, filename)
        img = cv2.imread(path)

        if img is None:
            continue

        h, w = img.shape[:2]

        # Random number of circles per image
        num_circles = random.randint(4, 6)

        for _ in range(num_circles):
            x = random.randint(0, w - 1)
            y = random.randint(0, h - 1)
            radius = random.randint(3, 5)

            if len(img.shape) == 2:
                cv2.circle(img, (x, y), radius, 255, -1)
            else:
                cv2.circle(img, (x, y), radius, (200, 200, 200), -1)

        cv2.imwrite(os.path.join(output_folder, filename), img)

print("Done: Occlusion with random white circles applied!")