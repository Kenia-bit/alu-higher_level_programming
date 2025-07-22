#!/bin/bash
# A script that obtains the content-length of an http request
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f2
