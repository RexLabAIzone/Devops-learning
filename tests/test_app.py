from compose.app.app import app

def test_index():
	client = app.test_client()
	response = client.get('/')
	assert respose.status.code == 200
