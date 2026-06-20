# 🏦 Loan Approval Prediction System
**AIML Summer Internship 2026 | IIHMF, MNNIT Allahabad, Prayagraj**

---

## 📌 Project Overview
Luxe Capital is an AI-powered Loan Approval Prediction System that uses Machine Learning to predict whether a loan application should be approved or rejected based on applicant financial and demographic details.

**Team Leader:** Aditya Srivastava   
**Institute:** United College Of engineering and Research Prayagraj 
**Internship:** AIML Summer Internship 2026, IIHMF, MNNIT Allahabad

---

## 🎯 Objective
To build a classification model that predicts loan approval status based on applicant data such as income, credit history, loan amount, and other indicators — and deploy it as an interactive web application.

---

## 📁 Folder Structure
```
LoanApprovalPrediction/
│
├── Dataset/
│   ├── train.csv              # Training dataset (614 records)
│   └── test.csv               # Test dataset
│
├── Notebook/
│   └── LoanApprovalPrediction.ipynb   # Complete ML pipeline
│
├── Model/
│   ├── loan_model.pkl         # Trained Random Forest model
│   └── feature_names.pkl      # Feature names list
│
├── Flask_App/
│   ├── app.py                 # Flask backend
│   ├── templates/
│   │   ├── home.html          # Landing page
│   │   ├── login.html         # Login/Signup page
│   │   ├── index.html         # Prediction form
│   │   └── result.html        # Result page
│   └── static/
│       └── style.css          # Custom styles
│
├── Documentation/
│   ├── Project_Report.pdf     # 20-page project report
│   └── Presentation.pptx      # Project PPT
│
└── README.md                  # This file
```

---

## 🤖 Machine Learning Pipeline

### Phase 1 — Data Preprocessing
- Handled missing values (mode/median imputation)
- Removed duplicate records
- Dropped irrelevant columns (Loan_ID)
- Label encoded all categorical features

### Phase 2 — Exploratory Data Analysis (EDA)
- Target distribution analysis
- Univariate analysis (histograms + KDE plots)
- Bivariate analysis (boxplots, count plots)
- Correlation heatmap
- Scatter plots

### Phase 3 — Feature Engineering
| Feature | Formula |
|---|---|
| Total_Income | ApplicantIncome + CoapplicantIncome |
| LoanAmount_log | log(LoanAmount + 1) |
| Total_Income_log | log(Total_Income + 1) |
| EMI | LoanAmount / Loan_Amount_Term |
| Balance_Income | Total_Income − (EMI × 1000) |

### Phase 4 — Models Trained
| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---|---|---|---|---|
| Logistic Regression | 85.37% | 83.17% | 98.82% | 90.32% | 80.03% |
| **Random Forest** ✅ | **79.67%** | **84.09%** | **87.06%** | **85.55%** | **80.88%** |
| Gradient Boosting | 81.30% | 81.63% | 94.12% | 87.43% | 75.48% |

> ✅ **Random Forest** selected as final model (best ROC-AUC + balanced predictions)

---

## 🚀 How to Run

### Prerequisites
```bash
pip install flask numpy pandas scikit-learn
```

### Steps
```bash
# 1. Clone / unzip the project
cd LoanApprovalPrediction_[YourName]

# 2. Copy model files to Flask_App/Model/
cp Model/loan_model.pkl Flask_App/Model/
cp Model/feature_names.pkl Flask_App/Model/

# 3. Run the Flask app
cd Flask_App
python app.py

# 4. Open in browser
# http://127.0.0.1:5000
```

---

## 🌐 Application Flow
```
/ (Home Page)
    ↓
/login (Login / Signup)
    ↓
/predict-form (Enter Details)
    ↓
/predict (POST → ML Model)
    ↓
/result (Approved ✅ / Not Approved ❌ + Probability)
```

---

## 📊 Dataset
- **Source:** Kaggle Loan Prediction Dataset
- **Train records:** 614
- **Test records:** 367
- **Features:** 12 (after preprocessing)
- **Target:** Loan_Status (1 = Approved, 0 = Not Approved)
- **Class balance:** ~69% Approved, ~31% Not Approved

---

## 🛠 Tech Stack
| Component | Technology |
|---|---|
| Language | Python 3 |
| ML Libraries | scikit-learn, pandas, numpy |
| Visualization | matplotlib, seaborn, Chart.js |
| Web Framework | Flask |
| Frontend | HTML5, CSS3, Tailwind CSS |
| Model Serialization | pickle |
| Development | Jupyter Notebook / Google Colab |

---

## 📋 Deliverables
- [x] Jupyter Notebook/GoogleColab (complete ML pipeline)
- [x] Trained model files (.pkl)
- [x] Flask web application (4 pages)
- [x] Project Report (20 pages, PDF)
- [x] Presentation (PPT)
- [x] README documentation

---

## ⚠️ Academic Integrity
This project was independently developed as part of the AIML Summer Internship 2026. All code has been written and understood by the team members. External libraries and AI tools were used for learning purposes only.

---

*AIML Summer Internship 2026 | IIHMF, MNNIT Allahabad, Prayagraj*
