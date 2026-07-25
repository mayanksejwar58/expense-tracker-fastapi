from datetime import date, timedelta
import pandas as pd
import streamlit as st
from services import api

st.set_page_config(page_title="All Expenses", page_icon="📋", layout="wide")

if not st.session_state.get("access_token"):
    st.warning("Please log in first.")
    st.stop()

st.title("📋 All Expenses")

CATEGORIES = [
    "All", "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Health", "Travel", "Groceries", "Other"
]

col1, col2, col3 = st.columns(3)
with col1:
    category_filter = st.selectbox("Category", CATEGORIES)
with col2:
    start_date = st.date_input("From", value=date.today() - timedelta(days=30))
with col3:
    end_date = st.date_input("To", value=date.today())

result = api.get_expenses(
    category=None if category_filter == "All" else category_filter,
    start_date=str(start_date),
    end_date=str(end_date),
)

if result.get("status") != "success":
    st.error(result.get("message", "Could not load expenses."))
    st.stop()

expenses = result["data"]

if not expenses:
    st.info("No expenses found for this filter. Try widening the date range.")
    st.stop()

df = pd.DataFrame(expenses)
total = df["amount"].sum()
st.metric("Total for this view", f"${total:,.2f}")

st.divider()

for expense in expenses:
    c1, c2, c3, c4, c5 = st.columns([3, 1.5, 1.5, 1.5, 1])
    c1.write(f"**{expense['title']}**")
    c2.write(expense["category"])
    c3.write(expense["expense_date"])
    c4.write(f"${expense['amount']:,.2f}")
    if c5.button("Delete", key=f"del_{expense['id']}"):
        del_result = api.delete_expense(expense["id"])
        if del_result.get("status") == "success":
            st.rerun()
        else:
            st.error(del_result.get("message", "Could not delete expense."))
