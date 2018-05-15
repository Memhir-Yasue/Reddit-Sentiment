from flask import Flask, request, render_template, session
import redditnlp


# redditnlp.version110()



app = Flask(__name__)

@app.route('/')
def index():
	ni = []

@app.route('/newpage')
def newpage():
	main_info = redditnlp.version125_flask(10)
	# main_infoee = ['Hi','I like','YOU!','bye!']

	return render_template("index.html", main_info=main_info)




if __name__ == "__main__":
	app.run(debug=True)