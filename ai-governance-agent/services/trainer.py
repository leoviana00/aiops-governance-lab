import pickle
import os
from sklearn.ensemble import RandomForestClassifier

from database.repository import load_dataset
from utils.feature_builder import build_features

MODEL_FILE = "storage/model.pkl"


def train_model():

    dataset = load_dataset()

    if len(dataset) < 5:
        return None

    X, y = build_features(dataset)

    model = RandomForestClassifier()

    model.fit(X, y)

    os.makedirs("storage", exist_ok=True)

    with open(MODEL_FILE, "wb") as f:
        pickle.dump(model, f)

    return model