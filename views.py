from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

task_list=[]

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/cakes")
def cakes():
    return render_template("cakes.html")

@views.route("/contact")
def contact():
    return render_template("contact.html")

@views.route("/ice_cream")
def ice_cream():
    return render_template("ice_cream.html")

@views.route("/gallery")
def gallery():
    return render_template("gallery.html")
