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


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def pyt_txt(text='is cool'):
    for_txt = text.replace('_', ' ')
    result = f"Python {for_txt}"
    return result


@app.route('/number/<int:n>', strict_slashes=False)
def num_txt(n):
    return '{} is a number'.format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
