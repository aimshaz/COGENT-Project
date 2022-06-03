from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import charts
import pandas as pd

df_events = pd.read_csv('../toeristische-evenementen-visit-gent1.csv', sep=";")
#df_events=pd.DataFrame(df_events)

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
            html.Div([
                dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=charts.get_min_date(),
                    max_date_allowed=charts.get_max_date(),
                    initial_visible_month=charts.get_min_date(),
                    end_date=charts.get_max_date(),
                    start_date=charts.get_min_date()
                ),
                html.Div(id='output-container-date-picker-range'),
          
                dcc.Dropdown(
                              id='event_theme',
                              options=[{'label': x,'value':x} for x in (sorted(df_events['Theme'].unique()))],
                              value = sorted(df_events['Theme'].unique()),
                              multi=True
                          ),
         
            ]),
            #get_map(),
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
