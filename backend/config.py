import os
from pathlib import Path

basedir = Path(__file__).parent

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(Path(basedir, 'app.db'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = "redis://localhost:6379/0"
    DEBUG = True

