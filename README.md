# Footballer Market value Prediction
*** Institution: Hochschule Luzern (HSLU)
*** Start date ( 02/05 2024/ ), end date (02 /09 /2024 )
*** People involved: Camille Mathilde Sophie Nigon, Victor Anton, Nicole Bolliger
Contact: camillemathildesophie.nigon@stud.hslu.ch, victor.anton@stud.hslu.ch, nicole.bolliger@stud.hslu.ch 
*** Software and versions: Python in Visual Studio Code 1.86.1
*** Data: found in data folder players_filtered.csv, apperances_filtered.csv and cleaned_df.csv
*** General purpose of experiment or processing: This project is about the market value of the football industry.
*** Specific purpose of experiment or processing:In the big 5 leagues we see high market values. With the following project it should be analyzed what factors could influence the market value of the players. In order to analyze the market value we look at the 4 different positions (goalkeeper, defender, midfield and striker) to see which factors play a role in the market value depending on the factors.
*** Installation: pandas, os, seaborn, matplotlib, sklearn, statsmodels, if not install it using pip
*** Basic operation: The app will process the user input based on the position of the player a model is chosen. Based on the factors provided by the user the market value is calculated.
*** Resources: Linear Regression: simple linear modeling technique assuming relationship is linear between the features
	Ridge Regression: Linear regression with regularization to prevent overfitting, suitable for multicollinear data.
	Lasso Regression: Linear regression with L1 regularization for feature selection, useful for models with many features.
	Polynomial Regression: Fits a polynomial function to the data, capturing nonlinear relationships between features and target.
	RandomForestRegressor: Ensemble learning method using multiple decision trees for robust predictions.
	GradientBoostingRegressor: Ensemble method building predictive models in stages, minimizing errors iteratively.
	SVR (Support Vector Regressor): Utilizes support vector machine principles for regression tasks, mapping features to high-dimensional space.







## Project Overview
This project is about market value prediction in the football industry. 

## Dataset

## Methodology

## Tools & Technologies


Notes from Lecturer

- Linear regression
- Wichtige features
- Kleines Programm, Analyse 
- je weniger unanbhängige Variable, desto besser
--> variable shouldn't be correlated
--> welche variable predicten am besten

Further Notes:
market value of football player

multiple (lin.) regression  (wahrscheinlich nicht linear)

zuerst schauen- ich habe gefühl dieser faktor hat einfluss

am schluss interaktives program/dashboard wo man parameter kann setzen
	-> eingabemaske und return eine Zahl/Intervall


1. Schritt
exploren wie Daten verteilt sind (scatterplot machen)
korrelation rechnen (wenn tief bedeuted nicht nicht verknüpft sondern nicht linear verknüpft) -> Mutual information


abhängig: Marktwert
unabhängig: {x1,x2,...}


einmal 10 unabhängige variablen raussuchen und dann kombinationen ausprobieren -> korrelationmatrix (unabhängige variablen müssen möglichst unkorreliert sein), Regressionsmodell aufstellen immer nur mit einer variablen, welche variablen predicten alleine gut und sind nicht untereinander korreliert


Analyse für jede position machen (Goalie, Defender, Midfield, Striker)


können auch indexe bilden  

Wichtig: Gutes Story Telling (erklären ist es counter intuitiv oder eine Beobachtung welche bestätigt wurde)

Application z.B. Shiny

Position wählen und dann wird anderes Regressionsmodell gebraucht

Notzen Cami

- Cleaning 
--> restrict die Liga, aber nicht die Jahren
--> Features current_club_domestic_competition id 
--> Scatter plot, EDA 
# welche Zeitperiode
# Fragestellung: market value faktoren, Unterschiede Big 5 Liga, Faktorenanalyse (welche faktoren steuern die variabilität des Marktwerter ) 
#unabhangige vs abhangige FAktoren, mögliche korrelation, wenn hohe korrelation zusammenrechnen (nur unabhängige variablen), Scatterplot
# Position unterscheiden hallo  f


to do Cami: 
- market value vs highest market value (nur market value im dataset)

