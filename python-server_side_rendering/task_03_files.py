#!/usr/bin/python3
from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)
JSON_FILE = "products.json"
CSV_FILE = "products.csv"

def read_json():
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

def read_csv():
    products = []
    try:
        with open(CSV_FILE, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                row['id'] = int(row['id'])
                row['price'] = float(row['price'])
                products.append(row)
    except Exception:
        pass
    return products

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id', type=int)
    if source == 'json':
        data = read_json()
    elif source == 'csv':
        data = read_csv()
    else:
        return render_template('product_display.html', error="Wrong source", products=[])

    if product_id is not None:
        data = [p for p in data if p.get('id') == product_id]
        if not data:
            return render_template('product_display.html', error="Product not found", products=[])

    return render_template('product_display.html', products=data, error=None)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
