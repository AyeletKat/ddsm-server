from flask import Flask
from App.config import config
from App.utils import SeriesManager, DataManager
from App.config import Config

series_mng = SeriesManager()
data_mng = DataManager()
config = Config()

def create_app():
    app = Flask(__name__)
    register_blueprints(app)
    DataManager()
    return app

def register_blueprints(app):
    from App.filter.routes import filter_bp
    app.register_blueprint(filter_bp, url_prefix='/filter')

    from App.image.routes import images_bp
    app.register_blueprint(images_bp, url_prefix='/images')

    from App.patient.routes import patients_bp
    app.register_blueprint(patients_bp, url_prefix='/patients')


# def configure_database():
#     series_mng.start(config)
#     data_mng.start(config)
