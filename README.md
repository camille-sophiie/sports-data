# Footballer Market Value Prediction

**Institution:** Hochschule Luzern (HSLU)

**Start date:** 02/05/2024  
**End date:** 02/09/2024

**People involved:**  
- Camille Nigon  
  Contact: [camillemathildesophie.nigon@stud.hslu.ch](mailto:camillemathildesophie.nigon@stud.hslu.ch)
- Victor Anton  
  Contact: [victor.anton@stud.hslu.ch](mailto:victor.anton@stud.hslu.ch)
- Nicole Bolliger  
  Contact: [nicole.bolliger@stud.hslu.ch](mailto:nicole.bolliger@stud.hslu.ch)

**Software and versions:**  
- Python in Visual Studio Code 

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
If not, install them or additional libraries using pip.

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

# Sports Data Streamlit Application

We are excited to share our new Streamlit application that allows users to interact with our carefully curated dataset. Our team has implemented a Ridge Regression model to power the predictive features of the application.

## Accessing the Application

To get started with the app, please visit the following URL:

[https://sports-data.streamlit.app/](https://sports-data.streamlit.app/)

## Viewing Requirements

For the best experience, we recommend using a desktop web browser. This ensures that all features and visualizations are displayed correctly and interactively.

## JavaScript Requirement

**Important:** You need to enable JavaScript in your web browser to run this app. JavaScript is essential for the dynamic and interactive elements of the Streamlit application to function properly.

## How to Enable JavaScript

If you're not sure how to enable JavaScript in your browser, follow these general steps (note that instructions may vary slightly depending on your browser version and type):

1. Open your web browser settings.
2. Look for the "Privacy" or "Security" settings.
3. Find the section that includes JavaScript settings.
4. Ensure that JavaScript is allowed/turned on for the website.

