import flask
from flask import Flask, request, render_template, session
from flask_caching import Cache
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import redditnlp
import user_redditnlp
# redditnlp.version110()

server = flask.Flask(__name__)
# cache_flask = Cache(server, config={'CACHE_TYPE': 'filesystem', 'CACHE_DIR': '/tmp'})
z = 20
# sub = 'Politics'

@server.route('/')
def main():
	return render_template("main.html")

@server.route('/result', methods=['POST'])
# @cache_flask.cached(timeout=0) 
def result():
    sub = request.form['subreddit']
    main_info = redditnlp.version170_flask(sub,z)

    return render_template("result_percent.html", main_info=main_info, sub=sub) # passing sub to print reddit name on result page

@server.route('/result/user', methods =['POST'])
def user():
	sub = request.form['subreddit']
	user_info = user_redditnlp.user_frm_subreddit(sub,z)

	return render_template("subredditor.html", user_info=user_info)


# @server.route('/index/result', methods=['POST']) #Methods for HTML buttons
# @cache_flask.cached(timeout=240) 
# def result():
# 	main_info = redditnlp.version125_flask(sub, z)
# 	return render_template("result.html", main_info=main_info)

# @server.route('/index/result_version150', methods=['POST']) #Methods for HTML buttons on index
# @cache_flask.cached(timeout=240)
# def result_version150():
#     main_info = redditnlp.version150_flask(sub,z)
#     return render_template("result_version150.html", main_info=main_info, sub=sub) # passing sub to print reddit name on result page



















# sub = result() 
# # dash app
# sentiment_Score = redditnlp.version125_dash(sub, z) #Calls the dash function which returns the sentiment scores
# # app starts below
# app = dash.Dash(__name__, server=server, url_base_pathname='/dashapp')
# colors = {
#     'background_chart':'#2d2d2d',
#     'background_paper':'#020202',
#     'chart':'#A9D3CE'
# }
# app.layout = html.Div(children=[
#     # html.H1(children='Dashapp Sentiment '),
#     # html.Div(children='''
#     # 	Dash: A web application framework for Python.
#     # 	'''),
#     dcc.Graph(
#     	id='Test-graph',
#     	figure={
#     		'data':[
#             go.Bar(
#                     x=len(sentiment_Score),
#                     y=sentiment_Score,
#                     opacity=0.9,
#                     marker=go.Marker(
#                         color='rgb(33, 236, 255)'
#                     )
                    
#                 )
#     			# {'x':len(sentiment_Score),'y':sentiment_Score, 'type':'bar','name':'sentiment',},
#     		],
#     		'layout':{
#                 'plot_bgcolor': colors['background_chart'], # background color inside chart
#                 'paper_bgcolor': colors['background_paper'], #color outside chart/background
#     			'title': 'Sentiment score per reddit post for'+' '+sub
#     		}
#     	}
# 	)
# ])



if __name__ == "__main__":
	server.run(debug=True)