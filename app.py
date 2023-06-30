from flask import Flask, render_template

app = Flask(__name__)
# app.config(debug = True)

from controller import *

@app.route("/")
@app.route("/home")
def home():
    return "This is Home Page."

if __name__ == "__main__":
    app.run(debug=True)