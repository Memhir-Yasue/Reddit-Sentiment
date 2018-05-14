from flask import Flask, request, render_template, session
import redditnlp


# redditnlp.version110()



app = Flask(__name__)
@app.route('/')
def index():
	return redditnlp.version111_flask()
if __name__ == "__main__":
	app.run(debug=True)