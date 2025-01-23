from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_redis import FlaskRedis
from config import Config

db = SQLAlchemy()
migrate = Migrate()
redis_client = FlaskRedis()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    redis_client.init_app(app)
    CORS(app)

    # Register blueprints
    from app.routes import api
    app.register_blueprint(api, url_prefix='/api')

    return app
