# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import os

# app = Flask(__name__)

# # Load model and feature names
# model = pickle.load(open('Model/loan_model.pkl', 'rb'))
# feature_names = pickle.load(open('Model/feature_names.pkl', 'rb'))

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get form data
#         gender = int(request.form['gender'])
#         married = int(request.form['married'])
#         dependents = int(request.form['dependents'])
#         education = int(request.form['education'])
#         self_employed = int(request.form['self_employed'])
#         loan_amount_term = float(request.form['loan_amount_term'])
#         credit_history = float(request.form['credit_history'])
#         property_area = int(request.form['property_area'])
#         applicant_income = float(request.form['applicant_income'])
#         coapplicant_income = float(request.form['coapplicant_income'])
#         loan_amount = float(request.form['loan_amount'])

#         # Feature Engineering (same as notebook)
#         total_income = applicant_income + coapplicant_income
#         loan_amount_log = np.log(loan_amount + 1)
#         total_income_log = np.log(total_income + 1)
#         emi = loan_amount / loan_amount_term if loan_amount_term > 0 else 0
#         balance_income = total_income - (emi * 1000)

#         # Input array (order must match training features)
#         input_data = np.array([[
#             gender, married, dependents, education, self_employed,
#             loan_amount_term, credit_history, property_area,
#             loan_amount_log, total_income_log, emi, balance_income
#         ]])

#         prediction = model.predict(input_data)[0]
#         probability = model.predict_proba(input_data)[0][1] * 100

#         result = {
#             'status': 'Approved' if prediction == 1 else 'Not Approved',
#             'approved': prediction == 1,
#             'probability': round(probability, 2)
#         }

#         return render_template('result.html', result=result)

#     except Exception as e:
#         return render_template('result.html', error=str(e))

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np
import os
app = Flask(__name__)
# Load model and feature names
model = pickle.load(open('Model/loan_model.pkl', 'rb'))
feature_names = pickle.load(open('Model/feature_names.pkl', 'rb'))
# ── Landing Page ──
@app.route('/')
def landing():
    return render_template('home.html')

# ── Login / Signup ──
@app.route('/login')
def login():
    return render_template('login.html')

# ── Prediction Form ──
@app.route('/predict-form')
def predict_form():
    return render_template('index.html')

# ── Predict (POST) ──
@app.route('/predict', methods=['POST'])
def predict():
    try:
        gender           = int(request.form['gender'])
        married          = int(request.form['married'])
        dependents       = int(request.form['dependents'])
        education        = int(request.form['education'])
        self_employed    = int(request.form['self_employed'])
        loan_amount_term = float(request.form['loan_amount_term'])
        credit_history   = float(request.form['credit_history'])
        property_area    = int(request.form['property_area'])
        applicant_income    = float(request.form['applicant_income'])
        coapplicant_income  = float(request.form['coapplicant_income'])
        loan_amount         = float(request.form['loan_amount'])

        # Feature Engineering
        total_income      = applicant_income + coapplicant_income
        loan_amount_log   = np.log(loan_amount + 1)
        total_income_log  = np.log(total_income + 1)
        emi               = loan_amount / loan_amount_term if loan_amount_term > 0 else 0
        balance_income    = total_income - (emi * 1000)

        input_data = np.array([[
            gender, married, dependents, education, self_employed,
            loan_amount_term, credit_history, property_area,
            loan_amount_log, total_income_log, emi, balance_income
        ]])

        prediction  = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100

        result = {
            'status':             'Approved' if prediction == 1 else 'Not Approved',
            'approved':           prediction == 1,
            'probability':        round(probability, 2),
            'applicant_income':   applicant_income,
            'coapplicant_income': coapplicant_income,
            'loan_amount':        loan_amount
        }
        return render_template('result.html', result=result)

    except Exception as e:
        return render_template('result.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)