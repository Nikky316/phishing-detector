![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-green)
![Machine Learning](https://img.shields.io/badge/ML-LogisticRegression-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

Phishing URL Detector
A Machine Learning–powered cybersecurity tool that analyzes URLs and classifies them as Safe, Suspicious, or Phishing, with a full explanation of why the URL was flagged.
This app uses:

Logistic Regression
Custom engineered URL features
Flask web application
Suspicious‑override heuristic layer
Bootstrap Cyber‑UI
Explainability module


Features
✔ Machine Learning Prediction
Analyzes 7 engineered URL features:

URL length
Dot count
HTTPS usage
IP presence
Hyphen count
Suspicious words
Domain length

✔ Suspicious‑Override System
A second layer of detection used in real SOC tools.
✔ Full Explainability
Shows why the engine flagged the URL:

Keywords detected
Banking indicators
HTTPS check
Hyphens
TLD anomalies
IP usage

✔ Risk Score + Color Coding
Results include:

🟢 SAFE
🟡 SUSPICIOUS
🔴 PHISHING

With a progress bar for risk visualization.
✔ POST‑Redirect‑GET (PRG) Implementation
Prevents:

Form resubmission
Cached results
Incorrect refresh behavior

✔ CLI mode
Predict phishing risk from the terminal using:
python predict.py


How It Works

User enters a URL
Features are extracted
ML model predicts phishing probability
Risk score is assigned
Override logic adjusts borderline predictions
Explanations provide transparency
UI displays the results in a clean dashboard


Installation
Clone the repository:
git clone https://github.com/Nikky316/phishing-detector.git
cd phishing-detector

Create a virtual environment:
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

Install dependencies:
pip install -r requirements.txt


Run the Application
Web App:
python app.py

Visit in browser:
http://127.0.0.1:5000

CLI Version:
python predict.py


📊 Dataset

Custom‑generated dataset using domain patterns
Includes 10,000 synthetic samples
Features extracted automatically
Model stored as model.pkl


File Structure
phishing-detector/
│── app.py
│── predict.py
│── model.py
│── features.py
│── data.csv
│── generate_dataset.py
│── templates/
│     └── index.html
│── requirements.txt
│── README.md


Deployment (Optional)
This project can be deployed on:
⭐ Render.com (recommended)
Railway.app
PythonAnywhere
Vercel (via serverless)
Deployment steps can be provided on request.


Future Improvements

Feature importance visualization
Real URL dataset integration
Threat intelligence API (VirusTotal, URLhaus)
Logging dashboard
Admin analytics panel
Multi-model comparison (XGBoost, RandomForest)


## 📸 Screenshots

### 🔹 Home Page  
<img src="assets/screenshots/home.png" width="500"/>

### 🔹 Suspicious URL Result  
<img src="assets/screenshots/suspicious.png" width="500"/>

### 🔹 Phishing Result  
<img src="assets/screenshots/phishing.png" width="500"/>



Author
Nike Nsikak-Nelson
Cybersecurity Professional | Blue Team | SOC Skills Development
LinkedIn / Portfolio (I can help you build this too)
