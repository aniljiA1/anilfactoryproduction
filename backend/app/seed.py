from datetime import datetime, timedelta, timezone
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Worker, Workstation, Event


def seed_data(db: Session):
    db.query(Event).delete()
    db.query(Worker).delete()
    db.query(Workstation).delete()
    db.commit()

    workers = [Worker(id=f"W{i}", name=f"Worker {i}") for i in range(1, 7)]
    stations = [Workstation(id=f"S{i}", name=f"Station {i}") for i in range(1, 7)]

    db.add_all(workers + stations)
    db.commit()

    now = datetime.now(timezone.utc)
    events = []

    for i in range(6):
        worker_id = f"W{i+1}"
        station_id = f"S{i+1}"

        # Working start
        events.append(Event(
            timestamp=now - timedelta(minutes=60),
            worker_id=worker_id,
            workstation_id=station_id,
            event_type="working",
            confidence=0.95
        ))

        # Still working (important for time continuity)
        events.append(Event(
            timestamp=now - timedelta(minutes=30),
            worker_id=worker_id,
            workstation_id=station_id,
            event_type="working",
            confidence=0.95
        ))

        # Product count (does NOT affect time)
        events.append(Event(
            timestamp=now - timedelta(minutes=20),
            worker_id=worker_id,
            workstation_id=station_id,
            event_type="product_count",
            count=15,
            confidence=0.9
        ))

        # Idle
        events.append(Event(
            timestamp=now,
            worker_id=worker_id,
            workstation_id=station_id,
            event_type="idle",
            confidence=0.92
        ))

    db.add_all(events)
    db.commit()


if __name__ == "__main__":
    db = SessionLocal()
    try:
        seed_data(db)
        print("✅ Database seeded successfully")
    finally:
        db.close()
