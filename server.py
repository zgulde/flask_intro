from flask import Flask, render_template, request
from time import strftime

app = Flask(__name__)


@app.route("/")
def home():
    languages = [
        ("Python", "https://www.python.org/"),
        ("Bash", "https://en.wikipedia.org/wiki/Bash_%28Unix_shell%29"),
        ("ClojureScript", "https://clojurescript.org/"),
        ("R", "https://www.r-project.org/"),
    ]
    return render_template(
        "index.html", the_date=strftime("%B %d, %Y"), languages=languages
    )

@app.route("/greeting")
def show_greeting_form():
    return render_template("greeting.html")

@app.route("/greeting-result", methods=["POST"])
def show_greeting_result():
    users_first_name = request.form["first_name"]
    return render_template(
        "greeting-result.html",
        name=users_first_name
    )


@app.route("/which-side-of-the-force")
def force():
    return "The dark side"


from random import randint


@app.route("/roll-dice/<int:ndice>")
def rolldice(ndice):
    rolls = [randint(1, 6) for _ in range(ndice)]
    output = "<h1>Here are your dice rolls:</h1>"
    output += "<br>"
    for roll in rolls:
        output += str(roll) + "<br>"
    print(output)
    return output


@app.route("/i-can-html")
def htmlpage():
    rolls = [randint(1, 6) for _ in range(10)]
    return render_template("my-html-page.html", rolls=rolls)


@app.route("/hello/<name>")
def hello(name):
    print("Will we see this?")
    return "Hello, " + name + "!"
