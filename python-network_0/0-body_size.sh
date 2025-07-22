#!/usr/bin/python3
"""Starts a basic web server with a single route"""
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "my index page is so cool! Mainly because it’s in Python"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
