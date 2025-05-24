import streamlit as st
import pandas as pd
import math

# Page config
st.set_page_config(page_title="Mortgage Calculator", page_icon="🏠", layout="centered")

# Title
st.title("🏠 Mortgage Calculator")
st.markdown("Use this tool to estimate your monthly mortgage repayments and view a repayment schedule.")

# Input section
st.header("📥 Input Data")
with st.container():
    col1, col2 = st.columns(2)
    home_value = col1.number_input("Home Value (£)", min_value=0, value=500000, step=10000)
    deposit = col1.number_input("Deposit (£)", min_value=0, value=100000, step=10000)
    interest_rate = col2.number_input("Interest Rate (%)", min_value=0.0, value=5.5, step=0.1)
    loan_term = col2.number_input("Loan Term (Years)", min_value=1, value=30)

# Calculation
loan_amount = home_value - deposit
monthly_interest_rate = (interest_rate / 100) / 12
number_of_payments = loan_term * 12

if monthly_interest_rate == 0:
    monthly_payment = loan_amount / number_of_payments
else:
    monthly_payment = (
        loan_amount
        * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments)
        / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    )

# Summary metrics
total_payments = monthly_payment * number_of_payments
total_interest = total_payments - loan_amount

st.header("📊 Summary")
st.markdown("Quick overview of your loan repayments:")

col1, col2, col3 = st.columns(3)
col1.metric("Monthly Repayment", f"£{monthly_payment:,.2f}")
col2.metric("Total Repayment", f"£{total_payments:,.0f}")
col3.metric("Total Interest", f"£{total_interest:,.0f}")

# Amortisation schedule
schedule = []
remaining_balance = loan_amount

for i in range(1, number_of_payments + 1):
    interest_payment = remaining_balance * monthly_interest_rate
    principal_payment = monthly_payment - interest_payment
    remaining_balance -= principal_payment
    year = math.ceil(i / 12)
    schedule.append(
        [i, monthly_payment, principal_payment, interest_payment, remaining_balance, year]
    )

df = pd.DataFrame(
    schedule,
    columns=["Month", "Payment", "Principal", "Interest", "Remaining Balance", "Year"],
)

# Line Chart
st.header("📉 Loan Balance Over Time")
st.markdown("This chart shows how your remaining loan balance decreases each year.")

payments_df = df[["Year", "Remaining Balance"]].groupby("Year").min()
st.line_chart(payments_df)

# Payment table
with st.expander("📋 View Full Payment Schedule"):
    st.dataframe(df.style.format({
        "Payment": "£{:.2f}",
        "Principal": "£{:.2f}",
        "Interest": "£{:.2f}",
        "Remaining Balance": "£{:.2f}"
    }))

# Footer
# Footer
st.markdown("---")
st.markdown(
    "📌 *Note: This calculator is for informational purposes only and does not constitute financial advice.*"
)
st.markdown(
    "🔗 **Reference**: [Current UK Mortgage Rates – Rightmove](https://www.rightmove.co.uk/news/articles/property-news/current-uk-mortgage-rates/)"
)