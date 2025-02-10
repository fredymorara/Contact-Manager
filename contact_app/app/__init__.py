from flask import Flask
from flask_login import LoginManager
from flask_mail import Mail
from pymongo import MongoClient
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Initialize MongoDB
client = MongoClient(app.config['MONGO_URI'])
db = client.contacts_db

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Initialize Flask-Mail
mail = Mail(app)

from app import routes, models