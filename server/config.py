from os import getenv
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = True

JWT_SECRET_KEY = getenv("JWT_SECRET_KEY", 'local-secret')
JWT_TOKEN_LOCATION = ['cookies']
JWT_ACCESS_TOKEN_EXPIRES = 1800
JWT_COOKIE_SECURE = False
JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=15)
JWT_COOKIE_CSRF_PROTECT = True
JWT_ACCESS_CSRF_HEADER_NAME = "X-CSRF-TOKEN-ACCESS"
JWT_REFRESH_CSRF_HEADER_NAME = "X-CSRF-TOKEN-REFRESH"
