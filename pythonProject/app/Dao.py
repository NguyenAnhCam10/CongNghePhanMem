from itertools import product
from app import app
from app.model import Category, Product


def load_categoreis():
    return Category.query.order_by().all()


def load_products(kw = None, page = 1, category_id=None):

    products = Product.query
    if kw:
        products = products.filter(Product.name.contains(kw))
    if category_id:
        products = products.filter(Product.category_id == category_id)

    page_size = app.config["PAGE_SIZE"]
    start = (page- 1) * page_size
    products = products.slice(start, start + page_size)
    # select * from product limit 8 offset 8
    return products.all()

def count_product():
    return Product.query.count()