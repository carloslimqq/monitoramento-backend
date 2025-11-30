from sqlalchemy import Column, Integer, String, DateTime, JSON
from datetime import datetime
from database import Base

class Leitura(Base):
    __tablename__ = "leituras"

    id = Column(Integer, primary_key=True, index=True)
    maquina = Column(String(50), index=True)
    dados = Column(JSON)   # Armazena o JSON inteiro
    timestamp = Column(DateTime, default=datetime.utcnow)

