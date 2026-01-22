
# 🧰 OpenCV & MediaPipe – Prerequisites and Installation Guide

This document provides **clear prerequisites** and **copy-ready installation commands** for setting up **OpenCV** and **MediaPipe** with Python. You can upload this file directly to **GitHub** as `README.md`.

---

## ✅ Prerequisites

### 1️⃣ Operating System
- Windows 10 / 11
- macOS
- Linux

---

### 2️⃣ Python Version (Very Important)
MediaPipe works best with the following Python versions:
- ✅ **Python 3.9 – 3.11 (Recommended: Python 3.10)**
- ❌ Python 3.12 / 3.13 may cause installation or runtime issues

#### 🔍 Check Python Version (Copy Command)
```bash
python --version
```

---

### 3️⃣ Basic Python Knowledge Required
- Variables
- Loops (`for`, `while`)
- Functions
- Running Python scripts

(No advanced Python knowledge required)

---

## 📦 Required Libraries

### 🔹 OpenCV
Used for:
- Camera access
- Image & video processing
- Drawing shapes, text, and landmarks

#### 📥 Install OpenCV (Copy Command)
```bash
pip install opencv-python
```

---

### 🔹 MediaPipe
Used for:
- Hand detection
- Face detection
- Pose estimation
- Finger & gesture tracking

#### 📥 Install MediaPipe (Copy Command)
```bash
pip install mediapipe
```

---

### 🔹 NumPy
Used for:
- Image array operations
- Mathematical calculations

#### 📥 Install NumPy (Copy Command)
```bash
pip install numpy
```

---

### 🔹 Protobuf (Important for Windows Users)
Fixes common MediaPipe errors on Windows.

#### 📥 Install Protobuf (Copy Command)
```bash
pip install protobuf==3.20.3
```

---

## ⭐ Recommended One-Line Installation (All Together)

You can install everything using a single command:

```bash
pip install opencv-python mediapipe numpy protobuf==3.20.3
```

---

## 🧪 Verify Installation

Run the following code to check whether all libraries are installed correctly:

```python
import cv2
import mediapipe as mp
import numpy as np

print("OpenCV version:", cv2.__version__)
print("MediaPipe version:", mp.__version__)
print("NumPy version:", np.__version__)
```

If no errors appear, your setup is successful ✅

---

## 🗂️ Optional (Professional Setup)

### Create Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate:

**Windows**
```bash
venv\Scripts\activate
```

**Linux / macOS**
```bash
source venv/bin/activate
```

Then install libraries:
```bash
pip install opencv-python mediapipe numpy protobuf==3.20.3
```

---

## ⚠️ Common Issues & Fixes

### ❌ MediaPipe Installation Error
✔ Ensure Python version is 3.9–3.11

✔ Upgrade pip:
```bash
python -m pip install --upgrade pip
```

---

### ❌ Camera Not Opening
✔ Close other apps using the camera

✔ Try changing camera index:
```python
cv2.VideoCapture(1)
```

---

## 🧠 Simple Real-Life Analogy

| Component | Role |
|---------|------|
| Camera | Eyes 👀 |
| OpenCV | Vision processing |
| MediaPipe | AI brain 🧠 |
| Python | Control language |

---

## 📌 Summary

- ✅ Python 3.10 recommended
- ✅ OpenCV for camera & image handling
- ✅ MediaPipe for AI-based detection
- ✅ NumPy for calculations
- ✅ Protobuf for stability on Windows

---

## 👤 Author
**Chaithanya Muppala**  
Robotics Trainer | Python & Computer Vision

---

> 💡 Tip: All command blocks are **copy-ready** for easy use from GitHub.

