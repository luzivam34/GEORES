from app.extensions import db
from datetime import datetime

class Movimentacao(db.Model):
    __tablename__ = "movimentacoes"

    id = db.Column(db.Integer, primary_key=True)
    produto_id = db.Column(db.Integer, db.ForeignKey("produtos.id"))
    tipo = db.Column(db.String(10))
    quantidade = db.Column(db.Integer)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
