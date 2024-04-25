from flask import Flask
from app.models import db


app= Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecomm-db.db' 
db.init_app(app)


from app import routes, models