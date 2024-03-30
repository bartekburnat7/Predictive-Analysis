import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def page_visualization_body():
    st.title("Data Visualization")
    st.info("Visualizing loan data...")
    
    # Load loan data
    loan_data_raw = pd.read_csv("inputs/datasets/raw/loan_data.csv").drop(['Loan_ID'], axis=1)
    
    # Select categorical columns
    cat_num = loan_data_raw.select_dtypes(include=['object']).columns.to_list()
    
    # Create subplots
    fig, ax = plt.subplots(4, 2, figsize=(12, 15))
    
    # Plot countplots for each categorical variable
    for index, cat_col in enumerate(cat_num):
        row, col = index // 2, index % 2
        sns.countplot(x=cat_col, data=loan_data_raw, hue='Loan_Status', ax=ax[row, col])
    
    # Adjust subplots
    plt.subplots_adjust(hspace=1)
    
    # Display plots
    st.pyplot(fig)

    st.write("## Conclusions and Next steps")
    st.success("The correlations and plots interpretation converge.\n"
            "An accepted customer has a credit score.\n"
            "A higher income increases your chance of approval.\n"
            "Customers' income has an impact on the approval rate.\n"
            "Loan amount has a low correlation with acceptance rates.")
