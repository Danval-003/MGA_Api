from flask import Flask
from flask_caching import Cache
import os

app = Flask(__name__)

template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../templates')
app = Flask(__name__, template_folder=template_folder)

cache = Cache(app, config={'CACHE_TYPE': 'simple'})


