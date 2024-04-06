import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from imblearn.over_sampling import RandomOverSampler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt
import time

def performance_analysis_body():
        st.write("### Performance Analysis")
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
        y_pred = rf_classifier.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        st.write(f"Using the Random Forest Classifier and dropping data accordingly, the model has an accuracy of {accuracy}")
