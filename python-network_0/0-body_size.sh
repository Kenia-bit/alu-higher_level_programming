#!/bin/bash
# Starts Flask server in background, waits, and fetches index page
python3 web_0.py & sleep 1 && echo "GET / => \"$(curl -s http://127.0.0.1:5000/)\""
