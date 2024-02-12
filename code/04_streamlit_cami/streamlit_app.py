import streamlit as st
import pickle
import numpy as np
from sklearn.datasets import load_iris
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

# Load the trained model
with open('iris_decision_tree.pkl', 'rb') as file:
    clf = pickle.load(file)

# Load Iris dataset for feature names and class names
iris = load_iris()

# Streamlit app title
st.title('Iris Decision Tree Classifier')

# Function to plot and visualize the tree
def plot_decision_tree(clf, feature_names, class_names):
    plt.figure(figsize=(16, 10))
    plot_tree(clf, filled=True, feature_names=feature_names, class_names=class_names)
    st.pyplot(plt)

# Function to accept user input
def user_input_features():
    sepal_length = st.slider('Sepal length', float(iris.data[:, 0].min()), float(iris.data[:, 0].max()), float(iris.data[:, 0].mean()))
    sepal_width = st.slider('Sepal width', float(iris.data[:, 1].min()), float(iris.data[:, 1].max()), float(iris.data[:, 1].mean()))
    petal_length = st.slider('Petal length', float(iris.data[:, 2].min()), float(iris.data[:, 2].max()), float(iris.data[:, 2].mean()))
    petal_width = st.slider('Petal width', float(iris.data[:, 3].min()), float(iris.data[:, 3].max()), float(iris.data[:, 3].mean()))
    return np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Main function to control the app
def main():
    st.sidebar.header('User Input Parameters')
    input_features = user_input_features()

    if st.button('Predict'):
        prediction = clf.predict(input_features)
        st.subheader('Prediction')
        st.write(iris.target_names[prediction][0])

    if st.button('Show Decision Tree'):
        plot_decision_tree(clf, iris.feature_names, iris.target_names)

if __name__ == '__main__':
    main()