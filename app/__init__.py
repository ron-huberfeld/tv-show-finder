from flask import Flask
from config import Config
from flask_wtf.csrf import CSRFProtect
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = str(os.urandom(32))
csrf = CSRFProtect(app)


from app import routes


if __name__ == '__main__':
    app.run(threaded=True)