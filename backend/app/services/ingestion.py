from sqlalchemy.orm import Session
from app.models import Event
from app.schemas import EventCreate

def ingest_event(db: Session, event: EventCreate):
    db_event = Event(**event.dict())
    db.add(db_event)
    db.commit()
    db.refresh(db_event)
    return db_event
