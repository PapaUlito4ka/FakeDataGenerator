from app import db


class Name(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    gender = db.Column(db.Boolean)


class Surname(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(64), unique=True)
    gender = db.Column(db.Boolean)


class Midname(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    midname = db.Column(db.String(64), unique=True)
    gender = db.Column(db.Boolean)


class City(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String(64), unique=True)


class Street(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(64), unique=True)
