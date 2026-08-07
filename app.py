import streamlit as st
import numpy as np
import pickle

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="centered"
)

# -----------------------------
# Load Trained Model
# -----------------------------
model = pickle.load(open("diabetes_model.pkl", "rb"))

# -----------------------------
# Title
# -----------------------------
st.title("🩺 Diabetes Prediction System")
st.write("Predict whether a person is diabetic based on medical details.")

st.markdown("---")

# -----------------------------
# User Inputs
# -----------------------------
pregnancies = st.number_input(
    "Number of Pregnancies",
    min_value=0,
    max_value=20,
    value=1
)

glucose = st.number_input(
    "Glucose Level",
    min_value=0,
    max_value=250,
    value=120
)

blood_pressure = st.number_input(
    "Blood Pressure",
    min_value=0,
    max_value=150,
    value=70
)

skin_thickness = st.number_input(
    "Skin Thickness",
    min_value=0,
    max_value=100,
    value=20
)

insulin = st.number_input(
    "Insulin Level",
    min_value=0,
    max_value=900,
    value=79
)

bmi = st.number_input(
    "BMI",
    min_value=0.0,
    max_value=70.0,
    value=25.0
)

diabetes_pedigree = st.number_input(
    "Diabetes Pedigree Function",
    min_value=0.0,
    max_value=3.0,
    value=0.47,
    format="%.3f"
)

age = st.number_input(
    "Age",
    min_value=1,
    max_value=120,
    value=30
)

st.markdown("---")

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    input_data = np.array([[pregnancies,
                            glucose,
                            blood_pressure,
                            skin_thickness,
                            insulin,
                            bmi,
                            diabetes_pedigree,
                            age]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("" \
        " Prediction: The person is likely to have Diabetes.")
    else:
        st.success("✅ Prediction: The person is NOT likely to have Diabetes.")

st.markdown("---")
st.caption("Developed using Python, Streamlit and Machine Learning")