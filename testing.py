from flask import flask
app = Flask(--name__)

@app.route("/")
def index():
    return "<h1>Hello Azure!</h1>"