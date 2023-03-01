from app import app
from flask import render_template, url_for, render_template_string


@app.route("/")
@app.route("/index/")
def index():
    profession =
    return render_template('index.html')
