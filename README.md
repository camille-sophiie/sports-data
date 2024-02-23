# Footballer Market Value Prediction

**Institution:** Hochschule Luzern (HSLU)

**Start date:** 02/05/2024  
**End date:** 02/09/2024

**People involved:**  
- Camille Mathilde Sophie Nigon  
  Contact: [camillemathildesophie.nigon@stud.hslu.ch](mailto:camillemathildesophie.nigon@stud.hslu.ch)
- Victor Anton  
  Contact: [victor.anton@stud.hslu.ch](mailto:victor.anton@stud.hslu.ch)
- Nicole Bolliger  
  Contact: [nicole.bolliger@stud.hslu.ch](mailto:nicole.bolliger@stud.hslu.ch)

**Software and versions:**  
- Python in Visual Studio Code 1.86.1  
- The app is located within the `streamlit-app` folder and is named `app.py`.

**Data:** 
- `players_filtered.csv`
- `apperances_filtered.csv`
- `cleaned_df.csv`  
  Found in the data folder.
  Data source: [Kaggle](https://www.kaggle.com/datasets/davidcariboo/player-scores)

**General purpose of experiment or processing:**  
This project is about predicting the market value of football players in the industry.

**Specific purpose of experiment or processing:**  
Analyzing factors that could influence the market value of players in the big 5 leagues. The project will focus on the 4 different positions (goalkeeper, defender, midfield, and striker) to determine which factors are influential in market value depending on the position.

**Installation:**  
For the modeling, ensure the following packages are installed:
- pandas
- os
- seaborn
- matplotlib
- sklearn
- statsmodels  
If not, install them using pip.

**Basic operation:**  
The app processes user input based on the player's position. A model is chosen accordingly and uses the factors provided by the user to calculate the market value.

**Resources:**  
- **Linear Regression:** Simple linear modeling technique assuming a linear relationship between features.
- **Ridge Regression:** Linear regression with regularization to prevent overfitting, suitable for multicollinear data.
- **Lasso Regression:** Linear regression with L1 regularization for feature selection, useful for models with many features.
- **Polynomial Regression:** Fits a polynomial function to the data, capturing non-linear relationships between features and target.
- **RandomForestRegressor:** Ensemble learning method using multiple decision trees for robust predictions.
- **GradientBoostingRegressor:** Ensemble method building predictive models in stages, minimizing errors iteratively.
- **SVR (Support Vector Regressor):** Utilizes support vector machine principles for regression tasks, mapping features to high-dimensional space.

# Instructions to run the streamlit app

## Prerequisites

Before running the app, ensure you have the following installed:

- Python 3.6 or higher
- pip (Python package installer)
- Streamlit


Install Streamlit using pip with the following command:

```bash
pip install streamlit
```

## Running the App

Follow these steps to run the app:

1. Open a terminal or command prompt.
2. Change directory to where `app.py` is located:



3. Execute the app with Streamlit:

```bash
streamlit run app.py
```

or alternatively

```bash
 python -m streamlit run test-app.py
 ```

Streamlit will start a server, and you should see the following:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

4. Open a browser and navigate to `http://localhost:8501` to view the app.

## Stopping the App

To stop the app, return to the terminal and press `Ctrl + C`.

## Troubleshooting
If you encounter any issues:

- Confirm app.py resides within the streamlit-app folder.
- Make sure you have installed all the necessary libraries. If you're unsure which libraries are needed, they are imported at the top of the app.py script. Install any that are missing using ```pip install library-name```.
- Make sure you're in the correct directory when running streamlit run app.py 
