import psycopg2
import os


def get_connection():

    return psycopg2.connect(
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
        database=os.getenv("DB_NAME", "aiops"),
        user=os.getenv("DB_USER", "aiops"),
        password=os.getenv("DB_PASSWORD", "aiops")
    )