import flask
from flask import Flask, request, render_template, session
import dash
import dash_html_components as html
import redditnlp
# redditnlp.version110()




server = flask.Flask(__name__)


@server.route('/')
def index():
	return 'Welcome'

@server.route('/result')
def result():
	main_info = redditnlp.version125_flask(10)
	return render_template("index.html", main_info=main_info)

# dash app
app = dash.Dash(__name__, server=server, url_base_pathname='/dashapp')
app.layout = html.Div(children=[
    html.H1(children='Dash App')])



if __name__ == "__main__":
	server.run(debug=True)