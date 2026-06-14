# 📊 Bank Customer Churn Prediction using ANN

## 📌 Project Overview

This project predicts whether a bank customer will churn (leave the bank) or not using an Artificial Neural Network (ANN). The model is trained on customer demographic and financial data to classify churn behavior and help banks improve customer retention strategies.

---

## 🎯 Objective

The main objectives of this project are:

* Analyze customer demographic and financial data
* Perform data preprocessing (encoding and scaling)
* Build and train an Artificial Neural Network (ANN) model
* Predict customer churn (binary classification)
* Evaluate model performance using classification metrics

---

## 📁 Dataset Description

The dataset contains bank customer information:

* Credit Score
* Country
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Credit Card Status
* Active Member Status
* Estimated Salary

### 🎯 Target Variable:

* **Churn**

  * 0 → Customer stays
  * 1 → Customer leaves (churn)

---

## ⚙️ Technologies Used

* Python 🐍
* Pandas
* NumPy
* Scikit-learn
* TensorFlow / Keras
* Jupyter Notebook

---

## 🧹 Data Preprocessing

The following preprocessing steps were applied:

* Removed irrelevant column (`customer_id`)
* Identified categorical and numerical features
* Applied **One-Hot Encoding** for categorical variables
* Applied **Standard Scaling** for numerical features
* Combined processed features into final dataset
* Performed **train-test split before preprocessing** to avoid data leakage

---

## 🧠 Model Architecture (ANN)

The Artificial Neural Network consists of:

* Input Layer: Based on transformed feature size
* Hidden Layer 1: 20 neurons (ReLU activation)
* Hidden Layer 2: 10 neurons (ReLU activation)
* Hidden Layer 3: 5 neurons (ReLU activation)
* Output Layer: 1 neuron (Sigmoid activation)

### ⚙️ Training Configuration:

* Loss Function: Binary Crossentropy
* Optimizer: Adam
* Epochs: 100
* Batch Size: 10

---

## 📊 Evaluation Metrics

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

A threshold of **0.5** was used for classification.

---

## 📈 Results

* **Accuracy:** ~85%
* **Precision (Class 1):** ~0.66
* **Recall (Class 1):** ~0.50
* **F1-Score (Class 1):** ~0.57

### 📌 Class-wise Performance:

| Class        | Precision | Recall | F1-score |
| ------------ | --------- | ------ | -------- |
| 0 (No Churn) | 0.89      | 0.94   | 0.91     |
| 1 (Churn)    | 0.66      | 0.50   | 0.57     |

---

## 📌 Key Learnings

* Data preprocessing for neural networks
* One-Hot Encoding and feature scaling
* Importance of avoiding data leakage
* Building ANN using Keras
* Model evaluation using precision, recall, and F1-score
* Understanding classification trade-offs

---

## ⚠️ Future Improvements

* Hyperparameter tuning (layers, neurons, learning rate)
* Handling class imbalance (SMOTE / class weights)
* Trying different ML models (Random Forest, XGBoost)
* Model deployment using Streamlit or Flask
* Feature selection for better performance

---

## 📌 Conclusion

This project demonstrates a complete machine learning pipeline for churn prediction using an ANN. The model achieves good performance and provides a strong foundation for further optimization and deployment.

---
