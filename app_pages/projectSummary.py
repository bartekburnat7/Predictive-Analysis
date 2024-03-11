import streamlit as st
import time

def page_summary_body():

    st.write("### Project Summary")

    st.info(
        f"**Introducing the Loan Approval Prediction System**\n"
        f"* The Loan Approval Prediction System is a groundbreaking tool designed to assist financial institutions and individuals in forecasting loan approval outcomes with precision and efficiency.\n"
        f"* This innovative system focuses on analyzing various financial and personal data points to determine the likelihood of a loan application being accepted.\n"
        f"* By utilizing state-of-the-art algorithms, our system can assess factors such as credit history, income stability, and debt-to-income ratio to provide accurate predictions.\n"
        f"* It's essential for borrowers to understand their chances of loan approval to make informed financial decisions.\n"
        f"* The Loan Approval Prediction System empowers both lenders and borrowers by streamlining the loan application process and minimizing uncertainty.\n"
        f"\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains [INSERT NUMBER] loan applications divided into train, test, and validation sets.\n"
        f"* The datasets were gathered from [INSERT SOURCE] (provide link if available)"
)
    st.success(
        f"The loan acceptance prediction model has 3 business requirements:\n"
        f"* 1 - Ensure the model achieves at least 90% accuracy in predicting loan acceptance.\n"
        f"* 2 - Implement measures to mitigate biases and ensure fairness across demographic groups.\n"
        f"* 3 - Provide transparent and interpretable results to enhance understanding of loan approval decisions."
)