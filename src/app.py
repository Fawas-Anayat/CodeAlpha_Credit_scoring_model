import streamlit as st
import pandas as pd
import joblib
model=joblib.load('src/credit_scoring_model.pkl')
st.title('The Credit Scoring ML Model')
min_value_income=600
max_value_income=8000
monthly_income=st.number_input('Monthly Income')
if monthly_income < min_value_income or monthly_income > max_value_income:
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 600-8000')
min_expenses=150
max_expenses=6000
total_monthly_expense=st.number_input('Total Monthly Expense')
if total_monthly_expense <min_expenses or total_monthly_expense>max_expenses:
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 150-6000')
min_saving=0.05
max_saving=0.5
savings_rate=st.number_input('Savings rate')
if savings_rate<min_saving or savings_rate > max_saving:
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 0.05-0.5')
min_credit_score=500
max_credit_score=900
credit_score=st.number_input('credit score')
if credit_score <min_credit_score or credit_score >max_credit_score:
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 500-900 ')
min_DTI=0.1
mix_DTI=0.6
DTI_ratio=st.number_input('debt to income ratio')
if DTI_ratio <min_DTI or DTI_ratio> mix_DTI:
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 0.1-0.6')
min_FAR=0.1
max_FAR=100
FAR=st.number_input('financial advice score')
if FAR < min_FAR or FAR > max_FAR :
    st.warning('This data is out of range of the training data of the model.The results may be unrelaible.For relaible results enter the value between 0.1-100')

d = pd.DataFrame({
    'monthly_income': [monthly_income],
    'monthly_expense_total': [total_monthly_expense],
    'savings_rate': [savings_rate],
    'credit_score': [credit_score],
    'debt_to_income_ratio': [DTI_ratio],
    'financial_advice_score': [FAR]
})

if st.button('Check creditworthness'):
    pred=model.predict(d)
    st.write("Creditworthy" if pred==1 else "Not Creditworthy")
    