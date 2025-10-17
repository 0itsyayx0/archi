import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base
 
"""
La clase File representa un documento físico dentro del sistema.
Cada instancia corresponde a un documento específico, almacenando información como:
- ID del documento
- Número de páginas
- Fecha del documento
- Número de caja
- ID de la caja
- Usuario que lo registró
"""
class File(Base):
    __tablename__ = 'files'
    id = Column(Integer, primary_key=True, index=True)
    document_id = Column(String(100), nullable=False)
    pages = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)
    box_number = Column(String(50), nullable=False)
    box_id = Column(Integer, ForeignKey('boxes.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
 
    box = relationship('Box', back_populates='files')
    user = relationship('User', back_populates='files')
 
 
"""
La clase Box representa una caja física que contiene documentos.
Cada instancia corresponde a una caja específica, almacenando su número visible
y la relación con los documentos que contiene.
"""
class Box(Base):
    __tablename__ = 'boxes'
    id = Column(Integer, primary_key=True, index=True)
    number = Column(String(50), nullable=False)
 
    files = relationship('File', back_populates='box', cascade='all, delete-orphan')