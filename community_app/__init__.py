from flask import Flask
from config import DeveloperConfig, Testing, Config
import os
import dotenv
from routes.questions import question_bp
from routes.responses import response_bp
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
dotenv.load_dotenv()
config_name = os.getenv("Flask_ENV")

#
# @app.route('/')
# def homepage():
#     return "Welcome, to home page"


config_set_up = {
    'production' : Config,
    'development' : DeveloperConfig,
    'test' : Testing
}.get(config_name)


def create_app():
    app = Flask(__name__)
    db.init_app(app)
    app.config.from_object(DeveloperConfig)
    app.register_blueprint(question_bp)
    app.register_blueprint(response_bp)
