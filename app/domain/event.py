import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from app.database import Base


class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    guid = Column(String, unique=True, index=True)
    dim_id_1 = Column(Integer, index=True)
    dim_type_1 = Column(Integer, index=True)
    dim_id_2 = Column(Integer, index=True)
    dim_type_2 = Column(Integer, index=True)
    dim_id_3 = Column(Integer, index=True)
    dim_type_3 = Column(Integer, index=True)
    ecategory = Column(String)
    etype = Column(String)
    especies = Column(String)
    date_created = Column(DateTime, default=datetime.datetime.utcnow)
    date_negated = Column(DateTime)
