from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from core import db

app = Flask(__name__)


#app.config.from_object(os.environ['APP_SETTINGS'])
app.config.from_object('config')
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///DB_File.db'
#db.init_app(app)
db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)

from app import views

