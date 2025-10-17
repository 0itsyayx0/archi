import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from models.file_model import File, Box
from sqlalchemy.orm import Session
 
class FileRepository:
    """
    Repositorio para la gestión de documentos físicos en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar archivos,
    así como para interactuar con las cajas asociadas a cada documento.
    """
 
    def __init__(self, db_session: Session):
        self.db = db_session
 
    def get_all_files(self):
        """
        Recupera todos los documentos almacenados en la base de datos.
        Utiliza una consulta ORM para obtener todas las instancias de la clase File.
        """
        logger.info("Obteniendo todos los archivos desde el repositorio")
        return self.db.query(File).all()
 
    def get_file_by_id(self, file_id: int):
        """
        Busca y retorna un documento específico según su ID.
        """
        logger.info(f"Buscando archivo por ID: {file_id}")
        return self.db.query(File).filter(File.id == file_id).first()
 
    def create_file(self, document_id: str, pages: int, date, box_number: str, box_id: int, user_id: int):
        """
        Crea y almacena un nuevo documento en la base de datos.
        """
        logger.info(f"Creando archivo: {document_id}")
        new_file = File(
            document_id=document_id,
            pages=pages,
            date=date,
            box_number=box_number,
            box_id=box_id,
            user_id=user_id
        )
        self.db.add(new_file)
        self.db.commit()
        self.db.refresh(new_file)
        return new_file
 
    def update_file(self, file_id: int, data: dict):
        """
        Actualiza la información de un documento existente.
        Permite modificar cualquier campo del archivo si está presente en el diccionario 'data'.
        """
        file = self.get_file_by_id(file_id)
        if file:
            logger.info(f"Actualizando archivo: {file_id}")
            for key, value in data.items():
                if hasattr(file, key):
                    setattr(file, key, value)
            self.db.commit()
            self.db.refresh(file)
        else:
            logger.warning(f"Archivo no encontrado para actualizar: {file_id}")
        return file
 
    def delete_file(self, file_id: int):
        """
        Elimina un documento de la base de datos según su ID.
        """
        file = self.get_file_by_id(file_id)
        if file:
            logger.info(f"Eliminando archivo: {file_id}")
            self.db.delete(file)
            self.db.commit()
        else:
            logger.warning(f"Archivo no encontrado para eliminar: {file_id}")
        return file