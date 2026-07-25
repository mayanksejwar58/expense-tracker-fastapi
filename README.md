# Expense Tracker API

A full-stack Expense Tracker application built using FastAPI, Streamlit, and Supabase. The application allows users to securely manage their daily expenses with JWT authentication and a clean dashboard.

## Features

- User Registration
- User Login
- JWT Authentication
- Secure Password Hashing (bcrypt)
- User Profile
- Add Expense
- View Expenses
- Update Expense
- Delete Expense
- Filter Expenses by Category and Date
- Expense Summary Dashboard
- REST API Documentation
- Deployed on Render

## Tech Stack

### Backend
- FastAPI
- Python
- Supabase (PostgreSQL)
- JWT Authentication
- bcrypt
- Uvicorn

### Frontend
- Streamlit

### Deployment
- Render

## Project Structure

```
ExpenseTracker/
│
├── backend/
│   ├── app/
│   ├── routers/
│   ├── services/
│   ├── repositories/
│   ├── schemas/
│   ├── models/
│   ├── utils/
│   └── main.py
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   └── services/
│
├── README.md
├── requirements.txt
└── .gitignore
```

## Live Demo

Frontend:
YOUR FRONTEND URL

Backend:
YOUR BACKEND URL

API Documentation:
YOUR_BACKEND_URL/docs

## Installation

```bash
git clone <repository-url>

cd ExpenseTracker
```

Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Frontend

```bash
cd frontend
pip install -r requirements.txt
streamlit run app.py
```

## API Endpoints

Authentication

- POST /auth/register
- POST /auth/login

Profile

- GET /profile

Expenses

- GET /expense
- POST /expense
- PUT /expense/{id}
- DELETE /expense/{id}

Summary

- GET /expense/summary

## Author

Mayank Sejwar