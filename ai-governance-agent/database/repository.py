from database.connection import get_connection


# ==========================================
# Inicialização do banco
# ==========================================

def init_db():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS change_events (

            id SERIAL PRIMARY KEY,

            commit_sha VARCHAR(120),

            commit_timestamp TIMESTAMP,
            deploy_timestamp TIMESTAMP,

            author VARCHAR(120),

            files_changed INT,
            lines_added INT,
            lines_removed INT,
            modules_affected INT,

            change_type VARCHAR(30),
            semantic_commit BOOLEAN DEFAULT FALSE,
            branch_type VARCHAR(30),
            self_approved BOOLEAN DEFAULT FALSE,

            mr_id VARCHAR(50),
            mr_source_branch VARCHAR(120),
            mr_target_branch VARCHAR(120),

            incident INT DEFAULT 0,

            risk_probability FLOAT,
            risk_level VARCHAR(20),
            risk_source VARCHAR(20),

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # garante colunas em caso de upgrade
    cur.execute("ALTER TABLE change_events ADD COLUMN IF NOT EXISTS commit_timestamp TIMESTAMP")
    cur.execute("ALTER TABLE change_events ADD COLUMN IF NOT EXISTS deploy_timestamp TIMESTAMP")

    conn.commit()

    cur.close()
    conn.close()


# ==========================================
# Persistir evento de mudança
# ==========================================

def add_event(event, prediction=None):

    conn = get_connection()
    cur = conn.cursor()

    metrics = event.get("change_metrics") or {}
    governance = event.get("governance") or {}
    mr = event.get("merge_request") or {}

    commit_sha = event.get("commit_sha")
    commit_timestamp = event.get("commit_timestamp")

    risk_probability = None
    risk_level = None
    risk_source = None

    # --------------------------------------
    # cálculo de risco
    # --------------------------------------

    if prediction:

        risk_probability = prediction.get("risk_probability")
        risk_source = prediction.get("risk_source")

        if risk_probability is not None:

            if risk_probability >= 0.7:
                risk_level = "HIGH"
            elif risk_probability >= 0.4:
                risk_level = "MEDIUM"
            else:
                risk_level = "LOW"

    # --------------------------------------
    # persistência
    # --------------------------------------

    cur.execute("""
        INSERT INTO change_events
        (
            commit_sha,
            commit_timestamp,
            author,

            files_changed,
            lines_added,
            lines_removed,
            modules_affected,

            change_type,
            semantic_commit,
            branch_type,
            self_approved,

            mr_id,
            mr_source_branch,
            mr_target_branch,

            incident,
            risk_probability,
            risk_level,
            risk_source
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (

        commit_sha,
        commit_timestamp,
        event.get("author"),

        metrics.get("files_changed"),
        metrics.get("lines_added"),
        metrics.get("lines_removed"),
        metrics.get("modules_affected"),

        governance.get("change_type"),
        governance.get("semantic_commit", False),
        governance.get("branch_type"),
        governance.get("self_approved", False),

        mr.get("id"),
        mr.get("source_branch"),
        mr.get("target_branch"),

        event.get("incident", 0),
        risk_probability,
        risk_level,
        risk_source
    ))

    conn.commit()

    cur.close()
    conn.close()


# ==========================================
# Atualizar incidente + deploy timestamp
# ==========================================

def update_incident(commit_sha, incident, deploy_timestamp=None):

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        UPDATE change_events
        SET incident = %s,
            deploy_timestamp = %s
        WHERE commit_sha = %s
    """, (incident, deploy_timestamp, commit_sha))

    conn.commit()

    cur.close()
    conn.close()


# ==========================================
# Dataset para treinamento ML (ENRIQUECIDO)
# ==========================================

def load_dataset():

    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT
            files_changed,
            lines_added,
            lines_removed,
            modules_affected,
            incident,

            semantic_commit,
            self_approved,
            change_type,
            branch_type

        FROM change_events
    """)

    rows = cur.fetchall()

    dataset = []

    for r in rows:

        dataset.append({
            "files_changed": r[0],
            "lines_added": r[1],
            "lines_removed": r[2],
            "modules_affected": r[3],
            "incident": r[4],

            # novos campos para ML
            "semantic_commit": r[5],
            "self_approved": r[6],
            "change_type": r[7],
            "branch_type": r[8]
        })

    cur.close()
    conn.close()

    return dataset