import streamlit as st
import requests

st.title("Telco Churn Prediction")

gender = st.selectbox("Gender", ["Female", "Male"])
gender_val = 0 if gender == "Female" else 1

senior = st.selectbox("Senior Citizen", ["No", "Yes"])
senior_val = 0 if senior == "No" else 1

partner = st.selectbox("Has Partner?", ["No", "Yes"])
partner_val = 0 if partner == "No" else 1

dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
dependents_val = 0 if dependents == "No" else 1

tenure = st.slider("Tenure (in months)", 0, 72, 9)

phone = st.selectbox("Phone Service", ["No", "Yes"])
phone_val = 0 if phone == "No" else 1

multiple_lines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
multiple_lines_val = {"No": 0, "Yes": 1, "No phone service": 2}[multiple_lines]

internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
internet_val = {"DSL": 0, "Fiber optic": 1, "No": 2}[internet_service]

online_sec = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_sec_val = {"No": 0, "Yes": 1, "No internet service": 2}[online_sec]

online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
online_backup_val = {"No": 0, "Yes": 1, "No internet service": 2}[online_backup]

device_protect = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
device_protect_val = {"No": 0, "Yes": 1, "No internet service": 2}[device_protect]

tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
tech_support_val = {"No": 0, "Yes": 1, "No internet service": 2}[tech_support]

stream_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
stream_tv_val = {"No": 0, "Yes": 1, "No internet service": 2}[stream_tv]

stream_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
stream_movies_val = {"No": 0, "Yes": 1, "No internet service": 2}[stream_movies]

contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])
contract_val = {"Month-to-month": 0, "One year": 1, "Two year": 2}[contract]

paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
paperless_val = 0 if paperless == "No" else 1

payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])
payment_val = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}[payment_method]

monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.00)
total_charges = st.number_input("Total Charges", min_value=0.0, value=845.50)

if st.button("Predict Churn"):
    input_data = {
        "Gender": gender_val,
        "SeniorCitizen": senior_val,
        "Partner": partner_val,
        "Dependents": dependents_val,
        "tenure": tenure,
        "PhoneService": phone_val,
        "MultipleLines": multiple_lines_val,
        "InternetService": internet_val,
        "OnlineSecurity": online_sec_val,
        "OnlineBackup": online_backup_val,
        "DeviceProtection": device_protect_val,
        "TechSupport": tech_support_val,
        "StreamingTV": stream_tv_val,
        "StreamingMovies": stream_movies_val,
        "Contract": contract_val,
        "PaperlessBilling": paperless_val,
        "PaymentMethod": payment_val,
        "MonthlyCharges": monthly_charges,
        "TotalCharges": total_charges
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=input_data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {'Churn' if result['prediction'] == 1 else 'No Churn'}")
    else:
        st.error("Prediction failed. Please check the backend.")