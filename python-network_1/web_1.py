#!/usr/bin/python3
from flask import Flask
app = Flask(__name__)

@app.route('/status')
def status():
    return "Custom status"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
