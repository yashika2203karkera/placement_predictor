# 🎓 Campus Placement Predictor

A Machine Learning-powered web application built with **Flask** and **Scikit-Learn** that predicts student placement status based on academic history and profile features. Designed for easy local execution or serverless deployment on **Vercel**.

---

## 🚀 Getting Started Locally

### 1. Clone the Project
```bash
git clone https://github.com
cd Campus-Placement-Predictor
```

### 2. Set Up Environment & Install Dependencies
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt
```

### 3. Run the Server
```bash
python api/index.py
```
Open **`http://127.0.0.1:5000/`** in your browser to view the application.

---

## 📂 Core Structure
* `api/index.py` — Flask backend application core logic.
* `model/placement_model.joblib` — Trained Scikit-Learn ML model.
* `templates/index.html` & `static/style.css` — Web UI and styling.
* `vercel.json` — Configuration blueprint for production deployment.
*
