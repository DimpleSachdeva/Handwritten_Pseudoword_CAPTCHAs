Handwritten Pseudoword CAPTCHA Dataset and Experimental Resources
Overview: 
This repository contains the complete experimental resources associated with the study on handwritten pseudoword CAPTCHA security evaluation. The repository provides CAPTCHA datasets, denoised outputs, source code, OCR evaluation resources, and machine learning classification files used in the experiments reported in the manuscript.
The repository has been organized to facilitate transparency, reproducibility, and independent verification of the reported results.
Repository Contents
CAPTCHA Scheme Archives
The repository contains sixteen handwritten pseudoword CAPTCHA schemes:
PWC_01.zip to PWC_16.zip
Each archive contains:
Sample CAPTCHA images generated using the corresponding scheme.
Denoised CAPTCHA images obtained after applying the proposed denoising framework.
Supporting documentation describing the implementation and experimental setup.
OCR Evaluation Archives
The repository also contains OCR evaluation resources for each CAPTCHA scheme:
PWC01_Tesseract.zip to PWC16_Tesseract.zip
Each OCR archive contains:
Tesseract OCR outputs for original CAPTCHA images.
Tesseract OCR outputs for denoised CAPTCHA images.
Recognition results used during OCR-based security evaluation.
CAPTCHA Generation Scripts
The following scripts are provided for CAPTCHA generation:
pwc01.py
pwc02.py
…
pwc16.py
These scripts generate CAPTCHA samples corresponding to each of the sixteen CAPTCHA schemes evaluated in the study.
Denoising Scripts
The repository includes denoising implementations for all CAPTCHA schemes:
denoise01.py
denoise02.py
…
denoise16.py
These scripts implement the denoising framework used to preprocess CAPTCHA images before OCR evaluation.
Machine Learning Classification Resources
The repository contains source code and supporting files for the machine learning experiments reported in the study, including:
Random Forest classifier
Support Vector Machine (SVM) classifier
K-Nearest Neighbors (KNN) classifier
These resources were used to evaluate CAPTCHA vulnerability against traditional machine learning approaches.
Experimental Workflow
The experimental workflow used in this study is illustrated below:
Step 1: CAPTCHA Generation
Run the CAPTCHA generation script corresponding to the desired CAPTCHA scheme.
Example:
python pwc01.py
Output:
Generated handwritten pseudoword CAPTCHA images for Scheme PWC_01.
Step 2: Denoising
Apply the denoising framework to the generated CAPTCHA images.
Example:
python denoise01.py
Output:
Denoised CAPTCHA images used for OCR and machine learning evaluation.
Step 3: OCR Evaluation
Review the corresponding Tesseract OCR archive.
Example:
PWC01_Tesseract.zip
The archive contains OCR recognition outputs for:
Original CAPTCHA images
Denoised CAPTCHA images
These results were used to assess CAPTCHA vulnerability before and after denoising
Step 4: Machine Learning Evaluation
Execute the provided classification scripts and supporting files for:
Random Forest
Support Vector Machine (SVM)
K-Nearest Neighbors (KNN)
These experiments evaluate CAPTCHA recognition performance using conventional machine learning techniques.
Dataset Organization
Each CAPTCHA scheme follows an identical organizational structure.
For example:
PWC_01.zip
├── samples/
├── denoised/
├── documentation/
The same structure is maintained for all sixteen CAPTCHA schemes (PWC_01–PWC_16).
Similarly, each OCR evaluation archive follows a consistent structure across all schemes.
Software Requirements
The experiments were implemented using Python.
Typical dependencies include:
Python 3.x
OpenCV
NumPy
Scikit-learn
Pillow
Matplotlib
Tesseract OCR
Install dependencies using:
pip install opencv-python numpy scikit-learn pillow matplotlib
Tesseract OCR should be installed separately according to the operating system being used.
Reproducibility
To reproduce the experiments reported in the manuscript:
Generate CAPTCHA images using the corresponding pwcXX.py script.
Apply denoising using the matching denoiseXX.py script.
Evaluate OCR performance using the provided Tesseract OCR resources.
Execute the Random Forest, SVM, and KNN classification experiments.
Compare the generated outputs with the reference results provided in the repository.
All datasets, source code, OCR outputs, and machine learning evaluation resources required to reproduce the reported experiments are publicly available in this repository.
