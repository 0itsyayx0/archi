"""Script de ayuda para listar usuarios registrados.
Usa la configuración de `config/database.py` y los modelos del proyecto.
Ejecutar desde la raíz del proyecto:
    python scripts/print_users.py
"""
import os
import sys
# Asegurar que la raíz del proyecto esté en sys.path para resolver imports relativos
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config.database import SessionLocal
from models.user_model import User


def main():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        if not users:
            print('No hay usuarios registrados.')
            return
        print(f"{len(users)} usuario(s) encontrado(s):")
        for u in users:
            print(f"- id={u.id}, username={u.username}, email={u.email}, role={u.role}")
    except Exception as e:
        print('Error al listar usuarios:', e)
    finally:
        db.close()


if __name__ == '__main__':
    main()
