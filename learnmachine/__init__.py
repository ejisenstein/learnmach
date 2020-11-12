#from learnmachine import routes
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
            # , template_folder='./templates', static_folder='./static')
app.config['SECRET_KEY'] = 'mGuhs8BCSoTgO4CMcKPv'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from learnmachine import routes
