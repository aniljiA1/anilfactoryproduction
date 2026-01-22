from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import EventCreate
from app.services.ingestion import ingest_event

router = APIRouter(prefix="/events", tags=["Events"])

@router.post("/ingest")
def ingest(event: EventCreate, db: Session = Depends(get_db)):
    ingest_event(db, event)
    return {"status": "event ingested"}
