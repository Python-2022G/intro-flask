from tinydb import TinyDB, Query

db = TinyDB('db.json', indent=4)

class DB:
    def __init__(self):
        self.product = db.table('product')

    def get_all_products(self):
        return self.product.all()
    
    def get_product_by_name(self, name):
        return self.product.get(Query().name == name)
    
    def get_product(self, id):
        return self.product.get(doc_id=id)
    
    def add_product(self, name, price):
        self.product.insert({'name': name, 'price': price})
    
    def update_product(self, id, name, price):
        self.product.update(
            {'name': name, 'price': price}, 
            doc_ids=[id]
        )

    def delete_product(self, id):
        self.product.remove(doc_ids=[id])
    