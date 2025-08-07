# 📞 Churn Risk Prediction

This project predicts customer churn using a machine learning model trained on the Telco dataset. It includes a model training script, a pickled model, and a Streamlit web application for real-time predictions.

---

## 📁 Project Structure

| File / Folder           | Description                                       |
|-------------------------|---------------------------------------------------|
| `dataset/telco_churn.csv` | Source dataset for training                     |
| `model_train.py`        | Trains and saves the churn prediction model       |
| `churn_model.pkl`       | Pickled trained model for prediction              |
| `app_streamlit.py`      | Streamlit app for user-friendly churn prediction  |
| `app.py`                | Optional Flask API for prediction (not required)  |
| `requirements.txt`      | Required Python libraries                         |

---

## ▶️ How to Use

### 🔧 1. Train the Model

If you want to retrain the model:

```bash
python model_train.py
