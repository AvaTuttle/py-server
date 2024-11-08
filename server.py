from flask import Flask
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

app.run(debug=True)