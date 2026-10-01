import streamlit as st
import csv

st.set_page_config(page_title="Lagos Crypto Dashboard")
st.title("Lagos Crypto Dashboard - Built from Lagos!")
st.markdown("Real Bitcoin Data | 1 Year Trend")

rows = []
with open("real_bitcoin_1year.csv", "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        rows.append(row)

st.success(f"Loaded {len(rows)} days of Bitcoin data")

first_price = float(rows[0][1])
last_price = float(rows[-1][1])
growth = last_price / first_price * 500
pct = (last_price/first_price-1)*100

st.markdown(f"**Columns:** {header[0]}, {header[1]}")
st.markdown(f"**First day:** {rows[0][0]} - ${first_price}")
st.markdown(f"**Last day:** {rows[-1][0]} - ${last_price}")

st.metric("Your $500 investment would be", f"${growth:.2f}", f"{pct:.1f}%")

st.markdown("---")
st.markdown("### Last 5 days:")
for r in rows[-5:]:
    st.markdown(f"- {r[0]} : ${r[1]}")

st.markdown("---")
st.markdown("Built by a Lagos Data Analyst | 2026")