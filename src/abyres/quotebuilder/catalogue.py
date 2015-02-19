from abyres.quotebuilder.app import App, template_globals, Root

class Catalogue(object):
    pass

class ProductCollection(object):
    pass

class Product(object):
    def __init__(self, id, name, data):
        self.id = id
        self.name = name
        self.data = data

def manage(self, request):
    return {}

PRODUCTS=[{
        'id': 1,
        'name': 'hello',
        'data': 'world'
    }, {
        'id': 2,
        'name': 'world',
        'data': 'hello'
    }]

@App.path(model=ProductCollection, path='products/')
def get_collection():
    return ProductCollection()

@App.path(model=Product, path='products/{pid}')
def get_product(pid):
    return Product(**PRODUCTS[int(pid)])

@App.json(model=ProductCollection)
def index(self, request):
    return PRODUCTS

@App.json(model=Product, name='')
def prodindex(self, request):
    return {
        'id': self.id,
        'name': self.name,
        'data': self.data
    }
