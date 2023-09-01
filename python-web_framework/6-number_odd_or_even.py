"""importing flask module"""
from flask import Flask, render_template
"""create an instance"""
app = Flask(__name__)
"""route definitiion"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"
"""/hbnb: display “HBNB”"""
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"

"""C is fun!"""
@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    return "C " + text.replace("_", " ")

"""Python is cool!"""
@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    return "Python " + text.replace("_", " ")

"""Is it a number?"""
@app.route('/number/<int:n>', strict_slashes=False)
def show_n(n):
    #display “n is a number”
    return ("{} is a number".format(n))

"""Number template"""
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return (render_template("5-number.html", number=n))

"""Odd or even?"""
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_even(n):
    return (render_template("6-number_odd_or_even.html", number=n))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
