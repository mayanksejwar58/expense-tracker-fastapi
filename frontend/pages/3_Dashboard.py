import pandas as pd
import plotly.express as px
import streamlit as st

from services import api

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="wide")

if not st.session_state.get("access_token"):
    st.warning("Please log in first.")
    st.stop()

st.title("📊 Dashboard")

result = api.get_summary()

if result.get("status") != "success":
    st.error(result.get("message", "Could not load summary."))
    st.stop()

summary = result["data"]

if summary["count"] == 0:
    st.info("No expenses yet. Add one from the 'Add Expense' page to see your dashboard.")
    st.stop()

col1, col2 = st.columns(2)
col1.metric("Total spent", f"${summary['total']:,.2f}")
col2.metric("Number of expenses", summary["count"])

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("By Category")
    cat_df = pd.DataFrame(
        list(summary["by_category"].items()), columns=["Category", "Amount"]
    )
    fig = px.pie(cat_df, names="Category", values="Amount", hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with right:
    st.subheader("By Month")
    month_df = pd.DataFrame(
        list(summary["by_month"].items()), columns=["Month", "Amount"]
    )
    fig = px.bar(month_df, x="Month", y="Amount")
    st.plotly_chart(fig, use_container_width=True)
