from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from urllib.parse import quote
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb1?charset=utf8mb4" % quote("123456789")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 1

db = SQLAlchemy(app)
