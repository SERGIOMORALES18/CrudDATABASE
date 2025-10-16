from sqlalchemy.orm import Session
from models.inventario_model import Inventario

class InventarioRepository:
    def __init__(self, db_session: Session):
        self.db = db_session

    def get_all_items(self):
        return self.db.query(Inventario).all()

    def get_item_by_id(self, item_id: int):
        return self.db.query(Inventario).filter(Inventario.id == item_id).first()

    def create_item(self, nombre: str, cantidad: int):
        new_item = Inventario(nombre=nombre, cantidad=cantidad)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def update_item(self, item_id: int, nombre: str = None, cantidad: int = None):
        item = self.get_item_by_id(item_id)
        if item:
            if nombre:
                item.nombre = nombre
            if cantidad is not None:
                item.cantidad = cantidad
            self.db.commit()
            self.db.refresh(item)
        return item

    def delete_item(self, item_id: int):
        item = self.get_item_by_id(item_id)
        if item:
            self.db.delete(item)
            self.db.commit()
        return item