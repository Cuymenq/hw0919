from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(200)) 
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    body = db.Column(db.String(1200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    make = db.Column(db.String(150))
    model = db.Column(db.String(50))
    year = db.Column(db.String(50))
    price = db.Column(db.String)
    date_created = db.Column(db.String(50))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  

# id
# make
# model
# year
# color
# price
# date_created
# user_id (the user that posted the car for sale)