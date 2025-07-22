#!/bin/bash
# Sends a GET request to the root URL and prints the response
echo "GET / => \"$(curl -s http://localhost:5000/)\""
