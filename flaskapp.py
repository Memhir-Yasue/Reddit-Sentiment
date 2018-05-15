from flask import Flask, request, render_template, session
import redditnlp


# redditnlp.version110()



app = Flask(__name__)

@app.route('/')
def index():
	ni = []

@app.route('/newpage')
def newpage():
	num_array = [redditnlp.version120_flask() for i in range(10)]
	return render_template("index.html", num_array=num_array)




if __name__ == "__main__":
	app.run(debug=True)