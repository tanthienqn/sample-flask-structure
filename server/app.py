from flask import Flask
from extensions import jwt, db, storage, health
from server.config import app_config
from flask_cors import CORS
from server.controlers import SampleControler


def create_app(env_name):
    # Create Flask server load server.config
    app = Flask(__name__)
    CORS(app)
    app.config.from_object(app_config[env_name])
    # Initialize DB
    db.init_app(app)
    # Initialize storage
    storage.init_app(app)
    # Initialize Flask-JWT-Extended
    jwt.init_app(app)
    # config upload large file
    app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024
    # VNP
    app.register_blueprint(SampleControler.sample_api, url_prefix='/sample-service/sample')
    # healthcheck
    app.add_url_rule("/sample-service/healthcheck", "healthcheck", view_func=lambda: health.run())
    app.app_context().push()
    return app
