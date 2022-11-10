from flask import Flask, url_for, render_template
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/profile")
def profile():
     return render_template('profile.html')

@app.route("/signup")
def signup():
     return render_template('signup.html')




    