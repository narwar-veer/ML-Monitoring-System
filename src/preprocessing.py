#!/usr/bin/env python
# coding: utf-8

# # Stroke Data Preprocessing

# #### Importing the required dependencies!

# In[184]:


# Importing Libraries:
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler, OneHotEncoder, LabelEncoder
from sklearn.impute import SimpleImputer
from sklearn.decomposition import PCA
from sklearn_pandas import DataFrameMapper

from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

print("Libraries Imported without any error")


# #### It's time to import the dataset

# In[185]:


df= pd.read_csv('test_strokes.csv')


# Stroke dataset has been imported!
# 

# #### Now Let's Have a Look on the Imported Data!

# In[186]:


df.head()


# In[187]:


df.shape


# Given Data has ->
# Rows: 5110 , 
# Columns: 12

# In[188]:


df.info()


# This function gives us information about the datatype of the existing columns

# #### Dropping the unnecessary feature (column):

# In[189]:


df = df.drop('id',axis=1)


# In[190]:


print(df.shape)
df.head()


# We ahve successfully dropped the 'id' column

# In[191]:


# Checking for any null (NaN) values:

df.isnull().sum()


# So, this dataset has only Null values present in 'bmi' Column

# #### Filling the NaN Values in BMI feature with the mean values 

# In[192]:


df['bmi'] = df['bmi'].fillna(df['bmi'].median())
df['smoking_status'].fillna('Unknown', inplace=True)
df.isnull().sum()


# Now, We can see all the Null values has been filled with some numerical values

# #### Target Featuring

# In[193]:


print("Stroke People     : ", df['stroke'].value_counts()[1])
print("Non-Stroke People : ", df['stroke'].value_counts()[0])


# * By seeing target feature, We clearly say we have **imbalanced dataset.**

# In[194]:


# Gender
df['gender'].value_counts()


# We Seen that in our **Gender feature**, we have only one **Other** gender, So instead of taking we **drop** that record.

# In[195]:


other_gender_indices = df[df['gender'] == 'Other'].index

if len(other_gender_indices) > 0:
    other_gender = other_gender_indices[0]
    df = df.drop(other_gender, axis=0)
else:
    print("No rows found with gender 'Other'")
    
df['gender'].value_counts()


# We can clearly see that other value has been removed

# In[196]:


# Gender:
print("Male    : ", df['gender'].value_counts()[1])
print("female  : ", df['gender'].value_counts()[0])


# In[197]:


# Rename some names in smokers feature for simplacity nothing else:
df.replace({'never smoked':'never_smoked', 'formerly smoked':'formerly_smoked'}, inplace=True)


# In[198]:


df.head()
df.info()


# In[199]:


num_features = df.select_dtypes(exclude=['object']).columns
num_features


# In[200]:


num_pipeline = Pipeline([('impute', SimpleImputer(strategy='mean'))])


# In[201]:


cat_features = df.select_dtypes(include =['object']).columns
cat_features


# In[202]:


cat_pipeline = Pipeline([
    ('Label', DataFrameMapper([(cat_features, OneHotEncoder(drop='first'))]))
])


# In[205]:


preprocess_pipeline = ColumnTransformer ([('categorical',cat_pipeline,cat_features),
                                         ('numerical',num_pipeline,num_features)])


# In[206]:


processed = preprocess_pipeline.fit(df)


# In[208]:


# df = cat_pipeline.fit_transform(df)
clean_data= pd.DataFrame(processed.transform(df),columns = df.columns)
# processed


# In[183]:


cat_columns = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
num_columns = ['age', 'hypertension', 'heart_disease', 'avg_glucose_level', 'bmi']

# Create transformers for categorical and numerical columns
cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='most_frequent')),
    ('onehot', OneHotEncoder(drop='first', sparse=False))
])

num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('scaler', StandardScaler())
])

# Create the column transformer
preprocessor = ColumnTransformer(transformers=[
    ('cat', cat_transformer, cat_columns),
    ('num', num_transformer, num_columns)
])

# Get the transformed feature names
transformed_feature_names = list(preprocessor.named_transformers_['cat']['onehot'].get_feature_names(cat_columns)) \
                           + num_columns

# Apply the pipeline to the dataset and create the transformed DataFrame
df_encoded = pd.DataFrame(preprocessor.fit_transform(df), columns=transformed_feature_names)


# In[81]:


# One Hot Encoding:
df = pd.get_dummies(df, drop_first=True)


# In[164]:


df_encoded.head()


# In[32]:


df.columns


# In[83]:


# Rearranging the columns for better understanding
df = df[['gender_Male','age', 'hypertension', 'heart_disease', 'ever_married',
       'Residence_type', 'avg_glucose_level', 'bmi', 
       'work_type_Never_worked', 'work_type_Private','work_type_Self-employed', 'work_type_children','smoking_status_formerly_smoked', 'smoking_status_never_smoked','smoking_status_smokes','stroke']]


# In[23]:


df.head()


# In[25]:


df.to_csv('test_data.csv', index=False)


# # We have done with the preprocesing of the dataset.
# 
# # Now in the notebook we'll do EDA and see data visually

# In[ ]:




