from flask import request, jsonify
from flask_restful import Resource

orders = []

class Orders(Resource):
	''' Retrieving and creating products'''
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
	
	
class SingleOrder(Resource):
	''' Retrieving, updating and deleting a product by id'''
	def get(self, id):
		for prod in orders:
			if prod['id'] == id:
				return (jsonify({
                    "Message": "Ok",
                    "Product": prod
                }))

			return (jsonify({"Message": "Not found"}))

	def put(self, id):
		for prod in orders:
			data = request.get_json()
			if prod['id'] == id:
				prod['name'] = data['name']
				prod['describe'] = data['describe']
				prod['price'] = data['price']
				prod['qty'] = data ['qty']
				return (jsonify({"Product": prod}))

			updated_product = {
				"id":id,
				'Name':data['name'],
				'Describe':data['describe'],
				'Price':data['price'],
				'Quantity':data['qty']
			}

			orders.append(updated_product)

			return (jsonify({'Product successfully updated': updated_product}))
    
	def delete(self, id):
		global orders
		orders = [prod for prod in orders if prod['id'] != id]
		return (jsonify({
			"Message": "Product with id {} is deleted".format(id)
			}))
   		
