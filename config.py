class Config:
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'

class DeveloperConfig(Config):
    Debug = True

class Testing(Config):
    Debug = True
    Testing = True

