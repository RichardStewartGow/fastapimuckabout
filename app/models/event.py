from app.database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

class Event(Base):
    __tablename__ = "event"

    id = Column(Integer, primary_key=True)
    guid = Column(String, unique=True, index=True)