from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate



app= Flask(__name__)
app.config['SECRET_KEY']= 'doughnuts'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tony@localhost/ecomm'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
print("connected to db, perhaps")

db = SQLAlchemy(app)
from app.models import User
migrate= Migrate(app, db)


from app import routes, models
