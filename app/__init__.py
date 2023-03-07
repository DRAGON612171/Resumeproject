from flask import Flask
from config import Config

app = Flask(name)
app.config.from_object(Config)

from app import routes