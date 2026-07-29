from flask import Flask
import pymysql
import os

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_USER = os.getenv('DB_USER', 'devops')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'devops@123')
DB_NAME = os.getenv('DB_NAME', 'devops')

@app.route('/')
def index():
	try:
		conn = pymysql.connect( host=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_NAME )
		conn.close()
		return 'Flask + MySQL + Docker Compose OK!!!'
	except Exception as e:
		return f'Database connection fail: {e}'
app.run(host='0.0.0.0', port=5000, debug=True)
