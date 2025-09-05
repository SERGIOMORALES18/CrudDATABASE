from flask import Blueprint, request, jsonify
from services.band_service import crear_producto, obtener_productos, actualizar_producto, eliminar_producto

band_bp = Blueprint("band", __name__)

@band_bp.route("/crear", methods=["POST"])
def crear():
    data = request.json
    producto = crear_producto(data)
    return jsonify(producto), 201

@band_bp.route("/leer", methods=["GET"])
def leer():
    return jsonify(obtener_productos())

@band_bp.route("/actualizar/<int:id>", methods=["PUT"])
def actualizar(id):
    data = request.json
    return jsonify(actualizar_producto(id, data))

@band_bp.route("/eliminar/<int:id>", methods=["DELETE"])
def eliminar(id):
    return jsonify(eliminar_producto(id))
