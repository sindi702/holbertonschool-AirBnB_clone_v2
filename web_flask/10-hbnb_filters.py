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


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def storage_close(self):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
