import math

from flask import render_template, request, redirect
from app import app, login
import Dao
from flask_login import login_user, logout_user
@app.route("/")
def index():
    cates = Dao.load_categoreis()
    kw = request.args.get('kw')
    cate_id = request.args.get('category_id')
    page = request.args.get('page', 1)

    prods = Dao.load_products(kw, category_id= cate_id, page =int(page))
    total = Dao.count_product()
    return render_template("index.html", categories = cates,
                           products = prods, pages= math.ceil(total/app.config["PAGE_SIZE"]))

@app.route("/Login", methods = ['get','post'])
def Login_process():
    if request.method. __eq__('POST'):
        username = request.form.get('username')
        password = request.form.get('password')
        u = Dao.auth_user(username=username, password = password)
        if u:
            login_user(u)
            return redirect('/')
    return render_template('Login.html')

@login.user_loader
def load_user(user_id):
    return Dao.get_user_by_id(user_id)
if __name__ == '__main__':

    app.run(debug= True)