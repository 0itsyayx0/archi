import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from flask import Blueprint, request, jsonify
from services.file_service import FileService
from flask_jwt_extended import jwt_required
 
file_bp = Blueprint('file_bp', __name__)
 
# Importar la sesión de la base de datos desde config/database.py
from config.database import get_db_session
 
# Instancia global del servicio
service = FileService(get_db_session())
 
@file_bp.route('/files', methods=['GET'])
@jwt_required()
def get_files():
    """
    GET /files
    Recupera y retorna todos los archivos registrados en el sistema.
    """
    logger.info("Consulta de todos los archivos")
    files = service.listar_archivos()
    return jsonify([
        {
            'id': f.id,
            'document_id': f.document_id,
            'pages': f.pages,
            'date': f.date.isoformat(),
            'box_number': f.box_number,
            'box_id': f.box_id
        } for f in files
    ]), 200, {'Content-Type': 'application/json; charset=utf-8'}
 
@file_bp.route('/files/<int:file_id>', methods=['GET'])
@jwt_required()
def get_file(file_id):
    """
    GET /files/<file_id>
    Recupera la información de un archivo específico por su ID.
    """
    file = service.obtener_archivo(file_id)
    if file:
        logger.info(f"Consulta de archivo por ID: {file_id}")
        return jsonify({
            'id': file.id,
            'document_id': file.document_id,
            'pages': file.pages,
            'date': file.date.isoformat(),
            'box_number': file.box_number,
            'box_id': file.box_id
        }), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Archivo no encontrado: {file_id}")
    return jsonify({'error': 'Archivo no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}
 
@file_bp.route('/files', methods=['POST'])
@jwt_required()
def create_file():
    """
    POST /files
    Crea un nuevo registro de archivo.
    Parámetros esperados (JSON):
        document_id (str)
        pages (int)
        date (str, formato ISO)
        box_number (str)
        box_id (str)
    """
    data = request.get_json()
    required_fields = ['document_id', 'pages', 'date', 'box_number', 'box_id']
    if not all(field in data for field in required_fields):
        logger.warning("Faltan campos obligatorios para crear archivo")
        return jsonify({'error': 'Todos los campos son obligatorios'}), 400, {'Content-Type': 'application/json; charset=utf-8'}
 
    file = service.crear_archivo(
        document_id=data['document_id'],
        pages=data['pages'],
        date=data['date'],
        box_number=data['box_number'],
        box_id=data['box_id']
    )
    logger.info(f"Archivo creado: {file.document_id}")
    return jsonify({'id': file.id}), 201, {'Content-Type': 'application/json; charset=utf-8'}
 
@file_bp.route('/files/<int:file_id>', methods=['PUT'])
@jwt_required()
def update_file(file_id):
    """
    PUT /files/<file_id>
    Actualiza la información de un archivo existente.
    """
    data = request.get_json()
    file = service.actualizar_archivo(file_id, data)
    if file:
        logger.info(f"Archivo actualizado: {file_id}")
        return jsonify({'message': 'Archivo actualizado'}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Archivo no encontrado para actualizar: {file_id}")
    return jsonify({'error': 'Archivo no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}
 
@file_bp.route('/files/<int:file_id>', methods=['DELETE'])
@jwt_required()
def delete_file(file_id):
    """
    DELETE /files/<file_id>
    Elimina un archivo específico por su ID.
    """
    file = service.eliminar_archivo(file_id)
    if file:
        logger.info(f"Archivo eliminado: {file_id}")
        return jsonify({'message': 'Archivo eliminado'}), 200, {'Content-Type': 'application/json; charset=utf-8'}
    logger.warning(f"Archivo no encontrado para eliminar: {file_id}")
    return jsonify({'error': 'Archivo no encontrado'}), 404, {'Content-Type': 'application/json; charset=utf-8'}