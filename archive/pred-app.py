import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Run the Streamlit app
if __name__ == "__main__":
    st.set_page_config(page_title="Football Player Market Value Predictor", layout="wide")
    st.title("Football Player Market Value Predictor")
    st.markdown("Select the desired machine learning model and enter the player's features to predict the market value.")

# Function to load a model
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Load your models
models = {
    "Ridge Regression": load_model(r'C:\cloudresume\react\resume\sports-data\code\04_streamlit_cami\RidgeRegression_model.pkl'),
    "Polynomial Regression": load_model(r'C:\cloudresume\react\resume\sports-data\code\04_streamlit_cami\PolynomialRegression_model.pkl'),
    "Linear Regression": load_model(r'C:\cloudresume\react\resume\sports-data\code\04_streamlit_cami\LinearRegression_model.pkl'),
    "Lasso Regression": load_model(r'C:\cloudresume\react\resume\sports-data\code\04_streamlit_cami\LassoRegression_model.pkl')
}

# Define features
features = [
    'number_games_played',
    'total_minutes',
    'avg_goals_per_game',
    'goals',
    'assists',
    'age',
    'avg_games_per_year',
    'avg_goals_per_year', 
    'position'
]


