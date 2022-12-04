'''
Our composants using Card in Dash boostrap components to nicely plot our api results
'''


import dash_bootstrap_components as dbc
from dash import html

def card(title, description, rating, image) :
    return dbc.Card([
                dbc.CardImg(src=image, bottom=True, className="mycard"),
                dbc.CardBody([
                    html.H4(title, className="mycard-title"),
                    html.P([description,], className='mycard-description'),
                    html.P([f"{str(rating)}"], className='mycard-text'),
                    html.P(["IMDB ratings",], className='mycard-kpi')     
                ]),
            ], className="mycard")