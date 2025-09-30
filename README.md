# Diabetes Prediction (Machine Learning Project)
This project focuses on predicting diabetes using machine learning models trained on patient symptom data. The dataset consists of 520 patient records with 16 features (age, gender, and symptomatic attributes like polyuria, polydipsia, weight loss, etc.) and a binary target (Positive / Negative).The goal is to build a classification model that supports early detection of diabetes using non-invasive indicators, aiding in quick clinical screening and decision-making.

# Workflow
Data Preprocessing
Checked missing values → none found
Encoded categorical variables (Yes=1 / No=0, Male=1 / Female=0)
Train-Test Split (80:20)

Exploratory Data Analysis (EDA)
Countplots → symptom occurrence vs. diabetes outcome
Boxplots → Age distribution for Positive vs. Negative cases
Correlation Heatmap → Identified top predictors (Polyuria, Polydipsia, Sudden Weight Loss, Polyphagia)

Model Training & Evaluation
Trained multiple classification models and compared metrics:
| Model               | Accuracy   | Precision | Recall | ROC AUC |
| ------------------- | ---------- | --------- | ------ | ------- |
| **Random Forest**   | **95.51%** | 0.96      | 0.97   | 0.99    |
| Decision Tree       | 95.51%     | 0.96      | 0.96   | 0.95    |
| Logistic Regression | 94.87%     | 0.95      | 0.95   | 0.99    |
| SVM                 | 91.67%     | 0.92      | 0.92   | 0.98    |
| KNN                 | 83.97%     | 0.96      | 0.79   | 0.89    |

Best Model → Random Forest (highest accuracy & recall)

Model Deployment (Serialization)
Attempted pickle serialization (model.pkl)

# Key Strengths
End-to-end pipeline: EDA → preprocessing → modeling → evaluation → deployment
Clear comparison across 5 classifiers
