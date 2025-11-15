from repositories.celular_repository import CelularRepository
from models.celular_model import Game
from sqlalchemy.orm import Session


class CelularService:


    def __init__(self, db_session: Session):
        
        self.repository = CelularRepository(db_session)

    def listar_celular(self):

        return self.repository.get_all_Celulares()

    def obtener_celular(self, Celular_id: int):

        return self.repository.get_Celular_by_id(Celular_id)

    def crear_juego(self,marca: str, price: float, marca_id: int):

        return self.repository.create_Celular(marca, price, marca_id)

    def actualizar_juego(self, Celular_id: int, marca: str = None, price: float = None, marca_id: int = None):

        return self.repository.update_game(Celular_id, marca, price, marca_id)

    def eliminar_Celular(self, game_id: int):

        return self.repository.delete_Celular(game_id)
