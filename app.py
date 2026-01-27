from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello():
	# 初始版本，固定返回 “Hello, World!”
	return "Hello, World!"

if __name__ == '__main__':
	app.run(debug=True)
