from app.models.produto_model import Produto
from app.extensions import db

def criar_produto(data):
    produto = Produto(
        nome = data["nome"],
        descricao = data.get("descricao"),
        preco = data["preco"],
        quantidade = data.get("quantidade", 0)
    )

    db.session.add(produto)
    db.session.commit()

    return produto
