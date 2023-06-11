# ML-Monitoring-System

## 1. Overview
- The Stroke Dataset Model is a powerful machine learning tool for stroke detection.
- Provides real-time predictions, aiding in early diagnosis and prompt medical intervention.
- Enhances diagnostic accuracy and optimizes time and cost efficiency.
- Enables personalized care, leading to improved patient outcomes in stroke management.

## 2. Motivation

- **Early Stroke Detection:** The model's accurate predictions aid in the early detection of strokes, enabling prompt medical intervention and potentially reducing the risk of long-term complications or disability.

- **Improved Diagnostic Accuracy:** By leveraging a comprehensive dataset and advanced machine learning techniques, the model enhances diagnostic accuracy, reducing the likelihood of misdiagnosis or missed cases.

- **Time and Cost Efficiency:** The real-time predictions and automated analysis provided by the model can optimize the efficiency of stroke diagnosis, saving time and resources for healthcare providers.

- **Personalized Care:** The Stroke Dataset Model takes into account individual patient characteristics and medical history, allowing for more personalized care and tailored treatment plans.

- **Research and Insights:** The dataset and model contribute to stroke research by providing a valuable resource for studying the risk factors, underlying mechanisms, and potential interventions related to strokes.

## 3. Success Metrics

**The success of the project will be measured based on the following metrics:**

- Accuracy, precision, recall, and F1 score of the machine learning models.
- User satisfaction and ease of use of the web application.
- Increased awareness and understanding of stroke risk factors among users.

## 4. Requirements & Constraints

### a. Functional Requirements

**The web application should provide the following functionality:**

- Users can input their health parameters, such as age, gender, hypertension, heart disease, smoking status, etc., to assess their risk of stroke.
- Users can view and interpret the predictions of the machine learning models, including the probability of stroke occurrence.
- Users can access educational resources and information about stroke prevention and risk factors.

### b. Non-functional Requirements

**The web application should meet the following non-functional requirements:**

- The machine learning models should demonstrate high accuracy and performance in stroke prediction.
- The web application should have an intuitive and user-friendly interface.
- The web application should ensure the privacy and security of user data.

### 5. Constraints

- The application should be built using Streamlit framework for the frontend and backend.
- Docker containers and Digital Ocean droplets should be used for deployment.
- The deployment cost should be minimized.

### Out-of-scope

**The following tasks are considered out of scope for this project:**

- Integration with electronic health records or real-time health monitoring devices.
- Providing personalized medical advice or treatment recommendations.

## 6. Methodology

### a. Problem Statement

The problem is to develop a machine learning model that predicts the risk of stroke based on health parameters provided by the user.

### b. Data

The dataset consists of anonymized health records of individuals, including features such as **age, gender, hypertension, heart disease, smoking status, and BMI.** The target variable is a binary label indicating whether the individual had a stroke or not.

### c. Techniques

**The project will utilize binary classification models to predict the risk of stroke. The following machine learning techniques will be employed:**

- Data preprocessing and cleaning.
- Feature engineering and selection.
- Model selection and training.
- Hyperparameter tuning.
- Model evaluation and testing.

## 7. Architecture

**The web application architecture consists of the following components:**

- Frontend web application built using Streamlit.
- Backend server built using Streamlit.
- Machine learning model for stroke prediction.
- Docker containers for running the frontend, backend, and model.
- Cloud infrastructure for hosting the application.

The frontend and backend components are both developed using Streamlit, enabling a seamless user interface and efficient data processing. The machine learning model is trained and deployed within a Docker container. The application is hosted on Digital Ocean droplets for scalability and reliability.

## 8. Pipeline

![Project Pipeline](pipeline.png)

**The project pipeline encompasses the following steps:**

- **Data collection:** The dataset, comprising anonymized health records, is used as input for model training and evaluation.
- **Data preprocessing:** The collected data undergoes cleaning, transformation, and feature engineering to prepare it for model training.
- **Model training:** The preprocessed data is used

 to train the machine learning model, optimizing it for stroke prediction.
- **Model evaluation:** The trained model is evaluated using appropriate metrics to assess its performance and accuracy.
- **Docker containerization:** The model and necessary application components are encapsulated within Docker containers for streamlined deployment.
- **Deployment:** The Docker containers, along with the frontend and backend components, are deployed on Digital Ocean droplets, making the application accessible to users.
- **Web application usage:** Users interact with the web application by inputting their health parameters and obtaining predictions regarding their stroke risk.
- **Results and recommendations:** The web application presents the predictions and offers educational resources and recommendations for stroke prevention.

## 9. Conclusion

The Stroke Prediction Web Application provides users with a convenient platform to assess their risk of stroke based on health parameters. By leveraging machine learning models and providing personalized insights, the application promotes stroke prevention and raises awareness about the risk factors associated with strokes.
