from flask import Flask
# This will need to 
# be imported via pip
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# now the app has to be 
# configured to use SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myapp.sqlite'

# this is the start of the database
db = SQLAlchemy(app)
ma = Marshmallow(app)

# this class is now a model that can be called when needed
class myApp(db.Model):
    # name = database then where on the table plus value type
    order_id = db.Column(db.Integer, primary_key=True)
    # the 500 refers to the size of the string
    size = db.Column(db.String(500))
    crust = db.Column(db.String(500))
    topping = db.Column(db.String(500))

class MyAppSchema(ma.Schema):
    class Meta:
        fields = ('orderid', 'size', 'crust', 'topping')

@app.route('/')
def hello_world():
    return "Hello World"

# now make a route for a get method
@app.route('/orders')
def get_orders():
    return 

if __name__ == "__main__":
    db.create_all()
    app.run()