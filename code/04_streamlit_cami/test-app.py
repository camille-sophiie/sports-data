import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.express as px
import pickle

st.markdown("""
# Welcome to Our Football Market Value Prediction Project ⚽

## Project Introduction
Welcome! In this project, we aim to predict the market value of football players by analyzing a variety of features that influence a player's worth. Our analysis is based on a Kaggle dataset, meticulously curated to provide the most relevant factors affecting market values in the world of football.

## Exploratory Data Analysis (EDA)
The initial phase of our project is an in-depth Exploratory Data Analysis (EDA). Here's what you can expect:

- **Descriptive Statistics**: We summarize the central tendencies, dispersion, and shape of the dataset's distribution.
- **Data Visualizations**: Interactive charts and graphs that reveal underlying patterns and relationships.
- **Data Quality Checks**: Assessment of missing values, duplicate data, and outlier detection.
 ADD LEAGUES and other restrictions
---
""")

# Load the CSV files to df
cleaned_df = pd.read_csv(r'C:\cloudresume\react\resume\sports-data\data\cleaned_df.csv')

st.write("### Data Overview", cleaned_df.head())

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

import streamlit as st
import pandas as pd
import pickle
import os

# Define the path where the models are stored
MODEL_PATH = 'C:/cloudresume/react/resume/sports-data/models'

# Function to load the model and its components
def load_model_components(model_name):
    model_file = os.path.join(MODEL_PATH, f'{model_name}_model.pkl')
    X_imputer_file = os.path.join(MODEL_PATH, f'{model_name}_X_imputer.pkl')
    y_imputer_file = os.path.join(MODEL_PATH, f'{model_name}_y_imputer.pkl')

    with open(model_file, 'rb') as file:
        model = pickle.load(file)
    with open(X_imputer_file, 'rb') as file:
        X_imputer = pickle.load(file)
    with open(y_imputer_file, 'rb') as file:
        y_imputer = pickle.load(file)

    scaler = None
    if model_name in ['LinearRegression', 'RidgeRegression', 'LassoRegression', 'PolynomialRegression']:
        scaler_file = os.path.join(MODEL_PATH, f'{model_name}_scaler.pkl')
        with open(scaler_file, 'rb') as file:
            scaler = pickle.load(file)
    
    return model, X_imputer, y_imputer, scaler

# Streamlit app for interactive predictions
def main():
    st.title('Soccer Player Market Value Prediction')

    st.write("### Enter the player's details to predict the market value")

    # Model selection
    model_names = ['LinearRegression', 'RidgeRegression', 'LassoRegression',
                   'PolynomialRegression', 'RandomForestRegressor', 'GradientBoostingRegressor', 'SVR']
    selected_model_name = st.selectbox('Select a model for prediction:', model_names)

    # Load the selected model and components
    model, X_imputer, y_imputer, scaler = load_model_components(selected_model_name)

    # Define the input fields
    input_data = {
        'age': st.number_input('Age', min_value=15, max_value=40, value=25, step=1),
        'goals': st.number_input('Goals', min_value=0, value=0, step=1),
        'assists': st.number_input('Assists', min_value=0, value=0, step=1),
        'total_minutes': st.number_input('Total Minutes Played', min_value=0, value=0, step=1),
        'number_games_played': st.number_input('Number of Games Played', min_value=0, value=0, step=1),
        'avg_goals_per_game': st.number_input('Average Goals per Game', min_value=0.0, value=0.0, step=0.1),
        'avg_assists_per_year': st.number_input('Average Assists per Year', min_value=0.0, value=0.0, step=0.1)
    }

    # Button to make prediction
    if st.button('Predict Market Value'):
        input_df = pd.DataFrame([input_data])
        
        # Apply imputation
        input_df = pd.DataFrame(X_imputer.transform(input_df), columns=input_df.columns)
        
        # Apply scaling if necessary
        if scaler is not None:
            input_df = scaler.transform(input_df)
        
        # Predict and display the result
        prediction = model.predict(input_df)[0]
        st.success(f"The predicted market value is: ${prediction:,.2f}")

if __name__ == "__main__":
    main()