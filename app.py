'''
Python app in dash to implement our api

Our api have for objective to return informations and rate for an given input (Movie's name).
See my_api.py in the scripts folder
'''

from dash import Dash, dcc, html, Input, Output, State
from scripts.my_api import RequestMovie
from scripts.card import card
import dash_bootstrap_components as dbc

IMDB_KEY = "YOUR_IMDB_KEY"   

app = Dash(__name__)
'''
Three layer in the app :

The banner with the app's name and the icon
The zone to search a movie
Our api's return in form of a card
'''

app.layout = html.Div([
    html.Div([
        html.H1("MovieSearcher"),
        html.Img(src="/assets/image.png")
    ], className="banner"),
    html.Div([
        html.H2("Search for a movie"),
        dcc.Input(id='movie-on-submit', type='text'),
        html.Button('Submit', id='submit-movie', n_clicks=0)
    ], className="searcher"),
    html.Div(id='container-movie-results',
             children='Enter a value and press submit', className="results")
], className='app')

'''
callback used to call the update_output function when the button is pressed
'''
@app.callback(
    Output('container-movie-results', 'children'),
    Input('submit-movie', 'n_clicks'),
    State('movie-on-submit', 'value')
)

def update_output(n_clicks, value):
    '''
    Function used to update the results part when called
    Params :
    n_clicks : the number if times the button is pressed
    value : Value of the input

    Default : No search yet
    Empty : Enter a name
    Not empty : card with the information retrieved by our api
    '''
    if n_clicks == 0 :
        return 'No search yet'
    
    if value is None :
        return 'Enter a name'
    
    movie = RequestMovie(IMDB_KEY).get_movie(value)
    return dbc.Container(
    html.Div(
        [
            html.H1("Movie List", style={"justify-content":"center"}),
            dbc.Row(
                [
                    card(movie.title, movie.description, movie.rate, movie.image),
                ],
                className="mycards",
            ),
        ]
    )
)
    
   
if __name__ == '__main__':
    app.run_server(debug=True)