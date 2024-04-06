import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split


def loan_acceptance_body():

    st.write("### Loan Acceptance")
    st.info("Fill in form to receive loan acceptance prediction.")

    loan_data = pd.read_csv("outputs/loan_data.csv")

    # Drop rows with NaN values
    loan_data_drop = loan_data.dropna()

    loan_data_drop['Married'] = loan_data_drop['Married'].map({'No': 0, 'Yes': 1})
    loan_data_drop['Gender'] = loan_data_drop['Gender'].map({'Female': 0, 'Male': 1})
    loan_data_drop['Education'] = loan_data_drop['Education'].map({'Not Graduate': 0, 'Graduate': 1})
    loan_data_drop['Self_Employed'] = loan_data_drop['Self_Employed'].map({'No': 0, 'Yes': 1})
    loan_data_drop['Property_Area'] = loan_data_drop['Property_Area'].map({'Rural': 0, 'Semiurban': 1, 'Urban': 2})
    loan_data_drop['Loan_Status'] = loan_data_drop['Loan_Status'].map({'N': 0, 'Y': 1})
    loan_data_drop['Dependents'] = loan_data_drop['Dependents'].map({'0': 0, '1' : 1, '2': 1, '3+': 2})

    # Apply random oversampling to balance the loan status
    loan_data_drop.drop(columns=['Loan_ID'], inplace=True)
    X = loan_data_drop.drop(columns=['Loan_Status'])
    y = loan_data_drop['Loan_Status']
    X_resampled, y_resampled = RandomOverSampler(random_state=42).fit_resample(X, y)
    loan_data_drop = pd.concat([pd.DataFrame(X_resampled),
                                pd.DataFrame(y_resampled,columns=['Loan_Status'])], axis=1)
    
    # Split the data into features and target
    X = loan_data_drop.drop(columns=['Loan_Status'])
    y = loan_data_drop['Loan_Status']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    rf_classifier = RandomForestClassifier()
    rf_classifier.fit(X_train, y_train)


    Gender = st.selectbox('Gender', ['Male', 'Female'])
    Married = st.selectbox('Married', ['Yes', 'No'])
    Dependents = st.selectbox('Dependents', ['0', '1', '2', '3+'])
    Education = st.selectbox('Education', ['Graduate', 'Not Graduate'])
    Self_Employed = st.selectbox('Self Employed', ['Yes', 'No'])
    Applicant_Income = st.number_input('Applicant Income', min_value=0)
    Coapplicant_Income = st.number_input('Coapplicant Income', min_value=0)
    Loan_Amount = st.number_input('Loan Amount', min_value=0)
    Loan_Amount_Term = st.number_input('Loan Amount Term', min_value=0)
    Credit_History = st.selectbox('Credit History', ['0.0', '1.0'])
    Property_Area = st.selectbox('Property Area', ['Rural', 'Semiurban', 'Urban'])

    if st.button('Submit'):
        # Convert input values to numerical format
        Gender = 1 if Gender == 'Male' else 0
        Married = 1 if Married == 'Yes' else 0
        Education = 1 if Education == 'Graduate' else 0
        Self_Employed = 1 if Self_Employed == 'Yes' else 0
        Property_Area = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}[Property_Area]
        Dependents = {'0': 0, '1' : 1, '2': 1, '3+': 2}[Dependents]
        Credit_History = float(Credit_History)

        # Make predictions using the trained classifier
        prediction = rf_classifier.predict([[Gender, Married, Dependents, Education, Self_Employed, Applicant_Income, Coapplicant_Income, Loan_Amount, Loan_Amount_Term, Credit_History, Property_Area]])

        # Display the predictions
        st.write("Predicted Loan Status:", 'Loan Accepted' if prediction[0] == 1 else 'Loan Rejected')