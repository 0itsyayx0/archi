from flask import Blueprint, request, jsonify
from config.database import SessionLocal
from models.celular_model import Celular

# Blueprint para las rutas de celulares
celulares_bp = Blueprint("celulares", __name__, url_prefix="/celulares")
@celulares_bp.before_request
def handle_options():
    if request.method == 'OPTIONS':
        return '', 200


# GET todos
@celulares_bp.route("/", methods=["GET"])
def listar_celulares():
    db = SessionLocal()
    try:
        celulares = db.query(Celular).all()
        return jsonify([
            {"id": c.id, "modelo": c.modelo, "precio": c.precio, "marca_id": c.marca_id}
            for c in celulares
        ])
    finally:
        db.close()

# GET por ID
@celulares_bp.route("/<int:celular_id>", methods=["GET"])
def obtener_celular(celular_id):
    db = SessionLocal()
    try:
        celular = db.query(Celular).filter(Celular.id == celular_id).first()
        if not celular:
            return jsonify({"error": "Celular no encontrado"}), 404
        return jsonify({"id": celular.id, "modelo": celular.modelo, "precio": celular.precio, "marca_id": celular.marca_id})
    finally:
        db.close()

# POST crear
@celulares_bp.route("/", methods=["POST"])
def crear_celular():
    data = request.get_json()
    modelo = data.get("modelo")
    precio = data.get("precio")
    marca_id = data.get("marca_id")

    if not modelo or not precio or not marca_id:
        return jsonify({"error": "Faltan datos"}), 400

    db = SessionLocal()
    try:
        nuevo = Celular(modelo=modelo, precio=precio, marca_id=marca_id)
        db.add(nuevo)
        db.commit()
        db.refresh(nuevo)
        return jsonify({"id": nuevo.id, "modelo": nuevo.modelo}), 201
    finally:
        db.close()


# DELETE eliminar
@celulares_bp.route("/<int:celular_id>", methods=["DELETE"])
def eliminar_celular(celular_id):
    db = SessionLocal()
    try:
        celular = db.query(Celular).filter(Celular.id == celular_id).first()
        if not celular:
            return jsonify({"error": "Celular no encontrado"}), 404
        db.delete(celular)
        db.commit()
        return jsonify({"message": "Celular eliminado"})
    finally:
        db.close()

# PUT actualizar
@celulares_bp.route("/<int:celular_id>", methods=["PUT"])
def actualizar_celular(celular_id):
    data = request.get_json()
    db = SessionLocal()
    try:
        celular = db.query(Celular).filter(Celular.id == celular_id).first()
        if not celular:
            return jsonify({"error": "Celular no encontrado"}), 404
        celular.modelo = data.get("modelo", celular.modelo)
        celular.precio = data.get("precio", celular.precio)
        celular.marca_id = data.get("marca_id", celular.marca_id)
        db.commit()
        db.refresh(celular)
        return jsonify({
            "id": celular.id,
            "modelo": celular.modelo,
            "precio": celular.precio,
            "marca_id": celular.marca_id
        })
    finally:
        db.close()

