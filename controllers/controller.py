from flask import render_template
from models.order_list import orders
from app import app


@app.route('/orders')
def index():
    return render_template('index.html', title='Order', orders=orders)

@app.route("/<index>", methods=['GET'])
def order_page(index):
    return render_template('order.html', title='Order', orders=orders, index=0)
