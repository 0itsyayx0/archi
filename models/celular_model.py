from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Marca(Base):
    __tablename__ = 'marcas'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)

    celulares = relationship('Celular', back_populates='marca', cascade='all, delete-orphan')

class Celular(Base):
    __tablename__ = 'celulares'
    id = Column(Integer, primary_key=True, index=True)
    modelo = Column(String(255), nullable=False)
    precio = Column(Float, nullable=False)

    marca_id = Column(Integer, ForeignKey('marcas.id'))
    marca = relationship('Marca', back_populates='celulares')
