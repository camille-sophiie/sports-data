import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pickle
import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
import matplotlib.pyplot as plt
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error, r2_score
import plotly

st.markdown("""
# Welcome to Our Football Market Value Prediction Project ⚽

## Project Introduction
Welcome! In this project, we aim to predict the market value of football players by analyzing a variety of features that influence a player's worth. Our analysis is based on a Kaggle dataset, meticulously curated to provide the most relevant factors affecting market values in the world of football.


""")

# Load the CSV files to df
cleaned_df = pd.read_csv('cleaned_df.csv')

st.write("### Data Overview", cleaned_df.head())
# Text input for the search query
search_query = st.text_input("Enter a name to search:")

# Display the full DataFrame if the search query is empty
if search_query == "":
    st.dataframe(cleaned_df.head())  # Show only the first few rows using .head()
else:
    # Filter the DataFrame based on the search query in the 'name' column
    filtered_df = cleaned_df[cleaned_df['name'].str.contains(search_query, case=False, na=False)]

    # Display the filtered DataFrame
    st.dataframe(filtered_df)
def main():
    st.title('Interactive Scatter Plot')

    # Sidebar for user input:
    # User can select the x-axis for the scatter plot from dataframe columns
    x_axis_options = cleaned_df.columns.tolist()
    x_axis = st.sidebar.selectbox('Select the x-axis for the scatter plot:', x_axis_options)

    # Sidebar for position filter
    unique_positions = cleaned_df['position'].unique()
    selected_positions = st.sidebar.multiselect('Select position(s):', unique_positions, default=unique_positions)

    # Filter dataframe by selected positions
    filtered_df = cleaned_df[cleaned_df['position'].isin(selected_positions)]

    # Create a Plotly Express scatter plot
    fig = px.scatter(filtered_df, x=x_axis, y='highest_market_value',
                     color="position", hover_data=['name', 'country', 'height', 'foot', 'position', 'goals', 'assists', 'age'])
    
    # Update layout if desired
    fig.update_layout(
        title=f'Scatter Plot of Market Value vs. {x_axis}',
        xaxis_title=x_axis,
        yaxis_title='Highest Market Value'
    )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)
       

if __name__ == '__main__':
    main()




# Assuming you have the 'cleaned_df' DataFrame available with the correct data.

# Function to create the interactive heatmap
def create_interactive_heatmap(df):
    corr_matrix = df.corr()
    fig = px.imshow(
        corr_matrix,
        labels=dict(color="Correlation Coefficient"),
        x=corr_matrix.columns,
        y=corr_matrix.columns,
        text_auto=True,
        color_continuous_scale=px.colors.diverging.RdBu,
        aspect="auto"
    )
    fig.update_xaxes(side="bottom")
    fig.update_layout(
        title="Correlation Matrix Heatmap",
        coloraxis_colorbar={
            'title':'Correlation Coefficient'
        },
    )
    return fig

# Main function to run the Streamlit app
def main():
    st.title('Soccer Players Performance Heatmap')
    
    # List of dimensions suitable for the heatmap
    dimensions = [
        'height',
        'highest_market_value',
        'number_games_played',
        'total_minutes',
        'red_cards_sum',
        'red_cards_avg',
        'goals',
        'avg_goals_per_game',
        'assists',
        'age',
        'avg_games_per_year',
        'avg_goals_per_year',
        'avg_assists_per_year'
    ]

    # Make sure to filter the DataFrame to only include the specified dimensions
    heatmap_data = cleaned_df[dimensions]

    # Create the heatmap
    fig = create_interactive_heatmap(heatmap_data)

    # Display the heatmap in Streamlit
    st.plotly_chart(fig, use_container_width=True)

if __name__ == "__main__":
    main()


# Load  model
model = load('ridge_regression_model.pkl')


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