from flask import Flask, request, render_template, session
import redditnlp






app = Flask(__name__)
@app.route('/')
def index():
	# redditnlp.version106()
	return 'Hello, World'
if __name__ == "__main__":
	app.run(debug=True)