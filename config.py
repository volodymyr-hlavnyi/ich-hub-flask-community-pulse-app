class Config:
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

class DeveloperConfig(Config):
    Debug = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

class Testing(Config):
    Debug = True
    Testing = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

