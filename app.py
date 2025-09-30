from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/fitconnect'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config["JWT_SECRET_ KEY"] = 'supersecrekey'


db =SQLAlchemy(app)
migrate =Migrate(app,db)
jwt =JWTManager(app)


