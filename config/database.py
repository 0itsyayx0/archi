import os
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv
logging.basicConfig(level=logging.INFO)

# Añadir la raíz del proyecto al sys.path para que los imports funcionen correctamente
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.celular_model import Base
# Asegurar que todos los modelos estén importados para que SQLAlchemy los registre
import models.user_model
import models.revoked_token_model
import models.celular_model

# Cargar variables de entorno desde .env
load_dotenv()

MYSQL_URI = os.getenv('MYSQL_URI')
SQLITE_URI = 'sqlite:///celulares_local.db'

def get_engine():
    """
    Intenta crear una conexión con MySQL. Si falla, usa SQLite local.
    """
    if MYSQL_URI:
        try:
            engine = create_engine(MYSQL_URI, echo=True)
            # Probar conexión
            conn = engine.connect()
            conn.close()
            logging.info('Conexión a MySQL exitosa.')
            return engine
        except OperationalError:
            logging.warning('No se pudo conectar a MySQL. Usando SQLite local.')
    # Fallback a SQLite
    engine = create_engine(SQLITE_URI, echo=True)
    return engine


engine = get_engine()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = SessionLocal
Base.metadata.create_all(engine)


def get_db_session():
    """
    Retorna una nueva sesión de base de datos para ser utilizada en los servicios o controladores.
    """
    return SessionLocal()
