from flask import Flask
from config import Config
from app.extensions import db, migrate

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.estoque_route import estoque_bp
    from .routes.produto_route import produto_bp

    app.register_blueprint(estoque_bp)
    app.register_blueprint(produto_bp)

    with app.app_context():
        db.create_all()

    return app
