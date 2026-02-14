from app.extensions import db
from datetime import datetime

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_Key=True)
    nome = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.String(255))
    preco = db.Column(db.Float, nullable=False)
    quantidade = db.Column(db.Integer, default=0)
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
