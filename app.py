from flask import Flask
from Application import *

app = Flask(__name__)

@app.route("/")
def index():
    print("root route")
    # application()
    return "OK"