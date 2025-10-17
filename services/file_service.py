import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
from repositories.file_repository import FileRepository
from models.file_model import File
from sqlalchemy.orm import Session
 
"""
Librerías utilizadas:
- repositories.file_repository: Proporciona la clase FileRepository para la gestión de archivos en la base de datos.
- models.file_model: Define el modelo File que representa la entidad de documento físico.
- sqlalchemy.orm.Session: Permite manejar la sesión de la base de datos para realizar operaciones transaccionales.
"""
 
class FileService:
    """
    Capa de servicios para la gestión de archivos/documentos físicos.
    Esta clase orquesta la lógica de negocio relacionada con los archivos,
    utilizando el repositorio para acceder a los datos.
    Permite mantener la lógica de negocio separada de la capa de acceso a datos.
    """
 
    def __init__(self, db_session: Session):
        """
        Inicializa el servicio de archivos con una sesión de base de datos y un repositorio de archivos.
        """
        self.repository = FileRepository(db_session)
        logger.info("Servicio de archivos inicializado")
 
    def listar_archivos(self):
        """
        Recupera y retorna todos los archivos registrados en el sistema.
        Utiliza el repositorio para obtener la lista completa de documentos.
        """
        logger.info("Listando todos los archivos")
        return self.repository.get_all_files()
 
    def obtener_archivo(self, file_id: int):
        """
        Busca y retorna un archivo específico por su identificador único (ID).
        Utiliza el repositorio para acceder al documento correspondiente.
        """
        logger.info(f"Obteniendo archivo por ID: {file_id}")
        return self.repository.get_file_by_id(file_id)
 
    def crear_archivo(self, document_id: str, pages: int, date, box_number: str, box_id: int, user_id: int):
        """
        Crea un nuevo archivo con los datos proporcionados.
        Utiliza el repositorio para almacenar el documento en la base de datos.
        """
        logger.info(f"Creando archivo: {document_id}")
        return self.repository.create_file(document_id, pages, date, box_number, box_id, user_id)
 
    def actualizar_archivo(self, file_id: int, data: dict):
        """
        Actualiza la información de un archivo existente.
        Permite modificar cualquier campo del documento si está presente en el diccionario 'data'.
        """
        logger.info(f"Actualizando archivo: {file_id}")
        return self.repository.update_file(file_id, data)
 
    def eliminar_archivo(self, file_id: int):
        """
        Elimina un archivo del sistema según su identificador único (ID).
        Utiliza el repositorio para eliminar el documento de la base de datos.
        """
        logger.info(f"Eliminando archivo: {file_id}")
        return self.repository.delete_file(file_id)