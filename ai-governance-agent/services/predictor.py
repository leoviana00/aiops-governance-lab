import pickle
import os

MODEL_FILE = "storage/model.pkl"


def load_model():

    if not os.path.exists(MODEL_FILE):
        return None

    with open(MODEL_FILE, "rb") as f:
        return pickle.load(f)


def classify_risk(prob):

    if prob < 0.4:
        return "LOW"

    if prob < 0.7:
        return "MEDIUM"

    return "HIGH"


def rule_based_risk(metrics):

    files_changed = metrics["files_changed"]
    lines_added = metrics["lines_added"]
    modules = metrics["modules_affected"]

    reasons = []

    if files_changed <= 2 and lines_added <= 50 and modules <= 1:

        reasons.append("small_change")

        return 0.05, reasons

    if modules >= 4:

        reasons.append("many_modules_affected")

        return 0.85, reasons

    if lines_added >= 500:

        reasons.append("large_code_change")

        return 0.8, reasons

    return None, reasons


def predict_risk(event):

    metrics = event["change_metrics"]
    governance = event.get("governance") or {}

    # --------------------------------------
    # 1 - regras (mantido)
    # --------------------------------------

    rule_probability, reasons = rule_based_risk(metrics)

    if rule_probability is not None:

        return {
            "risk_probability": rule_probability,
            "risk_level": classify_risk(rule_probability),
            "risk_source": "rules",
            "reasons": reasons
        }

    # --------------------------------------
    # 2 - modelo ML
    # --------------------------------------

    model = load_model()

    if not model:

        return {
            "risk_probability": None,
            "risk_source": "model_not_trained"
        }

    # --------------------------------------
    # FEATURES BASE
    # --------------------------------------

    files_changed = metrics.get("files_changed", 0)
    lines_added = metrics.get("lines_added", 0)
    lines_removed = metrics.get("lines_removed", 0)
    modules_affected = metrics.get("modules_affected", 0)

    # --------------------------------------
    # GOVERNANÇA
    # --------------------------------------

    semantic_commit = 1 if governance.get("semantic_commit") else 0
    self_approved = 1 if governance.get("self_approved") else 0

    # --------------------------------------
    # CHANGE TYPE
    # --------------------------------------

    change_type = governance.get("change_type")

    is_feat = 1 if change_type == "feat" else 0
    is_fix = 1 if change_type == "fix" else 0
    is_refactor = 1 if change_type == "refactor" else 0

    # --------------------------------------
    # BRANCH TYPE
    # --------------------------------------

    branch_type = governance.get("branch_type")

    is_hotfix = 1 if branch_type == "hotfix" else 0
    is_feature_branch = 1 if branch_type == "feature" else 0

    # --------------------------------------
    # VETOR FINAL (11 FEATURES)
    # --------------------------------------

    X = [[
        files_changed,
        lines_added,
        lines_removed,
        modules_affected,

        semantic_commit,
        self_approved,

        is_feat,
        is_fix,
        is_refactor,

        is_hotfix,
        is_feature_branch
    ]]

    probability = model.predict_proba(X)[0][1]

    return {
        "risk_probability": float(probability),
        "risk_level": classify_risk(probability),
        "risk_source": "ml",
        "reasons": []
    }