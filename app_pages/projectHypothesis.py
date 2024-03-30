import streamlit as st

def project_hypothesis_body():
    st.title("Loan Approval Prediction System")
    st.write("## Project Hypothesis and Validation")
    
    # Objective
    st.write("### Objective")
    st.write("Welcome to the Loan Approval Prediction System! Our goal is to streamline the lending process for banks and financial institutions by automating loan approval decisions based on applicant attributes and historical data.")
    
    # How it Works
    st.write("### How it Works")
    st.write("By leveraging machine learning algorithms, our system predicts loan approval status, allowing lenders to make objective assessments based on historical data and predefined criteria. Features like data preprocessing, feature engineering, and model selection optimize predictive performance, ensuring reliable outcomes.")
    
    # Dataset
    st.write("### Dataset")
    st.write("Our dataset comprises applicant attributes such as income, education, credit history, and property area, allowing for accurate prediction of loan approval status.")
    
    # Machine Learning Model
    st.write("### Machine Learning Model")
    st.write("Our machine learning model, including algorithms such as logistic regression, decision trees, and random forests, accurately predicts loan approval status based on applicant attributes and historical data.")
    
    # Success Criteria
    st.write("### Success Criteria")
    st.success("- Accurate Predictions: Our model achieves at least 80% accuracy in predicting loan approval status."
               "\n- Efficiency Improvement: Automated loan approval reduces turnaround time and enhances efficiency."
               "\n- Risk Management Enhancement: The system identifies potential defaulters, improving portfolio quality."
               "\n- Continuous Monitoring: Model updates based on stakeholder feedback demonstrate improvements in accuracy and reliability over time.")
    
    # Potential Impact
    st.write("### Potential Impact")
    st.info("- Enhanced Profitability: The system enhances profitability by streamlining the lending process and mitigating risks."
            "\n- Improved Customer Experience: Data-driven approach ensures superior customer experiences in the lending domain.")
