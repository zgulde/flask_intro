from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "This is the home page!"


@app.route("/which-side-of-the-force")
def force():
    return "The dark side"

from random import randint

@app.route('/roll-dice/<int:ndice>')
def rolldice(ndice):
    rolls = [randint(1, 6) for _ in range(ndice)]
    output = '<h1>Here are your dice rolls:</h1>'
    output += '<br>'
    for roll in rolls:
        output += str(roll) + '<br>'
    print(output)
    return output

@app.route('/i-can-html')
def htmlpage():
    rolls = [randint(1, 6) for _ in range(10)]
    return render_template(
        'my-html-page.html',
        rolls=rolls
    )


@app.route("/hello/<name>")
def hello(name):
    print('Will we see this?')
    return "Hello, " + name + "!"
