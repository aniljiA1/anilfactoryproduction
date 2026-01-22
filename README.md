# Factory Worker Metrics API

A FastAPI backend for tracking factory worker productivity, idle time, and units produced. Provides endpoints to fetch **worker-level metrics** and **factory-level summaries**.

## Features

- Calculate per-worker metrics:
  - Working time (seconds)
  - Idle time (seconds)
  - Units produced
  - Utilization (% of productive time)
- Aggregate factory metrics:
  - Total productive hours
  - Total units produced
  - Average utilization
- Handles timezone-aware and naive timestamps.
- Easy integration with frontend applications (React, Vite, etc.)
- CORS enabled for cross-origin requests.

## Tech Stack

- **Backend:** FastAPI, Python 3.11+
- **Database:** SQLAlchemy ORM (compatible with PostgreSQL, MySQL, SQLite)
- **Frontend:** React (example usage included)
- **Other:** Pydantic models, CORS middleware


## Installation

1. Clone the repository:


git clone https://github.com/your-username/factory-metrics-api.git
cd factory-metrics-api
Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
Install dependencies:


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


