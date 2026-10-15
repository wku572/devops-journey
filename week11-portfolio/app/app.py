import os

import psycopg2
from flask import Flask

app = Flask(__name__)


def get_conn():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["POSTGRES_DB"],
        user=os.environ["POSTGRES_USER"],
        password=os.environ["POSTGRES_PASSWORD"],
    )


def init_db():
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "CREATE TABLE IF NOT EXISTS visits ("
                "id SERIAL PRIMARY KEY, visited_at TIMESTAMPTZ DEFAULT now())"
            )
    finally:
        conn.close()


@app.route("/")
def index():
    conn = get_conn()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("INSERT INTO visits DEFAULT VALUES")
            cur.execute("SELECT count(*) FROM visits")
            count = cur.fetchone()[0]
    finally:
        conn.close()
    return f"Hello from Docker Compose! This page has been visited {count} times.\n"


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
