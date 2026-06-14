# 📊 Bank Customer Churn Prediction using ANN

## 📌 Project Overview

This project predicts whether a bank customer will churn (leave the bank) or not using an Artificial Neural Network (ANN). The model is trained on customer data and uses classification techniques to identify churn behavior.

---

## 🎯 Objective

The main goal of this project is to:

* Analyze customer data
* Preprocess and prepare features
* Build an ANN model
* Predict customer churn
* Evaluate model performance using classification metrics

---

## 📁 Dataset

The dataset contains bank customer information such as:

* Country
* Gender
* Age
* Balance
* Credit Score
* Estimated Salary
* Tenure
* Products Number
* Active Member
* Credit Card

Target variable:

* `churn` (0 = No churn, 1 = Churn)

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

Steps performed:

* Removed unnecessary column (`customer_id`)
* Checked missing values and duplicates
* One-Hot Encoding for categorical variables
* Standard Scaling for numerical features
* Combined features into final dataset

---

## 🧠 Model Architecture (ANN)

The neural network consists of:

* Input          : 11
* Hidden Layer 1 : 20 neurons (ReLU)
* Hidden Layer 2 : 10 neurons (ReLU)
* Hidden Layer 3 : 5 neurons (ReLU)
* Output Layer   : 1 neuron (Sigmoid)

Loss Function    : Binary Crossentropy
Optimizer        : Adam
Epochs           : 100
Batch Size       : 10

---

## 📊 Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Classification Report

A threshold of **0.3** was used for classification to improve recall.

---

## 📈 Results

* Accuracy            : 0.827 (82.7%)
* Precision (Class 1) : 0.55
* Recall (Class 1)    : 0.65
* F1-Score (Class 1)  : 0.60

Model performs well on binary classification with balanced evaluation metrics.

---

## 📌 Key Learnings

* Data preprocessing for ML models
* One-hot encoding & feature scaling
* Building ANN using Keras
* Model evaluation using classification metrics
* Effect of threshold tuning on precision/recall tradeoff

---

## 📌 Note

This is a beginner-friendly machine learning project built for learning and academic purposes.
