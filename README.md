# 🏭 Factory Production Monitoring System

A full-stack factory production monitoring system built with **FastAPI (Python)** and **React (Vite)**.  
This application tracks worker activity, production units, idle/working time, and provides real-time factory metrics.

---

## 🚀 Features

### Backend (FastAPI)
- Worker metrics calculation (working time, idle time, units produced)
- Factory-level summary metrics
- REST APIs with SQLAlchemy ORM
- Environment-based configuration
- CORS-enabled for frontend integration

### Frontend (React + Vite)
- Dashboard view for factory summary
- Worker metrics table
- Environment-based API configuration
- Clean UI with Tailwind CSS

---

## 🧱 Tech Stack

**Backend**
- Python
- FastAPI
- SQLAlchemy
- SQLite / PostgreSQL
- Uvicorn

**Frontend**
- React
- Vite
- JavaScript
- Tailwind CSS

---

## 📂 Project Display



  
 Screenshot: https://drive.google.com/file/d/1RwvpHKrNLOIGJQYZDb_FVCRA827jCLaf/view?usp=sharing




pip install -r requirements.txt
Set up the database (SQLite example):

# Create the database
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"
Running the API

uvicorn app.main:app --reload
API will run at: http://127.0.0.1:8000

Factory metrics endpoint: /factory/metrics

Worker metrics endpoint: /workers/metrics

Swagger docs: http://127.0.0.1:8000/docs

Example Usage
Fetch Factory Metrics

curl http://127.0.0.1:8000/factory/metrics
Response:

json
Copy code
{
  "total_productive_hours": 120.5,
  "total_units": 450,
  "avg_utilization": 85.7
}
Fetch Worker Metrics

curl http://127.0.0.1:8000/workers/metrics
Response:

json
Copy code
{
  "1": {"working_seconds": 3600, "idle_seconds": 600, "units": 50, "utilization": 85.71},
  "2": {"working_seconds": 4000, "idle_seconds": 500, "units": 60, "utilization": 88.9}
}
Frontend Integration
Enable CORS in main.py:


from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

👨‍💻 Author

Anil Kumar
