"""Script para insertar celulares de ejemplo en la BD.
Ejecutar desde la raíz del proyecto:
    python scripts/insert_sample_phones.py
"""
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.database import SessionLocal
from models.celular_model import Celular, Marca


def main():
    db = SessionLocal()
    try:
        # Crear marcas
        marcas_data = [
            {'nombre': 'Apple'},
            {'nombre': 'Samsung'},
            {'nombre': 'Xiaomi'},
            {'nombre': 'Motorola'},
            {'nombre': 'Nokia'},
            {'nombre': 'OnePlus'},
        ]
        
        marcas = {}
        for marca_data in marcas_data:
            existing = db.query(Marca).filter(Marca.nombre == marca_data['nombre']).first()
            if not existing:
                marca = Marca(nombre=marca_data['nombre'])
                db.add(marca)
                db.flush()
                marcas[marca_data['nombre']] = marca.id
            else:
                marcas[marca_data['nombre']] = existing.id
        
        # Crear celulares
        phones_data = [
            {'modelo': 'iPhone 15 Pro Max', 'precio': 1299.99, 'marca': 'Apple'},
            {'modelo': 'iPhone 15', 'precio': 799.99, 'marca': 'Apple'},
            {'modelo': 'Samsung Galaxy S24', 'precio': 999.99, 'marca': 'Samsung'},
            {'modelo': 'Samsung Galaxy A14', 'precio': 199.99, 'marca': 'Samsung'},
            {'modelo': 'Xiaomi 14 Ultra', 'precio': 899.99, 'marca': 'Xiaomi'},
            {'modelo': 'Xiaomi Redmi Note 13', 'precio': 249.99, 'marca': 'Xiaomi'},
            {'modelo': 'Motorola Edge 50', 'precio': 649.99, 'marca': 'Motorola'},
            {'modelo': 'Motorola G54', 'precio': 299.99, 'marca': 'Motorola'},
            {'modelo': 'OnePlus 12', 'precio': 799.99, 'marca': 'OnePlus'},
            {'modelo': 'Nokia G60', 'precio': 349.99, 'marca': 'Nokia'},
            {'modelo': 'Samsung Galaxy Z Fold 6', 'precio': 1799.99, 'marca': 'Samsung'},
            {'modelo': 'iPhone 14 Pro', 'precio': 999.99, 'marca': 'Apple'},
        ]
        
        count = 0
        for phone_data in phones_data:
            existing = db.query(Celular).filter(Celular.modelo == phone_data['modelo']).first()
            if not existing:
                celular = Celular(
                    modelo=phone_data['modelo'],
                    precio=phone_data['precio'],
                    marca_id=marcas[phone_data['marca']]
                )
                db.add(celular)
                count += 1
        
        db.commit()
        print(f'✓ {count} celulares nuevos insertados')
        print(f'✓ {len(marcas)} marcas registradas')
        
    except Exception as e:
        print(f'Error: {e}')
        db.rollback()
    finally:
        db.close()


if __name__ == '__main__':
    main()
