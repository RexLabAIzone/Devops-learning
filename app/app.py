from flask import Flask
import os
import pymysql


app = Flask(__name__)


DB_HOST = os.getenv("MYSQL_HOST", "mysql")
DB_USER = os.getenv("MYSQL_USER")
DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
DB_NAME = os.getenv("MYSQL_DATABASE")


def get_conn():
    return pymysql.connect(
	host=DB_HOST,
	user=DB_USER,
	password=DB_PASSWORD,
	database=DB_NAME,
	cursorclass=pymysql.cursors.DictCursor,
        ssl_disabled=True
    )

@app.route("/")
def index():
    return "Hello DevOPs + MySQL"

@app.route("/db")
def db():
    conn = get_conn()
    with conn.cursor() as cursor:
        cursor.execute("SELECT NOW() AS now_time")
        result = cursor.fetchone()
    conn.close()
    return result

@app.route("/health")
def health():
    return {"status":"ok"}


if __name__ == "__main__":

    app.run(host="0.0.0.0", ports=8000, debug=True)
