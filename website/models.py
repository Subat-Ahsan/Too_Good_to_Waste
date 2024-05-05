from . import db
from flask_login import UserMixin

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(100))
    date_made = db.Column(db.DateTime)
    date_expire = db.Column(db.DateTime)
    store_id = db.Column(db.Integer, db.ForeignKey('store.id'))

class Store (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    address = db.Column(db.String(100))
    items = db.relationship('Item')
    type = db.Column(db.String(1))

