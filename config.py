import os
from sqlalchemy import create_engine
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'isilop_secret_key'
    DATABASE_URL = 'localhost:5432'
    DATABASE_USER = 'postgres'
    DATABASE_PWD = 'alhamdulillah'
    DATABASE_NAME = 'isilop_db'
    # uri = 'postgresql+psycopg2://{user}:{pwd}@{url}/{db_name}'.format(user=DATABASE_USER, pwd=DATABASE_PWD, url=DATABASE_URL, db_name=DATABASE_NAME)
    # print( create_engine(uri).values)
    # print(uri) 
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pwd}@{url}/{db_name}'.format(user=DATABASE_USER, pwd=DATABASE_PWD, url=DATABASE_URL, db_name=DATABASE_NAME)

class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True