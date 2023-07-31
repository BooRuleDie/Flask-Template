from flask import Blueprint, render_template

base_routes = Blueprint('base_routes', __name__)

@base_routes.route("/")
def Home():
    return render_template("index.html")
