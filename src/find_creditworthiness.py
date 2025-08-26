import pandas as pd
import joblib

model = joblib.load('src/credit_scoring_model.pkl')

def find_creditworthy(model, new_data):
    missing_col = set(model.feature_names_in_) - set(new_data.columns)
    if missing_col:
        raise ValueError(f"Missing columns in input data: {missing_col}")
    new_data = new_data[model.feature_names_in_]
    predicted_class = model.predict(new_data)
    return predicted_class

d = pd.DataFrame({
    'monthly_income': [34557],
    'monthly_expense_total': [3456],
    'savings_rate': [78],
    'credit_score': [456],
    'debt_to_income_ratio': [5.7],
    'financial_advice_score': [34]
})

result = find_creditworthy(model, d)
print(result)
