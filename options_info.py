# options_info.py
import streamlit as st


def show_options_info():
    st.title("Options Pricing Methods")

    st.write(
        """
    Options are financial contracts that provide the buyer with the right, but not the obligation, 
    to buy or sell a certain asset at a specified price on or before a specified date. The seller 
    of the option is obligated to fulfill the contract if the buyer exercises their right.
    """
    )

    st.header("Types of Options")
    st.write(
        """
    There are two main types of options:

    - **Call options:** Give the buyer the right to buy the underlying asset at the strike price on or before the expiration date.
    - **Put options:** Give the buyer the right to sell the underlying asset at the strike price on or before the expiration date.
    """
    )

    st.header("Purposes of Options")
    st.write(
        """
    Options are used by investors for various purposes, including:

    - **Speculation:** Investors can buy or sell options to speculate on the future price of the underlying asset.
    - **Hedging:** Investors can buy or sell options to hedge their existing positions in the underlying asset.
    - **Income generation:** Investors can sell options to generate income, known as a premium.
    """
    )

    st.header("Options Pricing")
    st.write(
        """
    The price of an option is determined by factors such as the price of the underlying asset, the strike price, 
    the time to expiration, the volatility of the underlying asset, and the risk-free interest rate. The Black-Scholes 
    model is widely used for pricing options, taking all these factors into account.
    """
    )

    st.subheader("Black-Scholes Model and Assumptions")
    st.write(
        """
    The Black-Scholes model is a mathematical model for pricing European call and put options. It is based on the following assumptions:

    - The underlying asset price follows a geometric Brownian motion with constant drift and volatility.
    - The risk-free interest rate is constant.
    - There are no transaction costs or taxes.
    - The option can only be exercised at the expiration date.

    The Black-Scholes model is a popular tool for pricing options, but it's important to note that it has simplifying assumptions and may not be accurate in all cases.
    """
    )

    st.subheader("Black-Scholes Formula for Call Option")
    st.write(
        """
    The Black-Scholes formula for calculating the price of a call option is as follows:

    \[ C = N(d_1) \cdot S - N(d_2) \cdot K \cdot \exp(-rT) \]

    where:
    - \( C \) is the price of the call option
    - \( N(d) \) is the cumulative standard normal distribution function
    - \( S \) is the price of the underlying asset
    - \( K \) is the strike price of the option
    - \( T \) is the time to expiration of the option
    - \( r \) is the risk-free interest rate

    The Black-Scholes formula can be used to calculate the price of any European call or put option.
    """
    )

    st.subheader("Example - Using the Black-Scholes Formula")
    st.write(
        """

    Suppose you are considering buying a call option on a stock with the following characteristics:

    - Stock price: $100
    - Strike price: $110
    - Time to expiration: 3 months
    - Risk-free interest rate: 5%
    - Volatility: 20%

    Using the Black-Scholes formula, you can calculate the theoretical price of the call option to be USD 5.08. This means that you would have to pay USD 5.08 per share to buy the call option.

    If the stock price rises above USD 110 at any time before the expiration date, you can exercise your right to buy the stock at $110 per share, generating a profit. However, if the stock price does not rise above USD 110 by the expiration date, the option will expire worthless, and you will lose your investment.
    """
    )

    st.subheader("Monte Carlo Simulation for Options Pricing")
    st.write(
        """
    Monte Carlo simulation is a numerical technique used to model the probability of different outcomes in a process that 
    cannot easily be predicted due to the intervention of random variables. In options pricing, Monte Carlo simulations are 
    commonly used to model the future stock prices and calculate option prices based on the average of these simulated paths.
    """
    )

    st.subheader("Geometric Brownian Motion (GBM)")
    st.write(
        """
    Geometric Brownian Motion is a mathematical model used to describe the random movement of assets, such as stock prices. 
    It assumes that the logarithm of the asset's price follows a Brownian motion with drift and volatility. The GBM model is 
    often employed in Monte Carlo simulations for options pricing.
    """
    )

    st.subheader("Example")
    st.write(
        """
    Suppose you are using Monte Carlo simulation to price a call option. The simulation generates multiple future stock price 
    paths based on the GBM model. The option price is then calculated based on the average of the payoffs from these simulated paths.
    """
    )
