import cv2
import numpy as np
import easyocr
import csv
import os
import re
import matplotlib.pyplot as plt
from datetime import datetime

# ======= SETTINGS ========
IMAGE_PATH = 'Data/c2'
CASCADE_PATH = 'haarcascade_russian_plate_number.xml'
CSV_FILE = 'detected_plates.csv'
SAVE_ANNOTATED_IMAGE = True
OUTPUT_IMAGE_PATH = 'annotated_output.jpg'
# ==========================

# Load image
img = cv2.imread(IMAGE_PATH)
if img is None:
    raise FileNotFoundError(f"❌ Error: Image not found at '{IMAGE_PATH}'")

# Load Haar cascade
if not os.path.exists(CASCADE_PATH):
    raise FileNotFoundError(f"❌ Error: Haar cascade not found at '{CASCADE_PATH}'")
plate_detector = cv2.CascadeClassifier(CASCADE_PATH)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect plates
plates = plate_detector.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=2, minSize=(30, 30))
print(f"Plates detected: {len(plates)}")

# Initialize EasyOCR
reader = easyocr.Reader(['en'])

# Create CSV if not exists
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Plate Number"])

# For each detected plate
for (x, y, w, h) in plates:
    plate_img = img[y:y+h, x:x+w]

    # Preprocess for better OCR
    plate_gray = cv2.cvtColor(plate_img, cv2.COLOR_BGR2GRAY)
    _, plate_thresh = cv2.threshold(plate_gray, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Resize for better OCR accuracy
    plate_resized = cv2.resize(plate_thresh, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # OCR
    results = reader.readtext(plate_resized)
    plate_text = results[0][1].upper().replace(" ", "") if results else "TEXT NOT FOUND"
    plate_text = re.sub(r'\W+', '', plate_text)

    # Draw on image
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv2.putText(img, f'Plate: {plate_text}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

    # Log result
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"✅ {timestamp} | Detected: {plate_text}")
    with open(CSV_FILE, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, plate_text])

# Optionally save the annotated image
if SAVE_ANNOTATED_IMAGE:
    cv2.imwrite(OUTPUT_IMAGE_PATH, img)
    print(f"📸 Annotated image saved to '{OUTPUT_IMAGE_PATH}'")

# ✅ Show the image in Jupyter
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10, 8))
plt.imshow(img_rgb)
plt.axis('off')
plt.title('Detected License Plate(s)')
plt.show()
