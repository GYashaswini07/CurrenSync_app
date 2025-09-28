import streamlit as st

st.title("💱 Currency Converter")

rates = {
    "USD": 1,
    "INR": 88.69,
    "EUR": 0.85,
    "GBP": 0.746,
    "JPY": 150,
    "AUD": 1.53,
    "CAD": 1.39,
    "CNY": 7.13,
    "CHF": 0.80,
    "SGD": 1.35
}

currency_names = {
    "USD": "Dollar",
    "INR": "Rupee",
    "EUR": "Euro",
    "GBP": "Pound",
    "JPY": "Yen",
    "AUD": "Australian Dollar",
    "CAD": "Canadian Dollar",
    "CNY": "Yuan",
    "CHF": "Swiss Franc",
    "SGD": "Singapore Dollar"
}

currencies = [f"{code} ({currency_names[code]})" for code in rates]

amount = st.number_input("Enter amount:", min_value=0.0, format="%.2f")
from_selection = st.selectbox("From Currency:", currencies)
to_selection = st.selectbox("To Currency:", currencies)

from_currency = from_selection.split()[0]
to_currency = to_selection.split()[0]

if st.button("Convert"):
    usd_amount = amount / rates[from_currency]
    converted = usd_amount * rates[to_currency]
    st.success(f"{amount} {from_currency} = {round(converted, 2)} {to_currency}")
