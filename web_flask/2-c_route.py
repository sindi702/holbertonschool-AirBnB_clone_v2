#!/usr/bin/python3
''' flask setup'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def str_txt(text):
    formatted_text = text.replace('_', ' ')
    result = f"C {formatted_text}"
    return result


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
