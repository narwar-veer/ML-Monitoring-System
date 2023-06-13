#!/usr/bin/env python
# coding: utf-8

# # Stroke Prediction Model

# #### Importing the required dependencies

# In[1]:


import pandas as pd
import numpy as np
import pickle


# In[2]:


# for displaying all feature from dataset:
pd.pandas.set_option('display.max_columns', None)


# #### Importing the Preprocessed dataset 

# In[4]:


# Reading Dataset:
df = pd.read_csv("preprocessed_data.csv")


# #### Let's have a look on the data

# In[5]:


df.head(5)


# **Attribute Information**
# 
# - id: unique identifier
# - gender: "Male", "Female" or "Other"
# - age: age of the patient
# - hypertension: 0 if the patient doesn't have hypertension, 1 if the patient has hypertension
# - heart_disease: 0 if the patient doesn't have any heart diseases, 1 if the patient has a heart disease
# - ever_married: "No" or "Yes"
# - work_type: "children", "Govt_jov", "Never_worked", "Private" or "Self-employed"
# - Residence_type: "Rural" or "Urban"
# - avg_glucose_level: average glucose level in blood
# - bmi: body mass index
# - smoking_status: "formerly smoked", "never smoked", "smokes" or "Unknown"*
# - stroke: 1 if the patient had a stroke or 0 if not
# 
# *Note: "Unknown" in smoking_status means that the information is unavailable for this patient*

# In[6]:


# Dataset size
df.shape


# In[7]:


# Description of  the dataset
df.describe()


# #### Separating the dependent and independent variables 

# In[8]:


# Dependent & Independent Feature:
X = df.iloc[:, :-1]
y = df.iloc[:, -1]


# In[9]:


# Over Sampling:
from imblearn.over_sampling import RandomOverSampler

oversampler = RandomOverSampler(sampling_strategy=0.4)
x_oversampler, y_oversampler = oversampler.fit_resample(X, y)


# #### Train Test Splitting of the dataset

# In[10]:


# Train Test Split:
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x_oversampler,y_oversampler, test_size=0.2, random_state=0)


# ### Now its time to apply and fit ML model

# In[11]:


# RandomForestClassifier:

from sklearn.ensemble import RandomForestClassifier
RandomForest = RandomForestClassifier()
RandomForest = RandomForest.fit(X_train,y_train)


# #### Creating a pickle file for the classifier

# In[12]:


filename = 'stroke.pkl'
pickle.dump(RandomForest, open(filename, 'wb'))


# In[ ]:




