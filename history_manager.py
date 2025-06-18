import json
import os

file_path = "outputs/excuse_history.json"

def save_excuse(excuse):
    if not os.path.exists("outputs"):
        os.mkdir("outputs")
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([], f)

    with open(file_path, "r") as f:
        history = json.load(f)

    history.append(excuse)

    with open(file_path, "w") as f:
        json.dump(history, f)

def get_history():
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return []
