from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# Configure estas variáveis conforme seu ambiente
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "sua_senha")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_NAME = os.getenv("DB_NAME", "monitoramento")

SQLALCHEMY_DATABASE_URL = f"mysql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

# engine e session
engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
