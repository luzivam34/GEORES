from flask import Blueprint, request, jsonify
from app.services.produto_service import criar_produto

produto_bp = Blueprint("produtos", __name__, url_prefix="/api/v1/produtos")

@produto_bp.route('/', methods=["POST"])
def criar():
    data = request.get_json()
    produto = criar_produto(data)

    return jsonify({
        "sucesso": True,
        "data": {
            "id": produto.id,
            "nome": produto.nome
        }
    }), 201
