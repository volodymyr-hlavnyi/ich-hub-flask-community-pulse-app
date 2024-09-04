class Config:
    Debug = False
    Testing = False
    SQLALCHEMY_DATABASE_URI = 'аддресс базы данных'

class DeveloperConfig(Config):
    Debug = True

class Testing(Config):
    Debug = True
    Testing = True

