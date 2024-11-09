from flask import Flask, request
import json 

app = Flask(__name__)

@app.get("/")
def home():
    return "hello from flask"

#endpoints
@app.get("/test")
def test():
    return "you hackin' buster?"

# endpoint using json
@app.get("/api/about")
def aboutGet():
    me = {"name": "Ava"}
    return json.dumps(me)

#example
# @app.post("/")
# def homePost():
# return "hello from flask post"

#create a anew route /greet/{name}, this route should accept name as part of the urland areturn an html message saying "hello {name}"

@app.get("/greet/<name>")
def greet(name):
    return f"<h1 style=color:blue>Hello, {name}!</h1>"

#create a firewall message
@app.get("/firewall")
def firewall_message():
    return "<h1 style=color:red>Access Denied</h1><p>Your IP has been restricted by the firewall. Please contact the administrator if you believe this is an error.</p>", 403

# #############
products = []
@app.get("/api/products")
def get_products():
    return json.dumps(products)

@app.post("/api/products")
def save_products():
    item = request.get_json()
    print(item)
    products.append(item)
    return json.dumps(item)

@app.put("/api/products/<int:index>")
def update_products(index):
    updated_item=request.get_json()
    if 0<= index <=len(products):
        products[index] = updated_item
        return json.dumps(updated_item)
    else:
        return "that index does not exist"
    

@app.delete("/api/products/<int:index>")
def delete_products(index):
    if 0<= index <=len(products):
        delete_item = products.pop(index)
        return json.dumps(delete_item)
    else:
        return "that index does not exist"
    
# patch -- the method to update a specific element into python is: .update

@app.patch("/api/products/<int:index>")
def update_item(index):
    if 0 <= index <= len(products):
        updated_field = request.get_json()
        products(index).update(updated_field)
        return json.dumps(updated_field)
    else:
        return "That index does not exist"


app.run(debug=True)
