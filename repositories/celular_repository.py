from models.celular_model import Celular, Console
from sqlalchemy.orm import Session

class CelularRepository:
    """
    Repositorio para la gestión de videojuegos en la base de datos.
    Proporciona métodos para crear, consultar, actualizar y eliminar videojuegos,
    así como para gestionar la relación con las consolas.
    """

    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_games(self):

        """
        Gameservice
        Recupera todos los videojuegos almacenados en la base de datos.
        Retorna una lista de objetos Game.
        """
        return self.db.query(Celular).all()

    def get_game_by_id(self, game_id: int):
        """
        Busca y retorna un videojuego específico según su ID.
        Devuelve la instancia de Game si existe, o None si no se encuentra.
        """
        return self.db.query(Celular).filter(Celular.id == game_id).first()

    def create_game(self, modelo: str, price: float, marca_id: int):
        """
        Crea y almacena un nuevo videojuego en la base de datos.
        Parámetros:
            modelo (str): Título del videojuego.
            price (float): Precio del videojuego.
            marca_id (int): ID de la consola a la que pertenece.
        Retorna la instancia de Game creada.
        """
        new_game = Celular(modelo=modelo, price=price, marca_id=marca_id)
        self.db.add(new_game)
        self.db.commit()
        self.db.refresh(new_game)
        return new_game

    def update_game(self, game_id: int, modelo: str = None, price: float = None, marca_id: int = None):
        """
        Actualiza los datos de un videojuego existente en la base de datos.
        Permite modificar el título, precio o consola de un videojuego.
        Retorna la instancia actualizada o None si no existe.
        """
        game = self.get_game_by_id(game_id)
        if game:
            if modelo:
                game.modelo = modelo
            if price is not None:
                game.price = price
            if marca_id:
                game.console_id = marca_id
            self.db.commit()
            self.db.refresh(game)
        return game

    def delete_game(self, game_id: int):
        """
        Elimina un videojuego de la base de datos según su ID.
        Retorna la instancia eliminada o None si no existe.
        """
        game = self.get_game_by_id(game_id)
        if game:
            self.db.delete(game)
            self.db.commit()
        return game
