from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    

    @app.route("/")
    def hello_world():
        return "<p>helo world :3</p>"
    
    return app

from app import models
