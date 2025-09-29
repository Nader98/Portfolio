from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def home():
    return render_template("home.html")

@bp.route("/skills")
def about():
    return render_template("skills.html")

