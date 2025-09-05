from config.config import Base, engine
from models.band_model import Producto

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

print("✅ Tablas creadas correctamente en la base de datos")