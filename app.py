import dash
from dash import dcc, html
from dash.dependencies import Input, Output

from api import fetch_mars_photos
from utils import format_photos

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Mars Rover Photos'),
    dcc.Dropdown(
        id='rover-dropdown',
        options=[
            {'label': 'Curiosity', 'value': 'curiosity'},
            {'label': 'Opportunity', 'value': 'opportunity'},
            {'label': 'Spirit', 'value': 'spirit'}
        ],
        value='curiosity'
    ),
    html.Br(),
    dcc.Input(id='sol-input', type='number', value=1000, min=1, step=1),
    html.Br(), html.Br(),
    html.Button('Enviar', id='submit-button', n_clicks=0),
    
    html.Div(id='output-images', children=[])
])

@app.callback(
    Output('output-images', 'children'),
    [Input('submit-button', 'n_clicks')],
    [dash.dependencies.State('rover-dropdown', 'value'),
     dash.dependencies.State('sol-input', 'value')]
)
def update_images(n_clicks, rover, sol):
    if n_clicks > 0:
        photos = fetch_mars_photos(rover, sol)
        formatted_photos = format_photos(photos)

        if formatted_photos:
            return [html.Img(src=photo['img_src'], style={'width': '300px', 'margin': '10px'}) for photo in formatted_photos[:10]]
        else:
            return html.Div("No photos found for this Sol.")
    return []

if __name__ == '__main__':
    app.run_server(debug=True)