import logging
import os

from flask import Flask
from config import config

app = Flask(__name__)

app.logger.setLevel(logging.DEBUG)
app.logger.debug('this will show in the log')
app.config['SECRET_KEY'] = 'asdasxczxc123sdzxcwaf23dasd!'
log_error = app.logger.error
log_info = app.logger.info


def create_app(env="default"):
    config_name = env
    app.config.from_object(config[config_name])

    config[config_name].init_app(app)

    from .service import service as service_blueprint
    app.register_blueprint(service_blueprint, url_prefix='/')
    return app