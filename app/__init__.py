from flask import Flask
import os

SECRET_KEY = os.urandom(32)

app = Flask(__name__, static_folder="static")
app.config['SECRET_KEY'] = SECRET_KEY

from app import routes