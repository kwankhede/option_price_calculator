# mathematical_explanation.py
import streamlit as st


def show_mathematical_explanation():
    st.title("Mathematical Explanation")

    # Black-Scholes Model Section
    st.header("Black-Scholes Model")

    st.write(
        """
    The Black-Scholes model is a mathematical model used for pricing options. It assumes that the 
    price of the underlying asset follows a geometric Brownian motion. The formula for a call option 
    price is given by:

    \[ C = N(d_1) \cdot S - N(d_2) \cdot K \cdot e^{-rT} \]

    where:
    - \( C \) is the call option price.
    - \( N(d) \) is the cumulative standard normal distribution function.
    - \( S \) is the current price of the underlying asset.
    - \( K \) is the strike price of the option.
    - \( T \) is the time to expiration.
    - \( r \) is the risk-free interest rate.
    - \( \sigma \) is the volatility of the underlying asset.
    - \( d_1 = \frac{\ln(S/K) + (r + (\sigma^2)/2)T}{\sigma \sqrt{T}} \)
    - \( d_2 = d_1 - \sigma \sqrt{T} \)

    The input values are:
    - **Current Price (\(S\)):** The current price of the underlying asset.
    - **Strike Price (\(K\)):** The strike price of the option.
    - **Time to Expiration (\(T\)):** The time remaining until the option expires.
    - **Risk-Free Interest Rate (\(r\)):** The risk-free interest rate.
    - **Volatility (\(\sigma\)):** The volatility of the underlying asset.
    """
    )

    # Monte Carlo Simulations Section
    st.header("Monte Carlo Simulations")

    st.write(
        """
    Monte Carlo simulations involve simulating multiple future paths for the stock price to estimate 
    the option price. The general steps are as follows:

    1. **Generate Random Paths:**
        Simulate multiple future paths for the stock price based on a stochastic process, often modeled 
        using geometric Brownian motion.

    2. **Calculate Payoffs:**
        For each simulated path, calculate the payoff of the option at the expiration date.

    3. **Average Payoffs:**
        Average the payoffs over all simulated paths.

    4. **Discount to Present Value:**
        Discount the average payoff to the present value to obtain the option price.

    The input values include parameters such as:
    - **Number of Simulations:** The number of simulated paths to generate.
    - **Number of Time Steps:** The number of time steps in each simulation.
    - **Volatility (\(\sigma\)):** Similar to the Black-Scholes model, it represents the volatility of the underlying asset.
    - **Risk-Free Interest Rate (\(r\)):** The risk-free interest rate.
    """
    )

    st.subheader("Obtaining Input Values:")
    st.write(
        """
    - **Stock Price (\(S\)):** Obtained from the current market value of the underlying asset.
    - **Strike Price (\(K\)):** Determined based on the desired terms of the option contract.
    - **Time to Expiration (\(T\)):** Calculated as the time remaining until the option contract expires.
    - **Volatility (\(\sigma\)):** Estimated based on historical price data or implied volatility.
    - **Risk-Free Interest Rate (\(r\)):** Obtained from risk-free government bond rates.
    - **Number of Simulations and Time Steps:** Chosen based on computational resources and accuracy requirements.
    """
    )


# main.py
import streamlit as st
from mathematical_explanation import show_mathematical_explanation

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Mathematical Explanation"])

# Home Page
if selection == "Home":
    st.title("Options Trading App")
    st.write(
        "Welcome to the Options Trading App! Use the sidebar to navigate to different sections."
    )

# Mathematical Explanation Page
elif selection == "Mathematical Explanation":
    show_mathematical_explanation()
