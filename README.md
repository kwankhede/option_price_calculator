## Options Price Calculator: A Geometric Brownian Motion Approach

### Abstract

In the dynamic world of finance, options pricing plays a crucial role in risk management and investment strategy. The Options Price Calculator presented here leverages the power of Monte Carlo simulations and Geometric Brownian Motion (GBM) to predict option prices under various market scenarios. This article outlines the underlying principles, implementation details, and applications of the calculator.

### 1. Introduction

Options pricing involves forecasting the future value of financial instruments, providing investors with insights into potential risks and returns. The calculator utilizes a Monte Carlo simulation, a statistical technique that generates a multitude of potential outcomes to approximate the distribution of potential prices.

### 2. Geometric Brownian Motion

The foundation of the Options Price Calculator lies in Geometric Brownian Motion, a mathematical model for the unpredictable movements of financial markets. GBM assumes a constant drift accompanied by random shocks, capturing the inherent uncertainty in stock prices.

### 3. Monte Carlo Simulation

Monte Carlo simulations apply a chosen model—in this case, GBM—to a vast set of random trials. By running these simulations, the calculator produces a range of plausible future outcomes, allowing users to gauge the potential risks and rewards associated with options.

### 4. User Interface

The Streamlit-based user interface provides an intuitive platform for users to input key parameters such as stock price, strike price, days until expiration, volatility, and more. The interactive nature of the app allows for real-time adjustments and immediate visualization of the simulated stock prices.

### 5. Results and Analysis

The calculator generates not only the theoretical prices of options but also intrinsic values, option classifications (In the Money, Out of the Money, At the Money), and Greeks (Delta, Gamma, Vega, Theta, Rho). Users gain comprehensive insights into the potential behavior of their options under different market conditions.

### 6. Implementation Details

The Python-based implementation employs libraries such as NumPy, Matplotlib, and Streamlit. Geometric Brownian Motion paths are generated, and Black-Scholes equations calculate theoretical option prices. The Streamlit framework facilitates a seamless user experience.

### 7. Applications

The Options Price Calculator finds applications in risk management, investment strategy formulation, and financial education. Traders and investors can use the tool to make informed decisions based on a comprehensive understanding of potential outcomes.

### 8. Future Enhancements

Future iterations may include additional features such as more advanced option strategies, implied volatility calculations, and integration with real-time market data for enhanced accuracy.

### 9. Conclusion

The Options Price Calculator, utilizing Monte Carlo simulations and Geometric Brownian Motion, empowers users to make informed decisions in the complex landscape of options trading. Its user-friendly interface, robust calculations, and insightful visualizations make it a valuable tool for both novice and seasoned investors.

### References

1. Black, F., & Scholes, M. (1973). The Pricing of Options and Corporate Liabilities. Journal of Political Economy, 81(3), 637–654. https://doi.org/10.1086/260062

2. Hull, J. C. (2017). Options, Futures, and Other Derivatives. Pearson.

3. Shreve, S. E. (2004). Stochastic Calculus for Finance II: Continuous-Time Models. Springer.

4. Streamlit Documentation. (https://docs.streamlit.io)

5. NumPy Documentation. (https://numpy.org/doc/)

6. Matplotlib Documentation. (https://matplotlib.org/stable/contents.html)

This Options Price Calculator represents a fusion of financial theory and practical implementation, providing a valuable resource for anyone navigating the complexities of options trading.
