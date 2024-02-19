from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import pickle
import streamlit as st
import os
import pandas as pd

# Define the new working directory path
new_working_directory = r'\Users\e904176\Documents\GitHub\sports-data\data'

# Change the current working directory
os.chdir(new_working_directory)

# Assuming you have already loaded your dataframe as df_cleaned
df_cleaned = pd.read_csv(new_working_directory+'\cleaned_df.csv')

# Load the model and transformer
model = pickle.load(open('linear_regression_model.pkl', 'rb'))
transformer = pickle.load(open('transformer.pkl', 'rb'))

# Streamlit app layout
st.title('Footballer Market Value Prediction')

# Add inputs for the features
country = st.selectbox('Country', options=df_cleaned['country'].unique())
height = st.number_input('Height (in cm)')
foot = st.selectbox('Preferred Foot', options=df_cleaned['foot'].unique())
position = st.selectbox('Position', options=df_cleaned['position'].unique())

# Predict button
if st.button('Predict Market Value'):
    # Process the input data in the same way as the training data
    input_data = pd.DataFrame([[country, height, foot, position]],
                              columns=['country', 'height', 'foot', 'position'])
    
    input_transformed = transformer.transform(input_data)
    
    # Predict the market value
    prediction = model.predict(input_transformed)
    st.write(f'Predicted Market Value: €{prediction[0]:,.2f}')
