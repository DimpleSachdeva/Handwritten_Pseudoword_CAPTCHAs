import cv2
import numpy as np
import os
import random

# Input and output folders
input_folder = "D:/6"
output_folder = "D:/PC_1000/PCS_13/1"  #D:/pseudowords/PWC02/1  D:\PC_1000\PCS_13\1
#D:/tesseract_ocr/PWC01/samples

os.makedirs(output_folder, exist_ok=True)

# List of characters A-Z
characters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

# Number of word images to generate
num_words = 286

for i in range(num_words):

    # Step 1: Select random word length (6–9)
    word_length = random.randint(7, 7)

    # Step 2: Select unique characters (no repetition)
    selected_chars = random.sample(characters, word_length)

    char_images = []

    for ch in selected_chars:
        char_folder = os.path.join(input_folder, ch)

        # Get all images for that character
        images = os.listdir(char_folder)

        # Select a random image
        img_name = random.choice(images)
        img_path = os.path.join(char_folder, img_name)

        # Read image in grayscale
        img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

        # Ensure size is 40x40
        img = cv2.resize(img, (40, 40))

        char_images.append(img)

    # Step 3: Concatenate horizontally
    word_img = np.hstack(char_images)

    # Step 4: Resize to 200x40
    word_img = cv2.resize(word_img, (200, 40))

    # Step 5: Save image
    word_text = ''.join(selected_chars)
    output_path = os.path.join(output_folder, f"{word_text}_{i}.png")

    cv2.imwrite(output_path, word_img)

print("Word image generation completed!")