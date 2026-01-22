from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Event
from app.services.metrics import compute_worker_metrics

router = APIRouter(prefix="/factory", tags=["Factory"])

@router.get("/metrics")
def factory_metrics(db: Session = Depends(get_db)):
    workers = compute_worker_metrics(db)  # pass DB session, NOT events

    total_working = sum(w["working_seconds"] for w in workers.values())
    total_units = sum(w["units"] for w in workers.values())
    avg_utilization = round(
        sum(w["utilization"] for w in workers.values()) / len(workers),
        2
    ) if workers else 0

    return {
        "total_productive_hours": round(total_working / 3600, 2),
        "total_units": total_units,
        "avg_utilization": avg_utilization
    }
