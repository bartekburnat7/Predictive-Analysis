import streamlit as st
from app_pages.dashboardPages import dashboardPage
from app_pages.

appInstance = dashboardPage("Streamlit App")

appInstance.add_page("Loan Project Summary", app_pages.homePage)