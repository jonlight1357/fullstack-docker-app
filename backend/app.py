from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password=os.getenv("POSTGRES_PASSWORD"),
        host="db"
    )

@app.route("/api/data")
def data():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    now = cur.fetchone()
    conn.close()
    return jsonify({"timestamp": now[0]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
