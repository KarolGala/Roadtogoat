from flask import Blueprint, render_template, request
from flask import current_app


views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template("index.html")
