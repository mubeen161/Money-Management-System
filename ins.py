import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import webbrowser

def load_data():
    # Sample data (replace this with your actual dataset)
    data = {
        'Risk Exposure': ['High', 'Medium', 'Low', 'High', 'Medium', 'Low'],
        'Financial Situation': ['Stable', 'Variable', 'Stable', 'Variable', 'Stable', 'Stable'],
        'Lifestyle and Occupation': ['Professional', 'Entrepreneur', 'Corporate', 'High-risk Job', 'Retired', 'Service Industry'],
        'Family Composition': ['Family with Children', 'Single', 'Empty Nesters', 'Family with Children', 'Single', 'Family with Children'],
        'Asset Portfolio': ['Homeownership', 'Halal Investments', 'Vehicle Ownership', 'Property Ownership', 'Islamic Principles', 'Savings and Investments'],
        'Islamic Principles': ['Sharia Compliant', 'Halal Investments', 'Islamic Principles', 'Sharia Compliant', 'Sharia-compliant Investments', 'Halal Savings'],
        'Insurance Name': [
            'Student Insurance',
            'Car Insurance',
            'Home Insurance',
            'Travel Insurance',
            'Health Insurance',
            'Business Insurance'
        ],
        'Insurance Link': [
            'https://www.shariabanking.com/islamic-student-insurance.html',
            'https://www.shariabanking.com/islamic-car-insurance.html',
            'https://www.shariabanking.com/islamic-home-insurance.html',
            'https://www.shariabanking.com/islamic-travel-insurance.html',
            'https://www.shariabanking.com/islamic-health-insurance.html',
            'https://www.shariabanking.com/islamic-business-insurance.html'
        ]
    }

    return pd.DataFrame(data)

def train_model(data):
    # Convert categorical variables to numerical using one-hot encoding
    df = pd.get_dummies(data, columns=['Risk Exposure', 'Financial Situation', 'Lifestyle and Occupation', 'Family Composition', 'Asset Portfolio', 'Islamic Principles'])

    # Separate features and target variable
    X = df.drop(['Insurance Name', 'Insurance Link'], axis=1)
    y = df[['Insurance Name', 'Insurance Link']]

    # Build a decision tree classifier
    model = DecisionTreeClassifier()
    model.fit(X, y['Insurance Name'])

    return model, df

def main():
    st.title('Insurance Prediction App')

    user_input = {}
    for feature in ['Risk Exposure', 'Financial Situation', 'Lifestyle and Occupation', 'Family Composition', 'Asset Portfolio', 'Islamic Principles']:
        user_input[feature] = st.selectbox(f'Select {feature}', [''] + data[feature].unique())

    if st.button('Predict'):
        user_df = pd.DataFrame([user_input])
        user_df = pd.get_dummies(user_df, columns=['Risk Exposure', 'Financial Situation', 'Lifestyle and Occupation', 'Family Composition', 'Asset Portfolio', 'Islamic Principles'])
        user_df = user_df.reindex(columns=df.drop(['Insurance Name', 'Insurance Link'], axis=1).columns, fill_value=0)

        prediction = model.predict(user_df)
        predicted_link = df[df['Insurance Name'] == prediction[0]]['Insurance Link'].values[0]
        webbrowser.open_new_tab(predicted_link)

        st.success(f'Predicted Insurance Name: {prediction[0]}')
        st.success(f'Insurance Link: {predicted_link}')

if __name__ == '__main__':
    data = load_data()
    model, df = train_model(data)
    main()