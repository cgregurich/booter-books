from flask import render_template
from booter_books import app

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/login")
def login():
    return render_template("login.html")
