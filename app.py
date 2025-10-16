
from flask import Flask
from config.config import Base, engine
from models.producto_model import Producto

from controllers.user_controller import user_bp
try:
    from controllers.auth_controller import auth_bp
except ImportError:
    auth_bp = None

from flask_jwt_extended import JWTManager

# Crear tablas si no existen
Base.metadata.create_all(bind=engine)

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret-key'  # Cambia esto por una clave segura en producción
jwt = JWTManager(app)

# Registrar blueprints
app.register_blueprint(user_bp)
if auth_bp:
    app.register_blueprint(auth_bp)

if __name__ == "__main__":
    app.run(debug=True)