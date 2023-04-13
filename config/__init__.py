from pathlib import Path
from dotenv import dotenv_values


BASE_DIR = Path(__file__).parents[1]

env = dotenv_values(f"{BASE_DIR}/.env")


class Config(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://" \
                              f"{env['POSTGRES_USER']}:{env['POSTGRES_PASSWORD']}@" \
                              f"{env['POSTGRES_HOST']}:{env['POSTGRES_PORT']}/{env['POSTGRES_NAME']}"


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True


class ProdactionConfig(Config):
    ...
