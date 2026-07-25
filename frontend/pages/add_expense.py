from datetime import date
import streamlit as st
from services import api

st.set_page_config(page_title="Add Expense", page_icon="➕")

if not st.session_state.get("access_token"):
    st.warning("Please log in first.")
    st.stop()

st.title("➕ Add Expense")

CATEGORIES = [
    "Food & Dining", "Transportation", "Shopping", "Entertainment",
    "Bills & Utilities", "Health", "Travel", "Groceries", "Other"
]

with st.form("add_expense_form", clear_on_submit=True):
    title = st.text_input("Title", placeholder="e.g. Lunch with team")
    amount = st.number_input("Amount", min_value=0.01, step=1.0, format="%.2f")
    category = st.selectbox("Category", CATEGORIES)
    expense_date = st.date_input("Date", value=date.today())

    submitted = st.form_submit_button("Add Expense", use_container_width=True)

    if submitted:
        if not title.strip():
            st.error("Please enter a title.")
        else:
            with st.spinner("Saving..."):
                result = api.create_expense(
                    title.strip(), amount, category, str(expense_date)
                )
            if result.get("status") == "success":
                st.success(f"Added '{title}' — ${amount:.2f}")
            else:
                st.error(result.get("message", "Could not add expense."))
