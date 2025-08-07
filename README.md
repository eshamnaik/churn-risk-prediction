# Churn Risk Prediction

This project predicts customer churn using a machine learning model trained on the Telco dataset.

## Files
- `dataset/telco_churn.csv` — Source data
- `model_train.py` — Trains and saves the churn prediction model
- `app.py` — Flask API for making predictions
- `churn_model.pkl` — Pickled trained model
- `requirements.txt` — Required Python libraries

## Usage

1. Train the model:
   ```bash
   python model_train.py