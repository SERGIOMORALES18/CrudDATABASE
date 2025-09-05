
# Importaciones necesarias de SQLAlchemy
from sqlalchemy import Column, Integer, String, Float
from config.config import Base  # Usar la Base global definida en config.py

# Modelo que representa la tabla 'productos' en la base de datos
class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, autoincrement=True)  # Identificador único del producto
    nombre = Column(String(100), nullable=False)                # Nombre del producto
    precio = Column(Float, nullable=False)                      # Precio del producto
    stock = Column(Integer, nullable=False)                     # Cantidad disponible en inventario
