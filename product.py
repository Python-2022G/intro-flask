from flask import Flask, request, jsonify
from db import DB


app = Flask(__name__)
db = DB()

# GET /products/ -> get all products or by name
@app.route('/products/')
def get_all_products():
    params = request.args
    name = params.get('name')
    if name:
        return jsonify(db.get_product_by_name(name))

    return jsonify(db.get_all_products())


# GET /products/<id> -> get a product by id
@app.route('/products/<int:id>')
def get_product(id):
    return jsonify(db.get_product(id))


# POST /products/ -> add a product
@app.route('/products/', methods=['POST'])
def add_product():
    data = request.get_json()
    db.add_product(data['name'], data['price'])
    return jsonify({'message': 'Product added successfully'})


# PUT /products/<id> -> update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.get_json()
    db.update_product(id, data['name'], data['price'])
    return jsonify({'message': 'Product updated successfully'})


# DELETE /products/<id> -> delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    db.delete_product(id)
    return jsonify({'message': 'Product deleted successfully'})



if __name__ == '__main__':
    app.run(debug=True)