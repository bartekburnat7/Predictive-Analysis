import streamlit as st
from app_pages.dashboardPages import dashboardPage
from app_pages.projectSummary import page_summary_body
from app_pages.dataVisualization import page_visualization_body
from app_pages.loanAcceptance import loan_acceptance_body
from app_pages.projectHypothesis import project_hypothesis_body
from app_pages.performanceAnalysis import performance_analysis_body

appInstance = dashboardPage("Streamlit App")

appInstance.add_page("Loan Project Summary", page_summary_body())
appInstance.add_page("Data Visualization", page_visualization_body())
appInstance.add_page("Loan Acceptance", loan_acceptance_body())
appInstance.add_page("Project Hypothesis", project_hypothesis_body())
appInstance.add_page("Performance Analysis", performance_analysis_body())

appInstance.run()