import streamlit as st
import pandas as pd
import pickle

# Load your models and imputers (adjust the file paths as necessary)
model_path_dict = {
    'Model 1': r'C:\cloudresume\react\resume\sports-data\models\LinearRegression_model.pkl',
    # Add more models if you have them
}


models = {name: pickle.load(open(path, 'rb')) for name, path in model_path_dict.items()}

# Streamlit app
def main():
    st.title('Football Player Market Value Prediction')

    # Allow the user to select a model
    model_name = st.selectbox('Select Model', list(models.keys()))

    # User inputs
    input_data = {
        'age': st.number_input('Age', min_value=15, max_value=40, value=25, step=1),
        'goals': st.number_input('Goals', min_value=0, value=0, step=1),
        'assists': st.number_input('Assists', min_value=0, value=0, step=1),
        'total_minutes': st.number_input('Total Minutes Played', min_value=0, value=0, step=1),
        'number_games_played': st.number_input('Number of Games Played', min_value=0, value=0, step=1),
        'avg_goals_per_game': st.number_input('Average Goals per Game', min_value=0.0, value=0.0, step=0.1),
        'avg_assists_per_year': st.number_input('Average Assists per Year', min_value=0.0, value=0.0, step=0.1)
    }
    
    # Convert user inputs into a DataFrame
    input_df = pd.DataFrame([input_data])

    # Make prediction button
    if st.button('Predict Market Value'):
        # Load the selected model
        model = models[model_name]
        
        # Make prediction
        prediction = model.predict(input_df)

        # Display the prediction
        st.write(f"The predicted market value of the player is: {prediction[0]}")

if __name__ == "__main__":
    main()