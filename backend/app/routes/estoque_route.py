from flask import Blueprint, request, jsonify
from app.services.estoque_service import movimentar_estoque

estoque_bp = Blueprint("estoque", __name__, url_prefix="/api/v1/estoque")

@estoque_bp.route("/movimentar", methods=["POST"])
def movimentar():
    data = request.get_json()
    resposta = movimentar_estoque(
        data["produto_id"],
        data["tipo"],
        data["quantidade"]
    )
    return jsonify(resposta)
