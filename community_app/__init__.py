from flask import Flask
import os
import dotenv
from config import Config, DevelopmentConfig, TestingConfig, ProductionConfig
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

from community_app.routes.questions import question_bp
from community_app.routes.responses import response_bp

dotenv.load_dotenv()

app = Flask(__name__)
app.register_blueprint(question_bp)
app.register_blueprint(response_bp)

config_name = os.environ.get('FLASK_ENV', 'development')

# Определяем соответствующие классы конфигурации на основе значения переменной окружения FLASK_ENV
config_class = {
 'development': DevelopmentConfig,
 'testing': TestingConfig,
 'production': ProductionConfig
}.get(config_name)

# Применяем конфигурацию к приложению
if config_class:
 app.config.from_object(config_class)

def create_app():

    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(question_bp)
    app.register_blueprint(response_bp)

    @app.route('/')
    def home():
        return "Wellcome to the Community Pulse App"

    return app

