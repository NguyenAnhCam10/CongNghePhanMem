from itertools import product
from app import app, db
from app.model import Category, Product, User
import hashlib, cloudinary.uploader

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
def auth_user (username, password, role = None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password))
    if role:
        u = u.filter(User.user_role.__eq__(role))
    return u.first()

# Thêm khi đăng ký
def add_user(name, username, password, avatar):
    password =  str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name = name, username = username, password = password,
             avatar =  "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg")
    if avatar:
        res = cloudinary.uploader.upload(avatar)
        u.avatar = res.get('secure_url')
    db.session.add(u)
    db.session.commit()
def get_user_by_id(id):
    return User.query.get(id)