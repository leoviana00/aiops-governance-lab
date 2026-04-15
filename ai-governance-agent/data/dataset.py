import json
import os

DATASET_FILE = "storage/dataset.json"


def load_dataset():

    if not os.path.exists(DATASET_FILE):
        return []

    with open(DATASET_FILE, "r") as f:
        return json.load(f)


def save_dataset(data):

    os.makedirs("storage", exist_ok=True)

    with open(DATASET_FILE, "w") as f:
        json.dump(data, f, indent=2)


def add_event(event):

    dataset = load_dataset()

    dataset.append(event)

    save_dataset(dataset)

    return dataset