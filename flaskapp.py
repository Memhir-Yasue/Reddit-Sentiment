import flask
from flask import Flask, request, render_template, session
from flask_caching import Cache
import dash
import dash_core_components as dcc
import dash_html_components as html
import redditnlp
# redditnlp.version110()

server = flask.Flask(__name__)
cache_flask = Cache(server, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})
z = 50
sub = 'temple'

@server.route('/')
def main():
	return render_template("main.html")

@server.route('/index')
def index():
	return render_template("index.html")

@server.route('/index/result', methods=['POST']) #Methods for HTML buttons
@cache_flask.cached(timeout=120)
def result():
	main_info = redditnlp.version125_flask(sub, z)
	return render_template("result.html", main_info=main_info)



# dash app
sentiment_Score = redditnlp.version125_dash(sub, z)
# app starts below
app = dash.Dash(__name__, server=server, url_base_pathname='/index/dashapp')
app.layout = html.Div(children=[
    html.H1(children='Dashapp Sentiment '),
    html.Div(children='''
    	Dash: A web application framework for Python.
    	'''),

    dcc.Graph(
    	id='Test-graph',
    	figure={
    		'data':[
    			{'x':len(sentiment_Score),'y':sentiment_Score, 'type':'bar','name':'post'},
    		],
    		'layout':{
    			'title': 'Sentiment score per reddit post for subreddit'+' '+sub
    		}
    	}
	)
])



if __name__ == "__main__":
	server.run(debug=True)