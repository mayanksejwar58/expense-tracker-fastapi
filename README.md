# 💰 Expense Tracker API

A full-stack **Expense Tracker Application** built using **FastAPI, Streamlit, and Supabase**. It enables users to securely manage expenses using JWT authentication, cloud database integration, and a clean dashboard interface.

---

## 🚀 Features

### Authentication

- User Registration
- Secure Login
- JWT Authentication
- Password Hashing using bcrypt
- User Profile

### Expense Management

- Add Expense
- View Expenses
- Update Expense
- Delete Expense
- Filter Expenses by Category
- Filter Expenses by Date
- Expense Summary Dashboard

### Backend

- RESTful API
- Repository-Service Architecture
- Swagger API Documentation

### Deployment

- Backend deployed on Render
- Frontend deployed on Streamlit

---

## 🛠 Tech Stack

### Backend

- Python
- FastAPI
- Supabase (PostgreSQL)
- JWT Authentication
- bcrypt
- Uvicorn

### Frontend

- Streamlit

### Deployment

- Render
- Streamlit Community Cloud

---

## 📂 Project Structure

```text
ExpenseTracker/
│
├── backend/
│   ├── app/
│   ├── routers/
│   ├── services/
│   ├── repositories/
│   ├── models/
│   ├── schemas/
│   ├── utils/
│   ├── config/
│   ├── middleware/
│   ├── database/
│   └── main.py
│
├── frontend/
│   ├── app.py
│   ├── pages/
│   └── services/
│
├── README.md
├── LICENSE
├── requirements.txt
└── .gitignore
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/mayanksejwar58/expense-tracker-fastapi.git
```

Move into the project

```bash
cd expense-tracker-fastapi
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

---

## 🌐 Live Demo

### Frontend

Replace with your deployed Streamlit URL.

### Backend

Replace with your deployed Render URL.

### API Documentation

```
YOUR_RENDER_URL/docs
```

---

## 📡 REST API Endpoints

### Authentication

| Method | Endpoint |
|---------|----------|
| POST | /auth/register |
| POST | /auth/login |

### Profile

| Method | Endpoint |
|---------|----------|
| GET | /profile |

### Expenses

| Method | Endpoint |
|---------|----------|
| GET | /expense |
| POST | /expense |
| PUT | /expense/{id} |
| DELETE | /expense/{id} |

### Reports

| Method | Endpoint |
|---------|----------|
| GET | /expense/summary |

---

## 📸 Screenshots

- Login
- Dashboard
- Expense List
- Swagger Documentation

(Add screenshots here)

---

## 🌟 Project Highlights

- FastAPI REST APIs
- JWT Authentication
- Repository-Service Architecture
- Supabase Cloud Database
- Secure Password Storage
- Modular Backend Design
- Cloud Deployment

---

## 🚀 Future Improvements

- Monthly Reports
- Budget Planning
- Charts & Analytics
- CSV Export
- PDF Reports
- Email Notifications

---

## 👨‍💻 Author

**Mayank Sejwar**

B.Tech Artificial Intelligence & Data Science

Madhav Institute of Technology & Science (MITS), Gwalior

GitHub:
https://github.com/mayanksejwar58

---

## 📄 License

This project is licensed under the MIT License.

See the LICENSE file for more information.