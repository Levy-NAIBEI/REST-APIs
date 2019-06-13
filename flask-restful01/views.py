from flask import request, jsonify
from flask_restful import Resource

orders = []

class Orders(Resource):
	"""docstring for Orders"""
	def get(self):
		return jsonify({
			'Your orders':orders
			})

	def post(self):
		data = request.get_json()

		id = len(orders) +1
		name = data['name']
		describe = data['describe']
		price = data['price']
		qty = data ['qty']

		product = {'id':id,'Name':name, 'Price':price,
		 'Description': describe, 'Quantity': qty 
		 }

		orders.append(product)

		return (jsonify('Your Order', product))
	
	def put(self, id):
		data = request.get_json(id)
		name = data['name']
		describe = data['describe']
		price = data['price']
		qty = data ['qty']

		data.name = name
		data.describe = describe
		data.price = price
		data.qty = qty

		return (jsonify('Product successfully updated': data))
