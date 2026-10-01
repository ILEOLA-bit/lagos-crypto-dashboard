import streamlit as st
import pandas as pd

st.set_page_config(page_title="Lagos Crypto Dashboard", page_icon="🇳🇬", layout="wide")

st.title("Lagos! 🇳🇬 Bitcoin Dashboard")
st.markdown("**Real Bitcoin Data | 1 Year Trend | Built from Lagos**")
st.markdown("---")

# Load data
try:
    df = pd.read_csv("real_bitcoin_1year.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values('Date')

    st.success(f"Loaded {len(df)} days of Bitcoin data")

    # Metrics
    col1, col2, col3 = st.columns(3)
    first_price = df['Price'].iloc[0]
    last_price = df['Price'].iloc[-1]
    growth = ((last_price - first_price) / first_price) * 100

    initial_investment = 500
    final_value = initial_investment * (last_price / first_price)

    with col1:
        st.metric("First Price", f"${first_price:,.2f}", f"{df['Date'].iloc[0].date()}")
    with col2:
        st.metric("Last Price", f"${last_price:,.2f}", f"{df['Date'].iloc[-1].date()}")
    with col3:
        st.metric("Growth", f"{growth:.2f}%", f"${final_value:.2f} from $500")

    st.markdown("### Your $500 Investment Would Be:")
    st.markdown(f"# ${final_value:,.2f}")
    if growth > 0:
        st.markdown(f"<h3 style='color:green'>+{growth:.2f}% 🚀</h3>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h3 style='color:red'>{growth:.2f}% 📉</h3>", unsafe_allow_html=True)

    # CHART
    st.markdown("---")
    st.subheader("📈 Bitcoin Price - Last 1 Year")
    st.line_chart(df.set_index('Date')['Price'], height=400)

    # Data table
    with st.expander("See raw data"):
        st.dataframe(df.tail(20), use_container_width=True)

    st.markdown("---")
    st.markdown("Built with ❤️ in Lagos, Nigeria | ILEOLA-bit")

except Exception as e:
    st.error(f"Error: {e}")
    st.info("Make sure real_bitcoin_1year.csv is uploaded")