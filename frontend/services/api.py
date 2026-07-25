import requests
import streamlit as st

BASE_URL = "https://expense-tracker-fastapi-ae9w.onrender.com"

TIMEOUT = 10

def _handle(response: requests.Response) -> dict:
    try:
        return response.json()
    except ValueError:
        return {
            "status": "error",
            "message": f"Unexpected response from server (status {response.status_code})"
        }


def _request(method: str, path: str, auth: bool = False, **kwargs) -> dict:
    headers = kwargs.pop("headers", {})
    if auth:
        token = st.session_state.get("access_token")
        if not token:
            return {"status": "error", "message": "Not logged in"}
        headers["Authorization"] = f"Bearer {token}"
    try:
        response = requests.request(
            method, f"{BASE_URL}{path}", headers=headers, timeout=TIMEOUT, **kwargs
        )
    except requests.exceptions.ConnectionError:
        return {
            "status": "error",
            "message": f"Can't reach the backend at {BASE_URL}. Is it running?"
        }
    except requests.exceptions.Timeout:
        return {"status": "error", "message": "Request timed out. Please try again."}

    if response.status_code == 401:
        return {"status": "error", "message": "Session expired. Please log in again."}

    return _handle(response)


def register(name: str, email: str, password: str) -> dict:
    return _request(
        "POST", "/auth/register",
        json={"name": name, "email": email, "password": password}
    )


def login(email: str, password: str) -> dict:
    return _request(
        "POST", "/auth/login",
        json={"email": email, "password": password}
    )


def get_profile() -> dict:
    return _request("GET", "/profile/", auth=True)


def create_expense(title: str, amount: float, category: str, expense_date: str) -> dict:
    return _request(
        "POST", "/expense/", auth=True,
        json={
            "title": title,
            "amount": amount,
            "category": category,
            "expense_date": expense_date,
        }
    )


def get_expenses(category: str = None, start_date: str = None, end_date: str = None) -> dict:
    params = {}
    if category:
        params["category"] = category
    if start_date:
        params["start_date"] = start_date
    if end_date:
        params["end_date"] = end_date

    return _request("GET", "/expense/", auth=True, params=params)


def update_expense(expense_id: str, **fields) -> dict:
    # Drop unset fields so we only send what changed
    payload = {k: v for k, v in fields.items() if v is not None}
    return _request("PUT", f"/expense/{expense_id}", auth=True, json=payload)


def delete_expense(expense_id: str) -> dict:
    return _request("DELETE", f"/expense/{expense_id}", auth=True)


def get_summary() -> dict:
    return _request("GET", "/expense/summary", auth=True)
