import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_hello_default(client):
	"""测试默认返回值"""
	response = client.get('/')
	# 断言：初始版本应返回 “Hello, World!”
	assert response.data == b"Hello, World!"
