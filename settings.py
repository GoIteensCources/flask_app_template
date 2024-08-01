import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = f'sqlite:///db_{BASE_DIR.split("/")[-1]}.db'

    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_NAME = os.getenv('DB_NAME')

    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg://{DB_USERNAME}:{DB_PASSWORD}@localhost:5432/{DB_NAME}"
    SECRET_KEY = os.getenv("SECRET_KEY", 'your secret key')


