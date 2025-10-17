import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db import Base
 
"""
La clase User representa a un usuario del sistema.
Cada instancia corresponde a un auxiliar que puede registrar documentos.
Incluye:
- Nombre de usuario único
- Contraseña (en formato hash)
- Relación con los archivos que ha registrado
"""
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
 
    files = relationship('File', back_populates='user', cascade='all, delete-orphan')