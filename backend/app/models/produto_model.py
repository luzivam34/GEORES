from app.extensions import db

class Produto(db.Model):
    __tablename__ = "produtos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    descricao = db.Column(db.Text)
    preco = db.Column(db.Numeric(10,2), nullable=False)
    quantidade = db.Column(db.Integer, default=0)
    categoria_id = db.Column(db.Integer, db.ForeignKey("categorias.id"))
    ativo = db.Column(db.Boolean, default=True)
    criado_em = db.Column(db.DateTime, default=db.func.current_timestamp)
