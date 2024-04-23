from flask import Blueprint, render_template

bp = Blueprint("pages", __name__)

@bp.route("/")
def login():
    return render_template("pages/login.html")

@bp.route("/logout")
def logout():
    return login()

@bp.route("/register")
def register():
    return render_template("pages/register.html")

@bp.route("/home")
def home():
    return render_template("pages/home.html")

@bp.route("/qbank")
def qbank():
    return render_template("pages/qbank.html")

@bp.route("/test_paper")
def test_paper():
    return render_template("pages/test_paper.html")

@bp.route("/quiz")
def quiz():
    return render_template("pages/quiz.html")

@bp.route("/about")
def about():
    return render_template("pages/about.html")

@bp.route("/help")
def help():
    return render_template("pages/help.html")