from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import charts


def get_app_description():
    description_text = '''
        # Introduction
        TODO
        '''
    return dcc.Markdown(children=description_text)


def get_data_insights():
    insights = '''
        TODO
    '''
    return dcc.Markdown(children=insights)


def get_source_text():
    source_text = '''
    TODO
    Data from [Inside Airbnb](http://insideairbnb.com/get-the-data.html),
    licensed under [Creative Commons Attribution 4.0 International
    License](https://creativecommons.org/licenses/by/4.0/).
    '''
    return dcc.Markdown(children=source_text)


tab1_content = dbc.Card(
    dbc.CardBody(
        [
            dcc.RadioItems(
                ['Availability', 'Price'],
                'Availability',
                id='xaxis-type',
                inline=True
            ),
            dcc.Graph(id='my-output')
        ]
    ),
    className="mt-3",
)


def get_map():
    return dbc.Row(
        dbc.Col(
            [
                html.H2("Map", style={"margin-top": "1em"}), charts.map()       
            ],
        )
    )


def get_app_layout():
    return dbc.Container(
        [
            html.H1(children='Gent Museum',
                    style={"margin-top": "1rem"}),
            get_app_description(),
            get_map(),
            get_data_insights(),
            dbc.Row(
                [
                    dbc.Col(html.P("Created by ")),
                    dbc.Col(get_source_text(), width="auto")
                ],
                justify="between",
                style={"margin-top": "3rem"})
        ],
        fluid=True
    )


