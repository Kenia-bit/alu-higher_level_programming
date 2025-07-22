#!/bin/bash
# Fetches the body of a web page and prints it with GET / => prefix
echo "GET / => \"$(curl -s "$1")\""
