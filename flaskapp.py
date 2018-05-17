import flask
from flask import Flask, request, render_template, session
import dash
import dash_core_components as dcc
import dash_html_components as html
import redditnlp
# redditnlp.version110()

server = flask.Flask(__name__)
z = 25
sub = 'Temple'
@server.route('/result')
def index():
	return render_template("index.html")

@server.route('/result', methods=['POST']) #Methods for HTML buttons
def result():
	main_info = redditnlp.version125_flask(sub, z)
	return render_template("result.html", main_info=main_info)



# dash app
sentiment_Score = redditnlp.version125_dash(sub, z)
app = dash.Dash(__name__, server=server, url_base_pathname='/dashapp')
app.layout = html.Div(children=[
    html.H1(children='Dashapp Sentiment '),
    html.Div(children='''
    	Dash: A web application framework for Python.
    	'''),

    dcc.Graph(
    	id='Test-graph',
    	figure={
    		'data':[
    			{'x':len(sentiment_Score),'y':sentiment_Score, 'type':'line','name':'post'},
    		],
    		'layout':{
    			'title': 'Sentiment score per reddit post for subreddit'+' '+sub
    		}
    	}
	)
])



if __name__ == "__main__":
	server.run(debug=True)