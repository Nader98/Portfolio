from flask import Blueprint, redirect, render_template, request, url_for

from ne.database import get_db

bp = Blueprint("messages", __name__)

@bp.route("/contact-me", methods=("GET", "POST"))
def contact():
    if request.method == "POST":
        author = request.form["author"]
        message = request.form["message"]

        if message:
            f=author
            db = get_db()
            db.execute(
                "INSERT INTO message ('creator', 'text') VALUES (?, ?)",
                (author, message),
            )
            db.commit()
            return redirect(url_for("messages.message", f=author))

    return render_template("contact-me.html")

@bp.route("/messages/<f>")
def message(f):
    # db = get_db()
    # messages = db.execute(
    #     "SELECT creator, text, created FROM message ORDER BY created DESC"
    # ).fetchall()
    return render_template("messages.html", user=f)
