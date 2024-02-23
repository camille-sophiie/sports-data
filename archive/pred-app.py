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

# Streamlit sidebar options
st.sidebar.title("Football Player Market Value Prediction")
selected_model_name = st.sidebar.selectbox("Select Model", list(models.keys()))
selected_features = {}

# Input fields for features
for feature in features:
    selected_features[feature] = st.sidebar.number_input(f'Enter {feature}', value=0.0)

# Convert the position to a one-hot encoded feature if necessary
# This is a placeholder for whatever encoding mechanism you're using for categorical features
def encode_position(position):
    # Implement the actual encoding logic based on your dataset
    return [0, 1]  # Example encoding

# Predicting the market value
if st.sidebar.button('Predict Market Value'):
    # Prepare the feature vector for prediction
    feature_vector = [selected_features[feature] for feature in features if feature != 'position']
    position_encoded = encode_position(selected_features['position'])
    feature_vector += position_encoded
    
    # Make the feature vector a 2D array for the model
    feature_vector = np.array(feature_vector).reshape(1, -1)
    
    # Select the model
    selected_model = models[selected_model_name]
    
    # Predict
    prediction = selected_model.predict(feature_vector)
    
    # Display the prediction
    st.write(f"Predicted Market Value: ${prediction[0]:,.2f}")

