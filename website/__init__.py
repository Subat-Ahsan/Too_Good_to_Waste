from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

from os import path

appData = {'storeSelected' : 1, 'items' : []}



db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'test'
    
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')

    from .models import Item, Store
    if not path.exists('instance/' + 'database.db'):
        print("Database created")
        with app.app_context():
            db.create_all()
    
    return app

