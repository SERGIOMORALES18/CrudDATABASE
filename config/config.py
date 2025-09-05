import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

# Configurar logs
logging.basicConfig(level=logging.INFO)

# Cargar variables de entorno desde .env
load_dotenv()

# URI de conexión (MySQL primero, fallback SQLite)
MYSQL_URI = os.getenv("MYSQL_URI")   # mysql+mysqlconnector://user:password@localhost:3306/tienda
SQLITE_URI = "sqlite:///bands_local.db"

def get_engine():
    """
    Intenta conectarse a MySQL, si falla usa SQLite local.
    """
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            conn = engine.connect()
            conn.close()
            logging.info("✅ Conexión a MySQL exitosa.")
            return engine
        except OperationalError:
            logging.warning("⚠️ No se pudo conectar a MySQL. Usando SQLite local.")
    return create_engine(SQLITE_URI, echo=True)

# Crear engine y sesión global
engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

def get_db_session():
    """
    Retorna una nueva sesión de base de datos.
    Usar con try/finally o context managers.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
