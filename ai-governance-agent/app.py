import random
import uuid
from datetime import datetime, timedelta

from database.connection import get_connection

from fastapi import FastAPI

from database.connection import get_connection

from services.evaluator import evaluate_model
from models.schemas import ChangeEvent, IncidentFeedback
from database.repository import (
    add_event,
    load_dataset,
    init_db,
    update_incident
)

from services.trainer import train_model
from services.predictor import predict_risk

app = FastAPI()


# ==========================================
# Inicialização do banco
# ==========================================

@app.on_event("startup")
def startup():

    init_db()


# ==========================================
# Root
# ==========================================

@app.get("/")
def root():

    return {
        "service": "AIOps Governance Agent",
        "version": "1.2"
    }


# ==========================================
# Health
# ==========================================

@app.get("/health")
def health():

    return {"status": "ok"}


# ==========================================
# Dataset Stats
# ==========================================

@app.get("/dataset/stats")
def dataset_stats():

    data = load_dataset()

    incidents = sum(1 for d in data if d["incident"] == 1)

    return {
        "events": len(data),
        "incidents": incidents,
        "healthy": len(data) - incidents
    }


# ==========================================
# Change Event
# ==========================================

@app.post("/change-event")
def change_event(event: ChangeEvent):

    event_dict = event.dict()

    # log para diagnóstico
    print("EVENT RECEIVED:", event_dict)

    prediction = predict_risk(event_dict)

    add_event(
        event_dict,
        prediction
    )

    return {
        "status": "stored",
        "prediction": prediction
    }

# ==========================================
# Predict Risk
# ==========================================

@app.post("/predict")
def predict(event: ChangeEvent):

    result = predict_risk(event.dict())

    if result["risk_probability"] is None:

        return {
            "risk_probability": None,
            "message": "model not trained"
        }

    return result


# ==========================================
# Incident Feedback
# ==========================================

@app.post("/incident-feedback")
def incident_feedback(data: IncidentFeedback):

    update_incident(
        data.commit_sha,
        data.incident,
        data.deploy_timestamp
    )

    model = train_model()

    return {
        "status": "incident updated",
        "model_trained": model is not None
    }


# ==========================================
# Manual Training
# ==========================================

@app.post("/train")
def train():

    model = train_model()

    if model is None:

        return {"status": "not enough data"}

    return {"status": "model trained"}


# ==========================================
# Risk Explanation
# ==========================================

@app.post("/risk-explain")
def risk_explain(event: ChangeEvent):

    result = predict_risk(event.dict())

    probability = result["risk_probability"]

    if probability is None:

        return {
            "message": "model not trained"
        }

    level = "LOW"

    if probability >= 0.7:
        level = "HIGH"

    elif probability >= 0.4:
        level = "MEDIUM"

    return {
        "risk_probability": probability,
        "risk_level": level,
        "risk_source": result.get("risk_source"),
        "reasons": result.get("reasons", [])
    }


# ==========================================
# Reste Database
# ==========================================
@app.post("/dataset/reset")
def reset_dataset():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("TRUNCATE TABLE change_events RESTART IDENTITY")

    conn.commit()

    cur.close()
    conn.close()

    return {"status": "dataset reset"}

from datetime import datetime, timedelta
import random
import uuid

from database.connection import get_connection
from database.repository import add_event, update_incident
from services.predictor import predict_risk
from services.trainer import train_model

# ==========================================
# Model Evaluation
# ==========================================

@app.get("/model/evaluate")
def model_evaluation():

    result = evaluate_model()

    return result


# ==========================================
# Generate Demo
# ==========================================   
@app.post("/dataset/generate-demo")
def generate_demo_dataset(events: int = 500):

    print(f"Generating demo dataset ({events} events)")

    conn = get_connection()
    cur = conn.cursor()

    # limpa dataset
    # cur.execute("TRUNCATE TABLE change_events RESTART IDENTITY")
    # conn.commit()

    authors = [
        "Leonardo Viana",
        "José Moura",
        "Denner Araújo",
        "Ana Couto",
        "Deurivaldo Barbosa",
        "José Borges"
    ]

    branches = [
        "feature/payment",
        "feature/user-auth",
        "feature/cart",
        "hotfix/cart",
        "feature/order-api",
        "docs/project-demo"
    ]

    change_types = ["feat", "fix", "docs", "refactor", "chore"]

    now = datetime.utcnow()

    for i in range(events):

        commit = str(uuid.uuid4())

        # gera commit timestamp realista (até 7 dias atrás)
        commit_time = now - timedelta(minutes=random.randint(10, 10000))

        commit_timestamp = commit_time.isoformat()

        risk = random.choices(
            ["LOW", "MEDIUM", "HIGH"],
            weights=[0.6, 0.3, 0.1]
        )[0]

        # métricas de mudança baseadas no risco

        if risk == "LOW":

            metrics = {
                "files_changed": random.randint(1, 2),
                "lines_added": random.randint(10, 60),
                "lines_removed": random.randint(0, 30),
                "modules_affected": 1
            }

        elif risk == "MEDIUM":

            metrics = {
                "files_changed": random.randint(3, 6),
                "lines_added": random.randint(80, 250),
                "lines_removed": random.randint(40, 150),
                "modules_affected": random.randint(2, 3)
            }

        else:

            metrics = {
                "files_changed": random.randint(7, 15),
                "lines_added": random.randint(300, 1000),
                "lines_removed": random.randint(150, 600),
                "modules_affected": random.randint(3, 6)
            }

        author = random.choice(authors)

        governance = {
            "change_type": random.choice(change_types),
            "semantic_commit": random.random() > 0.1,
            "branch_type": "feature",
            "self_approved": random.random() < 0.15
        }

        merge_request = {
            "id": None,
            "source_branch": random.choice(branches),
            "target_branch": "master"
        }

        event = {
            "commit_sha": commit,
            "commit_timestamp": commit_timestamp,
            "author": author,
            "change_metrics": metrics,
            "governance": governance,
            "merge_request": merge_request
        }

        prediction = predict_risk(event)

        add_event(event, prediction)

        # gerar incidente com base no risco

        if prediction["risk_level"] == "HIGH":

            incident = 1 if random.random() < 0.5 else 0

        elif prediction["risk_level"] == "MEDIUM":

            incident = 1 if random.random() < 0.15 else 0

        else:

            incident = 1 if random.random() < 0.03 else 0

        # gera deploy timestamp entre 1 e 60 minutos após commit
        deploy_time = commit_time + timedelta(minutes=random.randint(1, 60))

        deploy_timestamp = deploy_time.isoformat()

        update_incident(
            commit,
            incident,
            deploy_timestamp
        )

    train_model()

    return {
        "status": "demo dataset generated",
        "events": events
    }