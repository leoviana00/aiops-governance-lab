from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix,
    classification_report
)

from database.repository import load_dataset
from utils.feature_builder import build_features
from services.predictor import load_model


def evaluate_model():

    dataset = load_dataset()

    if len(dataset) < 10:
        return {
            "status": "not enough data"
        }

    X, y = build_features(dataset)

    model = load_model()

    if not model:
        return {
            "status": "model not trained"
        }

    # -----------------------------
    # Predição
    # -----------------------------
    y_pred = model.predict(X)

    # -----------------------------
    # Métricas
    # -----------------------------
    accuracy = accuracy_score(y, y_pred)
    precision = precision_score(y, y_pred, zero_division=0)
    recall = recall_score(y, y_pred, zero_division=0)

    cm = confusion_matrix(y, y_pred).tolist()

    report = classification_report(y, y_pred, output_dict=True)

    return {
        "accuracy": round(accuracy, 4),
        "precision": round(precision, 4),
        "recall": round(recall, 4),
        "confusion_matrix": cm,
        "classification_report": report
    }