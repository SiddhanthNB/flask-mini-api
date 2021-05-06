from flask import Flask, redirect, url_for, render_template, request
from datetime import date

app = Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("dob"))

@app.route("/dob", methods=["POST", "GET"])
def dob():
    if request.method == "POST":
        y,m,d= map(int, request.form["nm"].split("/"))
        delta = abs(date(y,m,d) - date.today())
        day=str(delta.days)
        return redirect( url_for("days", usr_days=day) )
    else:
        return render_template("interface.html")

@app.route("/<usr_days>")
def days(usr_days):
    return f"<h1>{usr_days} Days </h1>"

if __name__ == "__main__":
    app.run(debug=True)