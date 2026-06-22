import streamlit as st
import requests

st.title("🏦 Bank Customer Churn Predictor")

# -------------------
# USER INPUTS (RAW ONLY)
# -------------------
credit_score     = st.number_input("Credit Score")
country          = st.selectbox("Country", ["France", "Germany", "Spain"])
gender           = st.selectbox("Gender", ["Male", "Female"])
age              = st.number_input("Age", 18, 100, 30)
tenure           = st.number_input("Tenure")
balance          = st.number_input("Balance")
products_number  = st.number_input("Number of Products", 1, 4, 1)
credit_card      = st.selectbox("Has Credit Card", [0, 1])
active_member    = st.selectbox("Is Active Member", [0, 1])
estimated_salary = st.number_input("Salary")

# -------------------
# PREDICTION
# -------------------
if st.button("Predict Churn"):

    payload = {
        "credit_score"      : credit_score,
        "country"           : country,
        "gender"            : gender,
        "age"               : age,
        "tenure"            : tenure,
        "balance"           : balance,
        "products_number"   : products_number,
        "credit_card"       : credit_card,
        "active_member"     : active_member,
        "estimated_salary"  : estimated_salary,
    }

    response = requests.post(
           "https://minhalali12-bank-churn-prediction.hf.space/predict" , json=payload
    )

    result = response.json()

    if result["prediction"] == 1:
        st.error("⚠️ Customer will CHURN")
    else:
        st.success("✅ Customer will NOT churn")