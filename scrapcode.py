########### Layout1 ###########

app.layout = html.Div(children=[
    html.H1("# searches with Twitter's API"),
    # Dropdowns
    html.Div(children=[
        html.Button('Scrape Now!', id='submit-val', n_clicks=0),
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

#### Layout2 #####
#### layout
app.layout = html.Div([
    html.H1("# searches with Twitter's API"),
    html.H6("Change the value in the text box to see callbacks in action!"),
    html.Div(["Input: ",
    dcc.Input(id='my-input', value='initial value', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output'),

])
