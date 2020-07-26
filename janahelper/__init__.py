from googletrans import Translator
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import PG_URI
translator = Translator()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = PG_URI
db = SQLAlchemy(app)
CORS(app)
