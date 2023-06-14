from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
import redis

cors = CORS()
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()

app = Flask(__name__)

#use os.get_env() and maintain .env file
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/poridhi_db"
app.config['REDIS_HOST']="localhost"
app.config['REDIS_PORT']=6379
redis_db = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'])

cors.init_app(app)
bcrypt.init_app(app)
db.init_app(app)
migrate.init_app(app, db)

from app.apis import api

