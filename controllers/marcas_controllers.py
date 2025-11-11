from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from models.celular_model import Marca

marcas_bp = Blueprint("marcas", __name__, url_prefix="/marcas")

@marcas_bp.route("/", methods=["POST"])
def crear_marca():
    data = request.get_json()
    db = SessionLocal()
    try:
        nueva = Marca(nombre=data["nombre"])
        db.add(nueva)
        db.commit()
        db.refresh(nueva)
        return jsonify({"id": nueva.id, "nombre": nueva.nombre}), 201
    finally:
        db.close()
