# 🚗 Real-Time License Plate Detection & Recognition

This project uses Computer Vision and OCR (Optical Character Recognition) to detect vehicle license plates from images and extract the plate number automatically.

---

## 📌 Features

* 🔍 Detects license plates using Haar Cascade
* 🧠 Extracts text using EasyOCR
* 🖼️ Image preprocessing for improved OCR accuracy
* 🧾 Stores detected plate numbers in a CSV file
* 📊 Displays detection results using graphs
* 📸 Saves annotated output image
* 🕒 Logs timestamp for each detection
* 🚘 Supports multiple plate detection in a single image

---

## 🛠️ Tech Stack

* Python
* OpenCV
* EasyOCR
* NumPy
* Matplotlib
* Pandas

---

## 📂 Project Structure

```
License-Plate-Detection/
│
├── Data/
│   └── c2.jpg
│
├── haarcascade_russian_plate_number.xml
├── main.py
├── detected_plates.csv
├── annotated_output.jpg
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/kruthikashry/License-Plate-Detection.git
cd License-Plate-Detection
```

---

### 2. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ How to Run

```
python main.py
```

---

## 📊 Output

* License plate numbers printed in terminal
* CSV file updated with:

  * Timestamp
  * Plate number
* Annotated image saved with bounding boxes
* Graph showing frequency of detected plates

---

## 📸 Sample Output

* Input: Vehicle image
* Output:

  * Detected license plate region
  * Extracted plate text
  * Annotated image with bounding box

---

## 🚀 Future Enhancements

* 🎥 Real-time detection using webcam
* 🤖 Replace Haar Cascade with YOLO for higher accuracy
* 🌐 Web-based interface using Flask
* 🔐 Integration with traffic monitoring systems
* 🚦 Helmet and red-light violation detection

---

## 👨‍💻 Author

**Kruthikashree SK**
MCA Student | Python Developer

🔗 GitHub: https://github.com/kruthikashry

---

## ⭐ Acknowledgment

* OpenCV for computer vision tools
* EasyOCR for OCR capabilities

---

## 📌 Note

* Ensure image path is correct (`Data/c2.jpg`)
* Make sure Haar cascade file is present in the project directory

---

## 💡 Resume Value

This project demonstrates:

* Computer Vision implementation
* OCR (Optical Character Recognition)
* Image preprocessing techniques
* Data storage and logging (CSV)
* Data visualization using graphs
