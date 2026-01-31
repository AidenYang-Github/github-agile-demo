import pytest
from app import app

@pytest.fixture
def client():
	with app.test_client() as client:
		yield client

def test_hello_with_name(client):
	"""测试带name参数的请求"""
	response = client.get('/?name=Alice')
	# 新断言：应返回 “Hello, Alice!”
	assert b"Hello, Alice!" in response.data

def test_hello_without_name(client):
	"""测试不带name参数的请求"""
	response = client.get('/')
	# 新断言：默认应返回 “Hello, World!”
	assert b"Hello, World!" in response.data
