from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from models import Leitura
from mqtt_client import start_mqtt

Base.metadata.create_all(bind=engine)

app = FastAPI()

mqtt_client = start_mqtt()

@app.get("/")
def raiz():
    return {"mensagem": "API de Monitoramento Industrial ativa!"}

@app.get("/leituras")
def listar(maquina: str = None, db: Session = Depends(get_db)):
    query = db.query(Leitura)
    if maquina:
        query = query.filter(Leitura.maquina == maquina)
    return query.order_by(Leitura.id.desc()).all()

@app.get("/leituras/{id}")
def buscar(id: int, db: Session = Depends(get_db)):
    return db.query(Leitura).filter(Leitura.id == id).first()
