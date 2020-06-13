from flask import Flask, request, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# init the app
app = Flask(__name__)


# init the app config
app.config.from_object(os.environ['APP_SETTINGS'])
# print(app.config.from_object(os.environ))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# from app.module import *
from .models import Users

from app.module.controller import userscontroller
from app.module.controller import authcontroller
# print("runing")