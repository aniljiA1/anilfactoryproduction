from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import engine, SessionLocal
from app.models import Base
from app.seed import seed_data
from app.routers import events, workers, workstations, factory



app = FastAPI(title="AI Productivity Dashboard")



origins = [
    "http://localhost:5173",  # your React app
    "http://127.0.0.1:5173", # optional, in case Vite uses this
    "https://anilfactoryproduction.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # can also be ["*"] for development
    allow_credentials=True,
    allow_methods=["*"],  # allow GET, POST, etc.
    allow_headers=["*"],  # allow all headers
)

Base.metadata.create_all(bind=engine)

@app.on_event("startup")
def startup():
    db = SessionLocal()
    seed_data(db)
    db.close()

app.include_router(events.router)
app.include_router(workers.router)
app.include_router(workstations.router)
app.include_router(factory.router)
