from app.extensions import db

class Movimentacao(db.Model):
    __tablename__ = "movimentacoes"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuarios.id"))
    tipo = db.Column(db.String(10))
    quantidade = db.Column(db.Integer)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp())
