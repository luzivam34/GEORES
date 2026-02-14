from app.models.produto_model import Produto
from app.models.movimentacao_model import Movimentacao
from app.extensions import db

def movimentar_estoque(produto_id, tipo, quantidade):
    produto = Produto.query.get(produto_id)

    if not produto:
        return {"erro":"Produto não encontrado"}, 404

    if tipo == "saida" and produto.quantidade < quantidade:
        return {"erro": "Estoque insuficiente"}, 400

    if tipo == "entrada":
        produto.quantidade += quantidade
    else:
        produto.quantidade -= quantidade

    movimentacao = Movimentacao(
        produto_id=produto_id,
        tipo=tipo,
        quantidade=quantidade
    )

    db.session.add(Movimentacao)
    db.session.commit()

    return {"mensagem":"Movimentação realizada com sucesso"}
