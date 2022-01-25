import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
import requests
import pandas as pd
import datetime
import os
import json
import plotly.graph_objs as go
from helpers import *

########### Define a few variables ######

tabtitle = 'Ashbery'
sourceurl = 'www.twitter.com'
githublink = 'https://github.com/shepparjani/ashbery'


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Layout
app.layout = html.Div(children=[
    html.H1('John Ashbery quotes from Twitter'),
    html.Div(children=[
        html.Div(id='message'),
        dcc.Graph(id='figure-1'),
    ], className='twelve columns'),

    # Footer
    html.Br(),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Callbacks
@app.callback(Output('message-div', 'children')
             )

def update_quotes():
    #austins_api_key = '9eb078023ce1d3136bbb540b8fee91ca'
    #request_string = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&units=imperial&appid={austins_api_key}'
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAC2eYQEAAAAA1idxHQ1U4YFvQO2kiDSrOlW2GRI%3DAFAvR8Gb8M6CjKEJMzFdlY37o1tb1QzHUZ1OgLwTbWu7GLKap0"
    search_url = "https://api.twitter.com/2/tweets/search/recent"

# merge in below code

query_params = {'query': '#collectiveashbery','tweet.fields': 'author_id'}

def bearer_oauth(r):
    """
    Method required by bearer token authentication.
    """

    r.headers["Authorization"] = f"Bearer {bearer_token}"
    r.headers["User-Agent"] = "v2RecentSearchPython"
    return r

def connect_to_endpoint(url, params):
    response = requests.get(url, auth=bearer_oauth, params=params)
    print(response.status_code)
    if response.status_code != 200:
        raise Exception(response.status_code, response.text)
    return response.json()


def main():
    json_response = connect_to_endpoint(search_url, query_params)
    print(json.dumps(json_response, indent=4, sort_keys=True))


############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
