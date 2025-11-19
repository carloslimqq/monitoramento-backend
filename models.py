from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.sql import func
from database import Base

class Telemetria(Base):
    __tablename__ = "telemetria"

    id = Column(Integer, primary_key=True, index=True)
    maquina = Column(String(50), index=True)
    parametro = Column(String(50))
    valor = Column(Float)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
