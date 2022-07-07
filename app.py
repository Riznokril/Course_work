from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy


#Connection to DB URI
dbhost = "localhost:3306"
dbuser = "root"
dbpass = "234432or"
dbname = "course_work_db"

#Flask DB configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{dbuser}:{dbpass}@{dbhost}/{dbname}"
app.config['SQLALCHEMY_TRACK_MODIFICATIOS'] = False

db = SQLAlchemy(app)

#ORM
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(45))
    password = db.Column(db.String(45))

class User_enter_and_exit(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    enter = db.Column(db.String(1))
    exit = db.Column(db.String(1))
    time = db.Column(db.DateTime)
    user_id = (db.Column(db.Integer))

