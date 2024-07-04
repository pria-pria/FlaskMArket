from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']= 'sqlite:///views.db'
db= SQLAlchemy(app)

class Item(db.Model):
    name=db.Column(db.String(length=30), nullable=False, unique=True)
    price=db.Column(db.Integer, nullable=False, default=0)
    id=db.Column(db.Integer, primary_key=True)
    barcode= db.Column(db.String(length=12), nullable=False, unique= True )


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/market')
def Market():
    items=[
        {'id':1,'name':'Phone','price':500, 'barcode': 'i374783287834'},
        {'id':2,'name':'Laptop','price':1000, 'barcode': 'i374g786476287834'},
        {'id':3,'name':'Tablet','price':200, 'barcode': 'i3747hwhw287834'},
        {'id':4,'name':'Watch','price':300, 'barcode': 'k324683287834'},
        {'id':5,'name':'Headphones','price':400, 'barcode': 'b7632473287834'},

    ]
    return render_template('market.html', items=items)