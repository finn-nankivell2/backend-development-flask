from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask import Flask
from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    from logging.config import dictConfig

    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s: %(message)s",
                }
            },
            "handlers": {
                "wsgi": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://flask.logging.wsgi_errors_stream",
                    "formatter": "default",
                }
            },
            "root": {"level": "INFO", "handlers": ["wsgi"]},
        }
    )

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    from app.cli import blueprint

    app.register_blueprint(blueprint)

    @app.route("/")
    def hello_world():
        return "<p>hello world :3</p>"

    return app


from . import models  # noqa
