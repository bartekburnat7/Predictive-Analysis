Deployed Code - https://loan-approval-p5-a86a2d0a5eef.herokuapp.com/

## Dataset Content

The dataset is sourced from Kaggle and contains 381 customers that have applied for a loan with the bank.

| Column             | Description                                                                                                  | Example                |
|--------------------|--------------------------------------------------------------------------------------------------------------|------------------------|
| Loan_ID            | Unique identifier assigned to each loan application                                                           | LP001003               |
| Gender             | Gender of the applicant                                                                                     | Male, Female           |
| Married            | Marital status of the applicant                                                                              | Yes, No                |
| Dependents         | Number of dependents of the applicant                                                                        | 0, 1, 2, 3+           |
| Education          | Highest education level attained by the applicant                                                             | Graduate, Not Graduate |
| Self_Employed      | Indicates whether the applicant is self-employed or not                                                      | Yes, No                |
| ApplicantIncome    | Total income of the applicant (in currency)                                                                   | 4583, 3000             |
| CoapplicantIncome  | Total income of the co-applicant (in currency, if any)                                                        | 1508.0, 0.0            |
| LoanAmount         | Amount of the loan applied for (in currency)                                                                  | 128.0, 66.0            |
| Loan_Amount_Term   | Duration of the loan (in months)                                                                             | 360, 120               |
| Credit_History     | Credit history of the applicant (1.0 represents good credit history, 0.0 represents bad credit history)     | 1.0, 0.0               |
| Property_Area      | Area where the property associated with the loan is located                                                   | Rural, Urban, Semiurban|
| Loan_Status        | Status of the loan application (Y for Approved, N for Not Approved)                                           | Y, N                   |


## Business Requirements

The Loan Approval Prediction System offers a solution to streamline the lending process for banks and financial institutions. By leveraging machine learning algorithms, this system automates loan approval decisions, reducing turnaround time, enhancing efficiency, and improving decision-making accuracy. With a dataset comprising applicant attributes such as income, education, credit history, and property area, the system predicts loan approval status, allowing lenders to make objective assessments based on historical data and predefined criteria. Through features like data preprocessing, feature engineering, and model selection, the system optimizes predictive performance, ensuring reliable outcomes. Implementation entails deploying the trained model into production, adhering to regulatory compliance, safeguarding data privacy, and managing risks associated with model bias. Continuous performance monitoring and feedback integration further refine the system, maintaining its effectiveness and reliability over time. Ultimately, the Loan Approval Prediction System offers a data-driven approach to enhance profitability, mitigate risks, and deliver superior customer experiences in the lending domain.


## Hypothesis and how to validate?
* List here your project hypothesis(es) and how you envision validating it (them)

Project Hypotheses and Validation:

-   __Hypothesis:__ Applicant attributes significantly influence loan approval decisions.

    __Validation:__ Analyze feature importance using machine learning algorithms to correlate attributes with loan approval outcomes.

-   __Hypothesis:__ Machine learning models accurately predict loan approval status.

    __Validation:__ Train models using historical data and evaluate performance against benchmarks using metrics like accuracy and precision.

-   __Hypothesis:__ Automated loan approval improves efficiency and reduces turnaround time.

    __Validation:__ Implement the system and compare processing times before and after automation through A/B testing or pilot studies.

-   __Hypothesis:__ The system enhances risk management by identifying potential defaulters.

    __Validation:__ Measure model performance in identifying defaulters and assess its impact on portfolio quality.

-   __Hypothesis:__ Continuous monitoring and feedback integration improve model performance.

    __Validation:__ Iterate on model updates using stakeholder feedback, demonstrating improvements in accuracy and reliability over time.


## The rationale to map the business requirements to the Data Visualizations and ML tasks
-   Data Visualation and Presentation
    - The dashboard will display the 'distribution graphs' and 'correlation graphs' for customers that were and were not accepted for a loan.
-   Classification Problem
    - Build and fit a ML Pipeline to predict if a given customer will be accepted for a loan or not. I will be using a DecisionTreeClassifier model.
    - This model will display if the candidate is fit for a loan or if the bank should avoid doing business with the individual.
    - I am aiming for at least 80% accuracy rating.

## ML Business Case
1. What are the business requirements?
    - Develop and deploy machine learning algorithms to automate loan approval decisions based on applicant attributes and historical data.
    - Implement continuous performance monitoring and feedback integration to ensure the system's effectiveness, reliability, and regulatory compliance over time.
2. Is there any business requirement that can be answered with conventional data analysis?
    - Utilize conventional data analysis techniques to identify key factors from historical data and optimize predictive performance for loan approval decisions.
3. Does the client need a dashboard or an API endpoint?
    - Given the need for lenders to interact with the system, monitor performance metrics, and access insights, the client would benefit from a user-friendly dashboard providing visual representations of loan approval predictions, performance metrics, and relevant insights derived from data analysis.
4. What does the client consider as a successful project outcome?
    - The client considers a successful project outcome to be a streamlined lending process with automated, accurate loan approval decisions, improved efficiency, minimized risks, enhanced profitability and a 80% accuracy rating.
5. Ethical or Privacy concerns?
    - Ethical and privacy concerns involve regulatory compliance, data privacy, mitigating model bias risks, and ensuring fairness and transparency in loan approval decisions.
6. Does the data suggest a particular model?
    - The type of models suggested for loan approval prediction includes machine learning algorithms such as logistic regression, decision trees, random forests.
7. What are the model's inputs and intended outputs?
    - The model's inputs typically include applicant attributes such as income, education, credit history, and property area. The intended output is the prediction of loan approval status, indicating whether a loan application should be approved or denied based on the provided inputs and historical data.
8. What are the criteria for the performance goal of the predictions?
    - An accuracy of at least 80%.
9. How will the client benefit?
    - The bank will benefit from increased operational efficiency, reduced risks, improved profitability, and enhanced customer satisfaction resulting from the implementation of the Loan Approval Prediction System.


## Dashboard Design

__Project Summary:__
-   This section provides an overview of the project, introducing the Loan Approval Prediction System and its significance. It highlights the system's objectives, such as assisting financial institutions and individuals in forecasting loan approval outcomes accurately and efficiently. Additionally, it emphasizes the importance of informed financial decisions and empowerment for both lenders and borrowers.

__Project Dataset:__
-   The purpose of this section is to provide information about the dataset used in the project. It specifies the size of the dataset and its division into train, test, and validation sets, allowing users to understand the data's structure and organization. Furthermore, it mentions the source of the dataset, providing transparency about the data used for analysis.

__Loan Acceptance Prediction Model Requirements:__
-   This section outlines the key business requirements for the loan acceptance prediction model. It identifies three critical objectives: achieving a minimum accuracy level, implementing measures to mitigate biases and ensure fairness across demographic groups, and providing transparent and interpretable results. By stating these requirements, the section sets clear expectations for the model's performance and ethical considerations.

__Data Visualization:__
-   The purpose of this section is to visually represent insights from the loan data. While the current content appears to be a placeholder, typically this section would include various charts, graphs, or visualizations that illustrate patterns, correlations, or trends within the dataset. Visualizations can enhance understanding and facilitate data-driven decision-making by making complex information more accessible and interpretable.

__Conclusions and Next Steps:__
-   This section summarizes the findings and conclusions drawn from the analysis conducted in the project. It provides insights into factors influencing loan acceptance based on correlations and interpretations from the data. Additionally, it outlines the next steps or actions to be taken, such as further analysis, model refinement, or implementation of recommendations. This section helps to wrap up the project and guide future activities based on the current findings.



## Unfixed Bugs
* I ended up creating a one page dashboard as I kept running into problems with the code and creating a one page dashboard resolved these issues.

## Deployment
### Heroku

* The App live link is: https://loan-approval-p5-a86a2d0a5eef.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
#### The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.



## Main Data Analysis and Machine Learning Libraries

- **NumPy**: A fundamental Python library for numerical computing, offering powerful array manipulation capabilities.
- **Pandas**: A versatile Python library for data manipulation and analysis, providing advanced data structures and tools for working with structured data.
- **Matplotlib**: A comprehensive Python library for creating static, interactive, and publication-quality visualizations from data.
- **Seaborn**: A statistical data visualization library in Python based on Matplotlib, offering a high-level interface for drawing attractive and informative statistical graphics.
- **Plotly**: A Python graphing library enabling the creation of interactive, publication-quality graphs online.
- **Streamlit**: An open-source Python library simplifying the creation and sharing of custom web apps for machine learning and data science.
- **Scikit-learn**: A simple and efficient Python library for machine learning, featuring tools for classification, regression, clustering, and dimensionality reduction.
- **Imbalanced-learn**: A Python library addressing class imbalance in machine learning datasets through various techniques for resampling and handling imbalanced data.


## Credits 

The genesis of my project's concept finds its roots in the insightful loan approval model presented in the Churnometer walkthrough project by the esteemed Code Institute. Furthermore, the invaluable Classification lessons offered by the Institute have significantly influenced the trajectory of my work. Leveraging the framework and code structure from these resources, I methodically customized and fine-tuned them to cater specifically to the intricacies of loan approval, ensuring alignment with the objectives and intricacies of my project.

### Content 

- I based my project off the code institute Churnometer project.
- Loand data was taken from kaggle - https://www.kaggle.com/datasets/bhavikjikadara/loan-status-prediction

## Acknowledgements
I extend heartfelt thanks to my machine learning mentor for their invaluable guidance and support, which has shaped my journey profoundly. Likewise, I'm deeply grateful to the Code Institute for their comprehensive curriculum and resources, crucial in honing my coding and machine learning skills. Your contributions have been integral to my success. Thank you both immensely.

