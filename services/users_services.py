import logging
from repositories.users_repository import UserRepository
from models.users_model import User
from werkzeug.security import generate_password_hash, check_password_hash
 
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
 
class UsersService:
    def __init__(self, db_session):
        self.users_repository = UserRepository(db_session)
 
    def authenticate_user(self, username: str, password: str):
        """
        Verifica las credenciales del usuario y retorna el usuario si son válidas.
        """
        user = self.users_repository.get_user_by_username(username)
        logger.info(f"Authenticating user: {username}")
        if user and check_password_hash(user.password, password):
            logger.info(f"User authenticated successfully: {username}")
            return user
        logger.warning(f"Failed authentication attempt: {username}")
        return None
 
    def get_all_users(self):
        """
        Retorna todos los usuarios registrados.
        """
        logger.info("Fetching all users")
        return self.users_repository.get_all_users()
 
    def get_user_by_id(self, user_id: int):
        """
        Retorna un usuario por su ID.
        """
        logger.info(f"Fetching user by ID: {user_id}")
        return self.users_repository.get_user_by_id(user_id)
 
    def create_user(self, username: str, password: str):
        """
        Crea un nuevo usuario con contraseña encriptada.
        """
        password_hashed = generate_password_hash(password)
        logger.info(f"Creating user: {username}")
        return self.users_repository.create_user(username, password_hashed)
 
    def update_user(self, user_id: int, username: str = None, password: str = None):
        """
        Actualiza el nombre de usuario y/o contraseña.
        """
        logger.info(f"Updating user: {user_id}")
        if password:
            password = generate_password_hash(password)
        return self.users_repository.update_user(user_id, username, password)
 
    def delete_user(self, user_id: int):
        """
        Elimina un usuario por su ID.
        """
        logger.info(f"Deleting user: {user_id}")
        return self.users_repository.delete_user(user_id)
 
    # 🔽 Opcionales para gestión de archivos por usuario
 
    def get_user_files(self, user_id: int):
        """
        Retorna todos los archivos registrados por un usuario.
        """
        logger.info(f"Fetching files for user: {user_id}")
        return self.users_repository.get_files_by_user(user_id)
 
    def user_exists(self, username: str):
        """
        Verifica si un usuario ya existe por nombre.
        """
        logger.info(f"Checking if user exists: {username}")
        return self.users_repository.get_user_by_username(username) is not None