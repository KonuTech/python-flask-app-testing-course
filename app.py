from flask import Flask, jsonify
from markupsafe import Markup


app = Flask(__name__)


@app.route('/')
def home():
    return jsonify({'message': 'Hello, world!'})


if __name__ == '__main__':
    app.run()
