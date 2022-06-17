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

# this is the start of the database
db = SQLAlchemy(app)

# this class is now a model that can be called when needed
class myApp(db.Model):
    # name = database then where on the table plus value type
    order_id = db.Column(db.Integer, primary_key=True)
    # the 500 refers to the size of the string
    size = db.Column(db.String(500))
    crust = db.Column(db.String(500))
    topping = db.Column(db.String(500))

@app.route('/')
def hello_world():
    return "Hello World"

if __name__ == "__main__":
    db.create_all()
    app.run()