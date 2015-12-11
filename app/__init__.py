from flask import Flask
from flask_bootstrap import WebCDN
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    app.extensions['bootstrap']['cdns']['jquery'] = WebCDN(
        '//cdn.bootcss.com/jquery/1.11.3/jquery.min.js'
    )
    app.extensions['bootstrap']['cdns']['bootstrap'] = WebCDN(
        '//cdn.bootcss.com/bootstrap/3.3.5/'
    )
    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .qsyk import qsyk as qsyk_blueprint
    app.register_blueprint(qsyk_blueprint)

    return app
