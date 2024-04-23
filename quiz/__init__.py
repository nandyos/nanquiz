from flask import Flask
from quiz import pages

from flask_sqlalchemy import SQLAlchemy
import os

def create_app():
    app = Flask(__name__)

    # Get the base directory
    basedir = os.path.abspath(os.path.dirname(__file__))

    # Set the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'nanquiz.sqlite3')

    # Create the SQLAlchemy database object
    db = SQLAlchemy(app)

    app.register_blueprint(pages.bp)
    return app
