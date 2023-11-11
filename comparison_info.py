# comparison_info.py
import streamlit as st


def show_comparison_info():
    st.title("Advantages and Disadvantages")

    # Black-Scholes Model Section
    st.header("Black-Scholes Model")

    st.subheader("Advantages:")
    st.write(
        """
    1. **Analytical Solution:** The Black-Scholes model provides a closed-form analytical solution, 
       allowing for quick and precise calculation of option prices.
    2. **Widely Used:** It is a standard model widely used in the financial industry for pricing European-style options.
    3. **Sensitivity Analysis:** It allows for sensitivity analysis, helping traders understand how option prices 
       change with variations in underlying parameters.
    """
    )

    st.subheader("Disadvantages:")
    st.write(
        """
    1. **Assumptions:** Relies on several assumptions, including constant volatility and risk-free interest rate, 
       which may not always hold in real-world scenarios.
    2. **European Options Only:** Applicable only to European-style options with no dividends.
    3. **Limited Flexibility:** The model is less flexible for complex options and does not account for early exercise.
    """
    )

    # Monte Carlo Simulations Section
    st.header("Monte Carlo Simulations")

    st.subheader("Advantages:")
    st.write(
        """
    1. **Flexibility:** Offers flexibility in modeling complex financial instruments and incorporating various 
       factors affecting option prices.
    2. **Realistic Scenarios:** Can simulate a wide range of realistic scenarios by considering stochastic processes 
       and capturing uncertainty.
    3. **American Options:** Can be applied to value American-style options with early exercise features.
    """
    )

    st.subheader("Disadvantages:")
    st.write(
        """
    1. **Computational Intensity:** Monte Carlo simulations can be computationally intensive, especially for a large number of paths.
    2. **Complex Implementation:** Requires careful implementation and calibration of the model parameters.
    3. **Interpretation Challenges:** Results may require careful interpretation due to the stochastic nature of the simulations.
    """
    )


# main.py
import streamlit as st
from comparison_info import show_comparison_info

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Advantages and Disadvantages"])

# Home Page
if selection == "Home":
    st.title("Options Trading App")
    st.write(
        "Welcome to the Options Trading App! Use the sidebar to navigate to different sections."
    )

# Advantages and Disadvantages Page
elif selection == "Advantages and Disadvantages":
    show_comparison_info()
