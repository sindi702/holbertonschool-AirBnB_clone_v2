#!/usr/bin/python3
''' flask setup'''
from flask import Flask
from flask import render_template
from models import storage
from models.state import State
from models.city import City
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_ls():
    cities_by_state = {}
    states = storage.all("State").values()
    for state in states:
        cities_by_state[state.name] = state.cities
    return render_template('8-cities_by_states.html', states=states,
                           cities=cities_by_state)


@app.teardown_appcontext
def storage_close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
