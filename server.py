from flask import Flask, request, jsonify
import json
from config import db

app = Flask(__name__)

# Helper function to convert ObjectId to string
def fix_id(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# Root endpoint with a welcome message
@app.get("/")
def home():
    return "Welcome to the Product Catalog API"

# Test endpoint
@app.get("/test")
def test():
    return "you hackin' buster?"

# About endpoint returning JSON
@app.get("/api/about")
def aboutGet():
    me = {"name": "Ava"}
    return json.dumps(me)

# Greet endpoint with name in URL
@app.get("/greet/<name>")
def greet(name):
    return f"<h1 style=color:blue>Hello, {name}!</h1>"

# Firewall message endpoint
@app.get("/firewall")
def firewall_message():
    return "<h1 style=color:red>Access Denied</h1><p>Your IP has been restricted by the firewall. Please contact the administrator if you believe this is an error.</p>", 403

# Retrieve all products from the catalog
@app.get("/api/catalog")
def get_catalog():
    products = []
    cursor = db.products.find({})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

# Save a new product to the catalog
@app.post("/api/catalog")
def save_product():
    item = request.get_json()
    db.products.insert_one(item)
    return json.dumps(fix_id(item))

# Calculate total value of catalog
@app.get("/api/reports/total")
def total_value():
    cursor = db.products.find({})
    total = sum(prod["price"] * prod["quantity"] for prod in cursor if "price" in prod and "quantity" in prod)
    return jsonify({"total_value": total})

# Retrieve products by category
@app.get("/api/products/<category>")
def get_products_by_category(category):
    products = []
    cursor = db.products.find({"category": category})
    for prod in cursor:
        products.append(fix_id(prod))
    return json.dumps(products)

# Update a product by index (index-based update for in-memory data)
@app.put("/api/products/<int:index>")
def update_product(index):
    updated_item = request.get_json()
    products = list(db.products.find({}))
    if 0 <= index < len(products):
        db.products.update_one({"_id": products[index]["_id"]}, {"$set": updated_item})
        return json.dumps(fix_id(updated_item))
    else:
        return "Index out of range", 404

# Delete a product by index
@app.delete("/api/products/<int:index>")
def delete_product(index):
    products = list(db.products.find({}))
    if 0 <= index < len(products):
        deleted_item = db.products.find_one_and_delete({"_id": products[index]["_id"]})
        return json.dumps(fix_id(deleted_item))
    else:
        return "Index out of range", 404

# Update specific fields of a product by index
@app.patch("/api/products/<int:index>")
def update_item_fields(index):
    products = list(db.products.find({}))
    if 0 <= index < len(products):
        updated_fields = request.get_json()
        db.products.update_one({"_id": products[index]["_id"]}, {"$set": updated_fields})
        return json.dumps(fix_id(updated_fields))
    else:
        return "Index out of range", 404

if __name__ == "__main__":
    app.run(debug=True)
