import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or '87V8gJ727bVD82C3z5J8q6n6S3A64Z2a'
    AES_KEY = '87V8gJ727bVD82C3z5J8q6n6S3A64Z2a'

    @staticmethod
    def init_app(app):
        pass


class ProductionConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True


config = {
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': ProductionConfig
}
