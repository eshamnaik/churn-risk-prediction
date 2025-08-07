import streamlit as st
import pickle
import numpy as np

# Load the model
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("📞 Telco Churn Prediction App")

# Gender
gender_input = st.radio("Gender", ["Female", "Male"])
gender = 0 if gender_input == "Female" else 1

# Senior Citizen
senior_input = st.radio("Are you a Senior Citizen?", ["No", "Yes"])
senior_citizen = 0 if senior_input == "No" else 1

# Partner
partner_input = st.radio("Do you have a Partner?", ["No", "Yes"])
partner = 0 if partner_input == "No" else 1

# Dependents
dependents_input = st.radio("Do you have Dependents?", ["No", "Yes"])
dependents = 0 if dependents_input == "No" else 1

# Tenure
tenure = st.number_input("Tenure (in months)", min_value=0, max_value=100, value=12)

# Phone Service
phone_service_input = st.radio("Phone Service", ["No", "Yes"])
phone_service = 0 if phone_service_input == "No" else 1

# Multiple Lines
multiple_lines_input = st.radio("Multiple Lines", ["No", "Yes"])
multiple_lines = 0 if multiple_lines_input == "No" else 1

# Internet Service
internet_input = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No Internet"])
internet_map = {"DSL": 0, "Fiber optic": 1, "No Internet": 2}
internet_service = internet_map[internet_input]

# Online Security
online_security_input = st.radio("Online Security", ["No", "Yes"])
online_security = 0 if online_security_input == "No" else 1

# Online Backup
online_backup_input = st.radio("Online Backup", ["No", "Yes"])
online_backup = 0 if online_backup_input == "No" else 1

# Device Protection
device_protection_input = st.radio("Device Protection", ["No", "Yes"])
device_protection = 0 if device_protection_input == "No" else 1

# Tech Support
tech_support_input = st.radio("Tech Support", ["No", "Yes"])
tech_support = 0 if tech_support_input == "No" else 1

# Streaming TV
streaming_tv_input = st.radio("Streaming TV", ["No", "Yes"])
streaming_tv = 0 if streaming_tv_input == "No" else 1

# Streaming Movies
streaming_movies_input = st.radio("Streaming Movies", ["No", "Yes"])
streaming_movies = 0 if streaming_movies_input == "No" else 1

# Contract
contract_input = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
contract = contract_map[contract_input]

# Paperless Billing
paperless_billing_input = st.radio("Paperless Billing", ["No", "Yes"])
paperless_billing = 0 if paperless_billing_input == "No" else 1

# Payment Method
payment_input = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}
payment_method = payment_map[payment_input]

# Monthly & Total Charges
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, max_value=1000.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, max_value=5000.0, value=845.5)

# Predict Button
if st.button("Predict Churn"):
    features = np.array([[gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines,
                          internet_service, online_security, online_backup, device_protection, tech_support,
                          streaming_tv, streaming_movies, contract, paperless_billing, payment_method,
                          monthly_charges, total_charges]])
    
    prediction = model.predict(features)
    result = "⚠️ Churn Likely" if prediction[0] == 1 else "✅ No Churn"
    st.success(f"Prediction: {result}")
