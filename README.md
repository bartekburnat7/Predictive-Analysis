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

1. The initial page outlines the project dataset and articulates the business requirements.



## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a significant variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is: https://YOUR_APP_NAME.herokuapp.com/ 
* Set the runtime.txt Python version to a [Heroku-20](https://devcenter.heroku.com/articles/python-support#supported-runtimes) stack currently supported version.
* The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file.


## Main Data Analysis and Machine Learning Libraries
* Here you should list the libraries you used in the project and provide an example(s) of how you used these libraries.


## Credits 

The genesis of my project's concept finds its roots in the insightful loan approval model presented in the Churnometer walkthrough project by the esteemed Code Institute. Furthermore, the invaluable Classification lessons offered by the Institute have significantly influenced the trajectory of my work. Leveraging the framework and code structure from these resources, I methodically customized and fine-tuned them to cater specifically to the intricacies of loan approval, ensuring alignment with the objectives and intricacies of my project.

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign-Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign-up page are from This Open-Source site
- The images used for the gallery page were taken from this other open-source site



## Acknowledgements (optional)
* Thank the people that provided support through this project.

