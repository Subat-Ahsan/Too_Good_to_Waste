from flask import Blueprint, render_template, jsonify, request 
from datetime import datetime
import json

from .models import Item, Store
from . import db, appData
views = Blueprint("views",__name__)

@views.route("/")
def home():
    return render_template("base.html")

@views.route("input-data", methods=['GET', 'POST'])
def input_data():
    if request.method == 'POST':
        name = request.form.get('name')
        quantity = int(request.form.get('quantity'))
        date_made = request.form.get('date_made')
        date_expire = request.form.get('date_expire')
        item = Item(store_id = appData["storeSelected"], name = name, quantity = quantity, date_made= datetime.strptime(date_made,'%Y-%m-%dT%H:%M'), date_expire=datetime.strptime(date_expire,'%Y-%m-%dT%H:%M'))
        db.session.add(item)
        db.session.commit()

    return render_template("data_input.html")

@views.route("store-input", methods=['GET', 'POST'])
def store_input():
    if request.method == 'POST':
        name = request.form.get('name')
        address = request.form.get('address')
        new_store = Store(name= name, address = address, type='S')
        db.session.add(new_store)
        db.session.commit()
    return render_template("store_input.html")

@views.route("store-view", methods=['GET'])
def store_view():
    all_stores = db.session.query(Store).filter_by(type="S").all()
    
    return render_template("store_view.html", stores=all_stores)

@views.route("store-info/<storeId>", methods=['GET'])
def store_info(storeId):
    store = db.session.query(Store).filter_by(id=storeId).first()
    return render_template("store_info.html", store = store)

@views.route("select-store", methods = ['POST'])
def select_store():
    store = json.loads(request.data)
    appData["storeSelected"] = store["storeID"]
    return jsonify({})