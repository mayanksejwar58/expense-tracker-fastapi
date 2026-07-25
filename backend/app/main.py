from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import auth, profile, expense

app = FastAPI(
    title="Expense Tracker API",
    version="1.0.0"
)

# Streamlit runs on a different origin/port, so it needs CORS enabled
# to call this API from the browser.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(profile.router)
app.include_router(expense.router)


@app.get("/")
def home():
    return {
        "status": "success",
        "message": "Expense Tracker Backend Running"
    }
