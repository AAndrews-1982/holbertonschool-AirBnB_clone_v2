#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """ Display HTML page with States and their cities """
    states = storage.all('State').values()
    states = sorted(states, key=lambda x: x.name)
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
