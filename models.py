from datetime import datetime
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username =db.Column(db.String(70), unique = True, nullable =False)
    email= db.Column(db.String(100), unique =True, nullable= False)
    password_hash =db.Column(db.string(100), unique =True, nullable =False)


    def set_password(self,password):
        self.password_hash =generate_password_hash(password)


    def check_password(self, password):
        return check_password_hash(self.password_hash, password)



class Trainer(db.Model):
    id = db.Column(db.String(100), unique =True, nullable =True)
    name =db.Column(db.String(100), unique =True, nullable =True)
    bio =db.Column (db.Text)
    speciality = db.Column =(db.string (120))
    image_url = db.Column(db.String(300))
