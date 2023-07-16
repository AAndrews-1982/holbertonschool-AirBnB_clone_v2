#!/usr/bin/python3
""" A simple flask web application that runs at 0.0.0.0:5000 """

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' at '/' """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' at '/hbnb' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_is_fun(text):
    """ Displays 'C ' followed by the value of <text> in the route """
    return f"C {text.replace('_', ' ')}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text='is cool'):
    """ Displays 'Python ' followed by the value of <text> in the route
    The default value of text is 'is cool'
    """
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def is_an_integer(n):
    """ Uses flask variable rules to only display n if n is an int """
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """ Uses flask variable rules to return a jinja2 formatted html page
    Only returns if n is an int
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ Uses flask variable rules to return a jinja2 formatted html page
    that says if n is odd or even
    Only returns if n is an int
    """
    if n % 2 == 0:
        out = f"{n} is odd"
    else:
        out = f"{n} is even"
    return render_template('6-number_odd_or_even.html', out=out)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
