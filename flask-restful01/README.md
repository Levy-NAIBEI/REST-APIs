## Flask-RESTful API
This is a full flask-restful Api that allows a user to create, read, update and delete a product

Features
* Post, retrieve, edit and delete a list of orders of a product

### How the API works
* Run rest_api.py on the commandline/terminal
* Copy the url and use Postman to consume the API

#### Creating a product
* Put `http://127.0.0.1:5000/prod` on Postman address bar
* Select `POST` request in Postman
* Create a product or list of products by `name, describe, price and qty`
* Press send button

#### Retrieve all products
* Put `http://127.0.0.1:5000/prod` in the address bar
* Select `GET` request in Postman
* Press send button

#### Retrieve a product
* Put `http://127.0.0.1:5000/prod/<int:id>`
* Select `GET` request in Postman
* Press send button

#### Edit/update a product
* Put `http://127.0.0.1:5000/prod/<int:id>` on the address bar
* Select `PUT` request in Postman
* Change details of the product
* Press send button

#### Delete a product
* Put `http://127.0.0.1:5000/prod/<int:id>` on the address bar
* Select `DELETE` request in Postman
* Press send button



