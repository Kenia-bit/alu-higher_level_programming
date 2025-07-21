#!/usr/bin/python3
"""This script adds arguments to a Python list and saves them to a file."""
import json
from sys import argv
from os.path import exists

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

# Step 1: Load existing list, or use an empty list
if exists(filename):
    items = load_from_json_file(filename)
else:
    items = []

# Step 2: Extend the list with new arguments
items.extend(argv[1:])

# Step 3: Save updated list to file
save_to_json_file(items, filename)
