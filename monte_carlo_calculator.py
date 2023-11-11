# monte_carlo_calculator.py
import streamlit as st
import numpy as np
import pandas as pd
from scipy.stats import norm
import plotly.graph_objects as go


# Function to generate geometric Brownian motion paths
def geo_paths(S, T, r, q, sigma, steps, N):
    dt = T / steps
    ST = np.log(S) + np.cumsum(
        (
            (r - q - sigma**2 / 2) * dt
            + sigma * np.sqrt(dt) * np.random.normal(size=(steps, N))
        ),
        axis=0,
    )
    return np.exp(ST)


# Function to calculate option price using Black-Scholes formula
def black_scholes_option_price(S, K, T, r, q, sigma, option_type):
    d1 = (np.log(S / K) + (r - q + (sigma**2) / 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == "Call":
        option_price = S * np.exp(-q * T) * norm.cdf(d1) - K * np.exp(
            -r * T
        ) * norm.cdf(d2)
    elif option_type == "Put":
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * np.exp(
            -q * T
        ) * norm.cdf(-d1)
    else:
        option_price = 0

    return option_price


def monte_carlo_option_pricing():
    st.title("Monte Carlo Option Pricing Calculator")

    st.header("Calculator Settings")

    # Take user input for option parameters
    S_input = st.number_input("Enter current stock price (S)", value=100.0)
    K_input = st.number_input("Enter strike price (K)", value=100.0)
    days_until_expiry_input = st.number_input("Enter Days Until Expiration", value=30)
    r_input = st.number_input(
        "Enter risk-free interest rate (r) in annual %", value=5.0
    )
    q_input = st.number_input("Enter dividend yield (q) in annual %", value=2.0)
    sigma_input = st.number_input("Enter annual volatility (sigma) in %", value=25.0)
    steps_input = st.number_input("Enter number of time steps", value=100)
    N_input = st.number_input("Enter number of trials", value=1000)

    # Add a "Generate Paths" button
    generate_button = st.button("Generate Paths and Calculate Option Price")

    # Placeholder for option metrics
    option_price_call = 0
    option_price_put = 0

    # Calculate option price using Monte Carlo simulation when the button is clicked
    if generate_button:
        T_input = days_until_expiry_input / 365.0  # Convert days to years
        paths = geo_paths(
            S_input,
            T_input,
            r_input / 100.0,
            q_input / 100.0,
            sigma_input / 100.0,
            steps_input,
            N_input,
        )

        # Calculate option price using Monte Carlo simulation
        payoffs_call = np.maximum(paths[-1] - K_input, 0)
        option_price_call = np.mean(payoffs_call) * np.exp(
            -r_input / 100.0 * T_input
        )  # discounting back to present value

        payoffs_put = np.maximum(K_input - paths[-1], 0)
        option_price_put = np.mean(payoffs_put) * np.exp(
            -r_input / 100.0 * T_input
        )  # discounting back to present value

        # Display option pricing results in a formatted table with custom styling
        st.subheader("Options Pricing Simulator")

        # Define CSS styles for the table
        table_styles = [
            {"selector": "thead", "props": "background-color: #f2f2f2;"},
            {"selector": "th, td", "props": "padding: 10px;"},
        ]

        # Create a Streamlit table with custom styles
        st.markdown(
            f"""
            <style>
                {' '.join([f"{style['selector']}{{{style['props']}}}" for style in table_styles])}
            </style>
            """,
            unsafe_allow_html=True,
        )

        # Data for the table
        data = {
            "Stock Price": [f"${S_input:.1f}"],
            "Exercise (Strike) Price": [f"${K_input:.1f}"],
            "Expiration Period": [days_until_expiry_input],
            "Number of Iterations": [f"{N_input}"],
            "Risk-Free Interest Rate": [f"{r_input:.1f}%"],
            "Time to Expiration": [f"{days_until_expiry_input}"],
            "Volatility of Stock": [f"{sigma_input:.1f}%"],
            "Simulation Value of Call Option": [f"${option_price_call:.3f}"],
            "Simulation Value of Put Option": [f"${option_price_put:.3f}"],
            "Black-Scholes Value of Call Option": [
                f"${black_scholes_option_price(S_input, K_input, T_input, r_input / 100.0, q_input / 100.0, sigma_input / 100.0, 'Call'):.3f}"
            ],
            "Black-Scholes Value of Put Option": [
                f"${black_scholes_option_price(S_input, K_input, T_input, r_input / 100.0, q_input / 100.0, sigma_input / 100.0, 'Put'):.3f}"
            ],
        }

        # Split the data into descriptions and values while preserving order
        descriptions = {key: key.replace("(", "<br>(") for key in data.keys()}
        values = {key: value[0] for key, value in data.items()}

        # Create a Streamlit layout with one column
        (col1,) = st.columns(1)

        # Create a table with values while preserving order
        col1.table(
            pd.DataFrame({"Values": list(values.values())}, index=list(values.keys()))
        )

        # Plot the generated paths interactively using Plotly
        st.subheader("Geometric Brownian Motion Paths")
        fig = go.Figure()
        for i in range(N_input):
            fig.add_trace(
                go.Scatter(
                    x=np.arange(steps_input + 1),
                    y=paths[:, i],
                    mode="lines",
                    name=f"Path {i+1}",
                )
            )

        fig.update_layout(
            title="Geometric Brownian Motion Paths",
            xaxis_title="Time Increments",
            yaxis_title="Stock Price",
            showlegend=True,
            height=600,  # Adjust the height of the plot
            width=800,  # Adjust the width of the plot
        )

        st.plotly_chart(fig)


# main.py
import streamlit as st
from monte_carlo_calculator import monte_carlo_option_pricing

# Sidebar
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", ["Home", "Monte Carlo Calculator"])

# Home Page
if selection == "Home":
    st.title("Options Trading App")
    st.write(
        "Welcome to the Options Trading App! Use the sidebar to navigate to different sections."
    )

# Monte Carlo Calculator Page
elif selection == "Monte Carlo Calculator":
    monte_carlo_option_pricing()
