import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import matplotlib.pyplot as plt
import os

# Load your trained model
model = load('ridge_regression_model.pkl')

# Load your dataset (for the box plot)
# Ensure your dataset CSV file is in the same directory as this script, or provide the full path.

# Load the CSV files to df
df = pd.read_csv('cleaned_df.csv')

# Define the layout of your app
st.title('Market Value Prediction App')

# Create user input fields
st.header('Enter the player details:')
number_games_played = st.number_input('Number of Games Played', min_value=0)
total_minutes = st.number_input('Total Minutes', min_value=0)
avg_goals_per_game = st.number_input('Average Goals per Game', min_value=0.0, format="%.2f")
goals = st.number_input('Goals', min_value=0)
assists = st.number_input('Assists', min_value=0)
age = st.number_input('Age', min_value=0)
avg_games_per_year = st.number_input('Average Games per Year', min_value=0)
avg_goals_per_year = st.number_input('Average Goals per Year', min_value=0.0, format="%.2f")
position_options = ['Goalkeeper', 'Defender', 'Midfielder', 'Forward']  # Update with your positions
position = st.selectbox('Position', position_options)

# Predict market value
if st.button('Predict Market Value'):
    # Create a DataFrame with the input features
    input_data = pd.DataFrame([[
        number_games_played,
        total_minutes,
        avg_goals_per_game,
        goals,
        assists,
        age,
        avg_games_per_year,
        avg_goals_per_year,
        position
    ]], columns=[
        'number_games_played',
        'total_minutes',
        'avg_goals_per_game',
        'goals',
        'assists',
        'age',
        'avg_games_per_year',
        'avg_goals_per_year',
        'position'
    ])
    
    # Get the prediction
    prediction = model.predict(input_data)
    
    # Ensure prediction is not negative
    prediction = max(prediction, [0])

    # Display the prediction
    st.write(f"The predicted market value is: ${max(prediction[0], 0):,.2f}")

    # Display a box plot for the market value distribution and the predicted point
    fig, ax = plt.subplots()
    ax.boxplot(df['highest_market_value'])  # Replace with your actual target variable name
    ax.scatter(1, prediction, color='red')  # Plot the predicted value on the boxplot
    st.pyplot(fig)