from flask import Flask


def create_app():
    app = Flask(__name__)

    from .routes.estoque_route import estoque_bp
    from .routes.produto_route import produto_bp

    app.register_blueprint(estoque_bp)
    app.register_blueprint(produto_bp)

    return app
