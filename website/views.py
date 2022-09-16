from flask import Blueprint, render_template, request
from flask import current_app


views = Blueprint('views', __name__)


@views.route("/")
def index():
    return render_template("index.html") 

@views.route("/Kalistenika")
def kalistenika():
    return render_template("Kategorie/Kalistenika.html") 


@views.route("/Trójbój")
def trojboj():
    return render_template("Kategorie/Trojboj.html") 

@views.route("/Hybryda")
def Hybrda():
    return render_template("Kategorie/Hybryda.html") 

