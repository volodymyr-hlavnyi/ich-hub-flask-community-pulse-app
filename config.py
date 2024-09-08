class Config:
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True

class ProductionConfig(Config):
    pass
