from flask import Flask
# This will need to 
# be imported via pip
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# now the app has to be 
# configured to use SQLAlchemy

app.config['SQL_ALCHEMY_DATABASE_URL'] = 'sqlite:///myapp.sqlite'
# this silecnces the tracking notifications 
app.config['SQL_ALCHEMY_TRACK_MODIFICATION'] = false

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    app.run()