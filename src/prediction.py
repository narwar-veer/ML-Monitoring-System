# Defining function for streamline
def perform_prediction():
         
    import streamlit as st
    import numpy as np
    import pickle
    import pandas as pd
    st.markdown('<h1 class="title">Stroke Prediction</h1>', unsafe_allow_html=True)
    st.write("Enter the following information to predict stroke.")
    model = pickle.load(open('artifacts/Stroke.pkl', 'rb'))
    # Gender
    gender = st.selectbox("Gender", ["Male", "Female"])

    # Age
    age = st.number_input("Age", min_value=0, max_value=110, value=30)

    # Hypertension
    hypertension = st.checkbox("Hypertension")

    # Heart disease
    heart_disease = st.checkbox("Heart Disease")

    # Marital status
    ever_married = st.checkbox("Ever Married")

    # Residence type
    Residence_type = st.selectbox("Residence Type", ["Urban", "Rural"])

    # Average glucose level
    avg_glucose_level = st.number_input("Average Glucose Level", value=80.0)

    # BMI
    bmi = st.number_input("Body Mass Index (BMI)", value=25.0)

    # Work type
    work_type = st.selectbox("Work Type", ["Never worked", "Private", "Self-employed", "Children", "Govt job"])

    # Smoking status
    smoking_status = st.selectbox("Smoking Status", ["Formerly smoked", "Never smoked", "Smokes", "Unknown"])

    # Convert selected options to binary values
    gender_Male = 1 if gender == "Male" else 0
    
    Residence_type = 1 if Residence_type == "Urban" else 0
    
    if work_type == 'Never_worked':
        work_type_Never_worked = 1
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 0
        work_type_Govt_job = 0

    if work_type == 'Private':
        work_type_Never_worked = 0
        work_type_Private = 1
        work_type_Self_employed = 0
        work_type_children = 0
        work_type_Govt_job = 0

    elif work_type == "Self_employed":
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 1
        work_type_children = 0
        work_type_Govt_job = 0

    elif work_type == "children":
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 1
        work_type_Govt_job 
    else:
        work_type_Never_worked = 0
        work_type_Private = 0
        work_type_Self_employed = 0
        work_type_children = 0
        work_type_Govt_job = 1

    if smoking_status == "formerly_smoked":
        smoking_status_formerly_smoked = 1
        smoking_status_never_smoked = 0
        smoking_status_Smokes = 0
        smoking_status_Unknown = 0

    elif smoking_status == "never_smoked":
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 1
        smoking_status_Smokes = 0
        smoking_status_Unknown = 0

    elif smoking_status == "Smokes":
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_Smokes = 1
        smoking_status_Unknown = 0

    else:
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_Smokes = 0
        smoking_status_Unknown = 1

    pred= None
    # Predict button
    if st.button("Predict"):
        values = np.array([[gender_Male,age, hypertension, heart_disease, ever_married,
                            Residence_type, avg_glucose_level, bmi,
                            work_type_Never_worked, work_type_Private,work_type_Self_employed, work_type_children,
                            smoking_status_formerly_smoked, smoking_status_never_smoked, smoking_status_Smokes]])
        
        pred = model.predict(values)
    
        if pred == [1]:
            return st.write(f"OOps! There is high chances for stroke please consult to doctot ASAP!!")
                 
        else:
            return st.write(f"Congratulation! You don't have any stroke")
