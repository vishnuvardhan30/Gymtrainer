# Gymtrainer


# 🏋️‍♂️ Fitness Pose Tracker – Webcam-Based Exercise Counter

A webcam-based fitness tracking application built using **MediaPipe**, **OpenCV**, and **Streamlit**. It detects body posture in real-time and automatically counts repetitions for popular exercises — no wearables or AI model training required.

---

## 🚀 Features

- 🎯 Real-time pose estimation using MediaPipe
- ✅ 5 Exercises with automatic rep counting or posture detection:
  - Bicep Curls
  - Dips
  - Sit-Ups
  - Plank (with timer)
  - Squats
- 📸 Live webcam feed with pose landmark visualization
- 🧠 Angle-based logic for rep detection using OpenCV + NumPy
- 🖥️ Interactive and clean UI built with Streamlit

---

## 📦 Tech Stack

- **[Streamlit](https://streamlit.io/)** – Web app interface
- **[MediaPipe](https://mediapipe.dev/)** – Pose landmark detection
- **OpenCV** – Video capture and annotation
- **NumPy** – Joint angle calculation
- **Python** – Application logic and control

---

## 🖥️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/vishnuvardhan30/Gymtrainer.git
cd Gymtrainer
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch the App
```bash
streamlit run app.py
```

---

---

## 📌 Project Structure
```
Gymtrainer/
├── app.py               # Streamlit UI & control
├── exercises.py         # Exercise logic & rep counters
├── requirements.txt     # Required packages
├── README.md            # Project overview
```

---

## 🤝 Contributions

Pull requests are welcome! If you want to add more exercises, improve UI, or include logging/export features, feel free to fork and enhance.

---

## 📄 License

This project is licensed under the MIT License — feel free to use it for learning or building personal projects.

---

## 🙋‍♂️ Author

Made with 💪 by [Vishnuvardhan](https://github.com/vishnuvardhan30)
