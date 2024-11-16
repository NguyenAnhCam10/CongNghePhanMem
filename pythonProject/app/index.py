import math

from flask import render_template, request
from app import app
import Dao
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
if __name__ == '__main__':

    app.run(debug= True)