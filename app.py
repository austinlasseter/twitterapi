import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
from helpers import *
import requests
import os
import json


########### Define a few variables ######

tabtitle = 'Twitter API MDS'
sourceurl = 'www.twitter.com'
githublink = 'https://github.com/shepparjani/twitterapi.git'
placeholderinput = "#collectiveashbery"

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

###########Layout0#############
app.layout = html.Div(children=[
    html.H1("keyword searches with Twitter's API"),
    html.Div(children=[
        dcc.Input(id='input-1-state', value=placeholderinput, type='text'),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state'),
        dcc.Graph(id='figure'),
    ], classname='twelve columns'),

    # Footer
    html.Br(),
    html.Br(),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


########### Callback ###########
@app.callback(Output('output-state', 'figure'),
              Input('input-1-state', 'value'),
             )

### Is the correct variable for the parens?
def update_output(Input):

    bearer_token = "AAAAAAAAAAAAAAAAAAAAAC2eYQEAAAAA1idxHQ1U4YFvQO2kiDSrOlW2GRI%3DAFAvR8Gb8M6CjKEJMzFdlY37o1tb1QzHUZ1OgLwTbWu7GLKap0"
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    ### Question: is the below how I'd insert the reference to user input? i.e. 'query': 'input-1-state'? replaced the "#collectiveashbery"placeholder
    query_params = {'query': 'input-1-state','tweet.fields': 'author_id','user.fields': 'location', 'max_results': 25}

    def bearer_oauth(r):
        """
        Method required by bearer token authentication.
        """

        r.headers["Authorization"] = f"Bearer {bearer_token}"
        r.headers["User-Agent"] = "v2RecentSearchPython"
        return r

    def connect_to_endpoint(url, params):
        response = requests.get(url, auth=bearer_oauth, params=params)
        #print(response.status_code)
        #if response.status_code != 200:
            #raise Exception(response.status_code, response.text)
        return response.json()

    def main():
        json_response = connect_to_endpoint(search_url, query_params)
        #print(json.dumps(json_response, indent=4, sort_keys=True))
        tweetdict = json_response["data"]
        tweetdf = pd.DataFrame(tweetdict)

        #set up table
        data=go.Table(columnwidth = [200,200,1000],
                        header=dict(values=tweetdf.columns, align=['left']),
                        cells=dict(align=['left'],
                                   values=[tweetdf['author_id'].values,
                                           tweetdf['id'].values,
                                           tweetdf['text'].values])
                     )
        figure = go.Figure([data])
        return figure

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
