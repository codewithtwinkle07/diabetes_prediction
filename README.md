# 🩺 Diabetes Prediction Using Machine Learning

## 📌 Project Overview
This project predicts whether a person is diabetic or non-diabetic using Machine Learning. The model is trained on the Pima Indians Diabetes Dataset and deployed using Streamlit for an interactive web interface.

---

## 🎯 Objective
The objective of this project is to build a machine learning model that predicts diabetes based on medical parameters such as glucose level, BMI, blood pressure, insulin level, age, and more.

---

## 🛠 Technologies Used
- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```
Diabetes_Prediction/
│── app.py
│── train_model.py
│── diabetes_dataset_400.csv
│── diabetes_model.pkl
│── requirements.txt
│── README.md
```

---

## 📊 Dataset Features
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age
- Outcome (Target)

---

## 🤖 Machine Learning Model
Algorithm Used:
- Random Forest Classifier

Other algorithms that can also be used:
- Logistic Regression
- Decision Tree
- Support Vector Machine
- K-Nearest Neighbors

---

## 📈 Workflow
1. Load the dataset.
2. Preprocess the data.
3. Split into training and testing sets.
4. Train the Random Forest model.
5. Save the trained model using Pickle.
6. Load the model in Streamlit.
7. Accept user input.
8. Predict diabetes status.
9. Display the prediction.

---

## ✨ Features
- Simple and user-friendly interface
- Fast prediction
- Accurate machine learning model
- Easy to use
- Interactive Streamlit web application

---

## 📷 Output
The user enters medical information and clicks the **Predict** button. The application displays:
- ✅ Non-Diabetic
- ⚠️ Diabetic

---

## 👨‍💻 Author
**Twinkle**

B.Tech – Artificial Intelligence & Machine Learning

---

## 📄 License
This project is developed for educational and learning purposes.
