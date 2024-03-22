import json
import os

file_path = 'interviewees.json'

def load_interviewees():
    """
    Function to load interviewee data from JSON file.
    """
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            interviewees = json.load(file)
        return interviewees
    else:
        return []

def save_interviewees(interviewees):
    """
    Function to save interviewee data to JSON file.
    """
    with open(file_path, 'w') as file:
        json.dump(interviewees, file, indent=4)
