from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from .routes import check_infringements
    app.register_blueprint(check_infringements)

    return app