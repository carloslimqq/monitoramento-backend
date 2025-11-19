from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
import models
from pydantic import BaseModel
from typing import List
from datetime import datetime

# cria tabelas se não existirem
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Monitoramento Industrial - Backend")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class TelemetriaOut(BaseModel):
    id: int
    maquina: str
    parametro: str
    valor: float
    timestamp: datetime

    class Config:
        orm_mode = True

@app.get("/")
def read_root():
    return {"status": "Backend rodando!"}

@app.get("/telemetria/recent", response_model=List[TelemetriaOut])
def get_recent(limit: int = 50, db: Session = Depends(get_db)):
    results = db.query(models.Telemetria).order_by(models.Telemetria.timestamp.desc()).limit(limit).all()
    return results

@app.get("/telemetria/by_machine/{maquina}", response_model=List[TelemetriaOut])
def get_by_machine(maquina: str, limit: int = 100, db: Session = Depends(get_db)):
    results = (db.query(models.Telemetria)
                  .filter(models.Telemetria.maquina == maquina)
                  .order_by(models.Telemetria.timestamp.desc())
                  .limit(limit)
                  .all())
    return results
