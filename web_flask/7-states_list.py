#!/usr/bin/python3
""" A simple flask web application that runs at 0.0.0.0:5000 """

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all(State)
    s_list = {value.id: value.name for value in states.values()}
    return render_template('7-states_list.html',
                           Table="States",
                           items=s_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
