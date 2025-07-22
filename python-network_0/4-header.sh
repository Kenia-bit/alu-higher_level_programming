#!/bin/bash
# A script that sends a GET request with a custom header
curl -s "$1" -H "X-School-User-Id: 98"
