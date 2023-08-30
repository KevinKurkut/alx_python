"""importing flask module"""
from flask import Flask
"""create an instance"""
app = Flask(__name__)
"""route definitiion"""
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
