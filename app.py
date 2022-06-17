from flask import Flask
# This will need to 
# be imported via pip
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run()