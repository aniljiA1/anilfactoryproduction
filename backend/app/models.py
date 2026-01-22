from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Worker(Base):
    __tablename__ = "workers"
    id = Column(String, primary_key=True)
    name = Column(String)

class Workstation(Base):
    __tablename__ = "workstations"
    id = Column(String, primary_key=True)
    name = Column(String)

class Event(Base):
    __tablename__ = "events"
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime)
    worker_id = Column(String, ForeignKey("workers.id"))
    workstation_id = Column(String, ForeignKey("workstations.id"))
    event_type = Column(String)
    confidence = Column(Float)
    count = Column(Integer, default=0)
