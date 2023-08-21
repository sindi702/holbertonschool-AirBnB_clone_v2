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


@app.route('/states', strict_slashes=False)
def state_ls():
    states = storage.all("State").values()
    return render_template('9-states.html', states=states, mode='all')


@app.route('/states/<id>', strict_slashes=False)
def state_id(id):
    states = storage.all("State").values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, mode='id')
    return render_template('9-states.html', states=state, mode=';')


@app.teardown_appcontext
def storage_close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
