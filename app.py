from flask import Flask, jsonify, request, redirect, url_for
# This will need to 
# be imported via pip
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
# now the app has to be 
# configured to use SQLAlchemy

# always make sure this is exactly like this,
# and always check this first if errors occur
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///pizza_orders.db'

# this is the start of the database
db = SQLAlchemy(app)
# this is getting no values
ma = Marshmallow(app)

# this class is now a model that can be called when needed
class my_app(db.Model):
    # name = database then where on the table plus value type
    order_id = db.Column(db.Integer, primary_key=True)
    # the 500 refers to the size of the string
    size = db.Column(db.String(500))
    crust = db.Column(db.String(500))
    topping = db.Column(db.String(500))

class MyAppSchema(ma.Schema):
    class Meta:
        fields = ['orderid', 'size', 'crust', 'topping']

my_app_schema = MyAppSchema(many=True)

@app.route('/')
def hello_world():
    return "Hello World"

# now make a route for a get method
@app.route('/orders')
def get_orders():
    entries = my_app.query.all()
    result = my_app_schema.dump(entries)
    return jsonify(result)

# now POST
@app.route('/orders', methods=['POST'])
def make_new_order():
    req = request.get_json()
    order_id = req['order_id']
    size = req['size']
    crust = req['crust']
    topping = req['topping']
    new_entry = my_app(order_id=order_id, size=size, crust=crust, topping=topping)

    db.session.add(new_entry)
    db.session.commit()
    return redirect(url_for('get_orders'))

# Now Delete
@app.route('/orders/<order_id>', methods=["DELETE"])
def delete_order(order_id):
    entry = my_app.query.get_or_404(order_id)
    db.session.delete(entry)
    db.session.commit()
    return redirect(url_for('get_orders'))

# Finally, PUT
@app.route('/orders/<order_id>', methods=["PUT"])
def update_order(order_id):
    entry = my_app.query.get_or_404(order_id)
    req = request.get_json()
    entry.size = req['size']
    entry.crust = req['crust']
    entry.topping = req['topping']
    
    db.session.commit()
    return redirect(url_for('get_orders'))

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, use_reloader=False)