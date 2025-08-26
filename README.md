# Credit Scoring Model:

This project is the part of my intership project at codeAlpha.tech.
This project is based on the Logistic Regression ML algorithm to classify the individual as creditworthy or not creditworthy based on its past financial records.

### Project Overview

This project is a Credit Scoring System built using Python and machine learning.
It predicts whether an individual is creditworthy based on financial attributes such as income, expenses, savings, debt ratio, and credit score.

A Streamlit app provides a simple web interface to enter user data and get instant predictions.

## Features

--Predicts creditworthiness (creditworthy / not creditworthy) using a trained ML model.

--Accepts user inputs through a Streamlit interface.

--Shows warning messages if the inputs are outside the range of training data.

--Easy to extend with additional features or models.

## usage
you can clone the repository and then run the app.py file . The streamlit app will run on your local machine(on browser) where you can enter the values and find the prediction

## Important Notes

--Predictions are most reliable for values similar to the training data.
--Extreme or unrealistic inputs may lead to unreliable predictions.
--Make sure credit_scoring_model.pkl is present in src/.

## Dependencies

--Python 3.10+
--numpy
--pandas
--scikit-learn
--joblib
--streamlit
