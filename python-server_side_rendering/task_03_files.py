#!/usr/bin/python3
"""Flask application that reads product data from JSON or CSV files and
displays it, with optional filtering by id and error handling for
invalid sources or missing ids."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json_products():
    """Read and return the list of products from products.json."""
    with open('products.json') as f:
        return json.load(f)


def read_csv_products():
    """Read and return the list of products from products.csv."""
    products = []
    with open('products.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                'id': int(row['id']),
                'name': row['name'],
                'category': row['category'],
                'price': float(row['price']),
            })
    return products


@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html')


@app.route('/products')
def products():
    """Render the product display page, reading data from JSON or CSV
    depending on the 'source' query parameter, optionally filtered by
    the 'id' query parameter."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_products()
    elif source == 'csv':
        data = read_csv_products()
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found")

        data = [p for p in data if p['id'] == product_id]

        if not data:
            return render_template(
                'product_display.html', error="Product not found")

    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)