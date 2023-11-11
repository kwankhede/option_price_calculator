# information.py
import streamlit as st
import numpy as np
import plotly.graph_objects as go


def show_home_page():
    # Introduction to Options
    st.header("Options Overview")
    st.write(
        """
    Options are financial derivatives that give the buyer the right, but not the obligation, 
    to buy or sell an underlying asset at a predetermined price (the strike price) before or at the option's expiration date.
    """
    )

    st.subheader("Key Concepts:")
    st.write(
        """
    - **Call Option:** Gives the holder the right to buy the asset.
    - **Put Option:** Gives the holder the right to sell the asset.
    - **Strike Price (K):** The price at which the option holder can buy or sell the underlying asset.
    - **Expiration Date (T):** The date by which the option must be exercised or it becomes worthless.
    - **Premium:** The price paid to purchase the option.
    """
    )

    # Types of Options
    st.header("Types of Options")
    st.write(
        """
    Options come in two main types: Call Options and Put Options. Traders use these instruments for various strategies 
    to hedge risk, speculate, or generate income.
    """
    )

    st.subheader("1. Call Options")
    st.write(
        """
    - **Long Call:** Buying a call option gives the right to buy the underlying asset at the strike price.
    - **Short Call (or Call Writing):** Selling a call option obligates the seller to sell the underlying asset if the option is exercised.
    """
    )

    st.subheader("2. Put Options")
    st.write(
        """
    - **Long Put:** Buying a put option gives the right to sell the underlying asset at the strike price.
    - **Short Put (or Put Writing):** Selling a put option obligates the seller to buy the underlying asset if the option is exercised.
    """
    )

    # Long/Short Positions for Call and Put Options
    st.header("Long and Short Positions for Call and Put Options")
    st.image(
        "long_short.jpeg",
        caption="Long/Short Positions for Options",
        use_column_width=True,
    )
    st.write(
        """
    In the context of options trading:
    - **Long Position:** The buyer of the option holds a long position, whether it's a call or a put.
    - **Short Position:** The seller (writer) of the option holds a short position, whether it's a call or a put.
    """
    )

    # Option Payoff for Different Positions
    st.header("Option Payoff for Different Positions")
    st.image(
        "payoff.jpeg",
        caption="payoff for Options",
        use_column_width=True,
    )

    st.subheader("Graph 1: Long Call")

    st.write(
        """
    **Explanation for Long Call (Graph 1):**
    - The option buyer makes a loss (represented by the red line) until the “Breakeven” is crossed.
    - The loss is capped, but profits grow with the price.
    - The long call holder makes a profit equal to the stock price at expiration minus strike price minus premium if the option is in the money.
    - The call option holder makes a loss equal to the amount of premium if the option expires out of money.
    - The writer of the option makes a flat profit equal to the option premium.
    """
    )

    st.subheader("Graph 2: Long Put")

    st.write(
        """
    **Explanation for Long Put (Graph 2):**
    - The option buyer makes a loss until the stock price is less than the strike price plus the premium.
    - The loss is capped at the total premium paid, but there is unlimited profit potential if the stock price goes to zero.
    - The long put holder makes a profit equal to the strike price minus the stock price at expiration, minus the premium if the option is in the money.
    - If the option expires out of the money, the long put holder loses the entire premium.
    - The writer of the option makes a flat profit equal to the option premium if the option expires out of the money and unlimited loss if it expires in the money.
    """
    )

    st.subheader("Graph 3: Short Call")

    st.write(
        """
    **Explanation for Short Call (Graph 3):**
    - The option buyer makes a profit until the stock price is more than the strike price plus the premium.
    - The profit is capped at the total premium received, but there is unlimited loss potential if the stock price goes significantly higher.
    - The short call writer makes a profit equal to the premium received if the option expires out of the money.
    - If the option expires in the money, the short call writer faces unlimited losses as the stock price rises.
    """
    )

    st.subheader("Graph 4: Short Put")

    st.write(
        """
    **Explanation for Short Put (Graph 4):**
    - The option buyer makes a profit until the stock price is less than the strike price minus the premium.
    - The profit is capped at the total premium received, but there is unlimited loss potential if the stock price goes to zero.
    - The short put writer makes a profit equal to the premium received if the option expires out of the money.
    - If the option expires in the money, the short put writer faces unlimited losses as the stock price falls.
    """
    )
