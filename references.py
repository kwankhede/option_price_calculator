import streamlit as st


def show_references():
    st.title("References")
    st.write(
        "This Streamlit app was developed for educational purposes and references the following sources:"
    )
    st.markdown(
        "- Black-Scholes Formula: [Wikipedia](https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model)"
    )
    st.markdown(
        "- Monte Carlo Simulation: [Investopedia](https://www.investopedia.com/terms/m/montecarlosimulation.asp)"
    )
    st.markdown(
        "- Geometric Brownian Motion: [Investopedia](https://www.investopedia.com/terms/g/geometricbrownianmotion.asp)"
    )
    st.markdown("- Streamlit: [Streamlit Documentation](https://docs.streamlit.io/)")


if __name__ == "__main__":
    show_references()
