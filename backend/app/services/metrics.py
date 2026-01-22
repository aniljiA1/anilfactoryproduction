from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.models import Event

def compute_worker_metrics(db: Session):
    # Fetch all events ordered by worker and timestamp
    events = (
        db.query(Event)
        .order_by(Event.worker_id, Event.timestamp)
        .all()
    )

    metrics = {}

    for event in events:
        wid = event.worker_id
        metrics.setdefault(wid, {
            "working_seconds": 0.0,
            "idle_seconds": 0.0,
            "units": 0,
            "last_event": None,
        })

        m = metrics[wid]

        # Make timestamp timezone-aware if it's naive
        ts = event.timestamp
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)

        if m["last_event"]:
            prev = m["last_event"]

            # Ensure previous timestamp is also timezone-aware
            prev_ts = prev.timestamp
            if prev_ts.tzinfo is None:
                prev_ts = prev_ts.replace(tzinfo=timezone.utc)

            delta = (ts - prev_ts).total_seconds()

            if prev.event_type == "working":
                m["working_seconds"] += delta
            elif prev.event_type == "idle":
                m["idle_seconds"] += delta

        # Count products
        if event.event_type == "product_count":
            m["units"] += event.count or 0

        # Save current event as last_event for next iteration
        m["last_event"] = event

    # Prepare final clean result (remove last_event)
    result = {}
    for wid, m in metrics.items():
        total = m["working_seconds"] + m["idle_seconds"]
        utilization = (m["working_seconds"] / total * 100) if total > 0 else 0

        result[wid] = {
            "working_seconds": round(m["working_seconds"], 2),
            "idle_seconds": round(m["idle_seconds"], 2),
            "units": m["units"],
            "utilization": round(utilization, 2),
        }

    return result
