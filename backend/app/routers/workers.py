from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.services.metrics import compute_worker_metrics

router = APIRouter(prefix="/workers", tags=["Workers"])

@router.get("/metrics")
def worker_metrics(db: Session = Depends(get_db)):
    return compute_worker_metrics(db)
