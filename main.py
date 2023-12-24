import streamlit as st
from information import show_home_page
from options_info import show_options_info
from mathematical_explanation import show_mathematical_explanation
from comparison_info import show_comparison_info
from monte_carlo_calculator import monte_carlo_option_pricing
from references import show_references
import time

# Function to check if 5 hours have passed
@st.cache(ttl=60 * 60 * 5)  # 60 seconds * 60 minutes * 5 hours
def check_time():
    return time.time()

# Navigation
page_options = [
    "Options Overview",
    "Pricing Methods",
    "Mathematical Explanation",
    "Comparison",
    "Calculator",
    "References",
]

# Sidebar
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", page_options)

# Main content
st.image("Monte.png", use_column_width=True)

# Check if 5 hours have passed, if yes, rerun the code
if check_time():
    if selected_page == "Options Overview":
        show_home_page()
    elif selected_page == "Pricing Methods":
        show_options_info()
    elif selected_page == "Mathematical Explanation":
        show_mathematical_explanation()
    elif selected_page == "Comparison":
        show_comparison_info()
    elif selected_page == "Calculator":
        monte_carlo_option_pricing()
    elif selected_page == "References":
        show_references()
