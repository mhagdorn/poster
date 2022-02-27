from flask import Flask
from flask_wtf.csrf import CSRFProtect

from .config import Config


csrf = CSRFProtect()

app = Flask(__name__)
app.config.from_object(Config)

csrf.init_app(app)
