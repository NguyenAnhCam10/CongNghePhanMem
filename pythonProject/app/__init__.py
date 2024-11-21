from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from urllib.parse import quote
import cloudinary
app.secret_key = 'njsdfisdbjsnjnjfnsfnkfeuhefuehfygrfues'
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saledb1?charset=utf8mb4" % quote("123456789")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"] = 2

db = SQLAlchemy(app)
login = LoginManager(app)
# Configuration
cloudinary.config(
    cloud_name = "dq7npllb4",
    api_key = "419655961425595",
    api_secret = "ObQxziuvjUZDCZOmu35ucpsL39U", # Click 'View API Keys' above to copy your API secret
    secure=True
)
