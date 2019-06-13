
"""CRUD API using flask, sqlalchemy, marshmallow --
 using postman api to test api endpoints"""

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#database
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

#init db
db = SQLAlchemy(app)
#init ma
ma = Marshmallow(app)

#product class/model
class Product(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(60), unique = True, nullable = False)
	description = db.Column(db.String(150))
	price = db.Column(db.Float)
	qty = db.Column(db.Integer)

	def __init__(self, name, description, price, qty):
		self.name = name
		self.description = description
		self.price = price
		self.qty = qty

#product schema
class ProductSchema(ma.Schema):
	#what to expose/display
	class Meta:
		fields = ('id','name','description','price','qty')

#init Schema
product_schema = ProductSchema(strict = True)
products_schema = ProductSchema(many = True, strict = True)

# To interact with db, create endpoints
#create product
@app.route('/product', methods = ['POST'])
def add_product():
	name = request.json['name']
	description = request.json['description']
	price = request.json['price']
	qty = request.json['qty']

    #instantiating an object
	new_product = Product(name, description, price, qty)
	
	db.session.add(new_product)
	db.session.commit()

	return product_schema.jsonify(new_product)

# Get all products
@app.route('/product', methods = ['GET'])
def get_products():
	all_products = Product.query.all()
	results = products_schema.dump(all_products)
	return jsonify(results.data)

# Get one product
@app.route('/product/<id>', methods = ['GET'])
def get_product(id):
	product = Product.query.get(id)
	return product_schema.jsonify(product)

#update product
@app.route('/product/<id>', methods = ['PUT'])
def update_product(id):
	product = Product.query.get(id)

	name = request.json['name']
	description = request.json['description']
	price = request.json['price']
	qty = request.json['qty']

	#assignment of updated attributes
	product.name = name
	product.description = description
	product.price = price
	product.qty = qty

	db.session.commit()
	return product_schema.jsonify(product)

# Delete one product
@app.route('/product/<id>', methods = ['DELETE'])
def delete_product(id):
	product = Product.query.get(id)
	db.session.delete(product)
	db.session.commit()

	return product_schema.jsonify(product)		

if __name__ == '__main__':
        app.run(debug = True)	
