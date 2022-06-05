from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
import charts
import pandas as pd
import sys
from datetime import datetime,timedelta

df_events = pd.read_csv(sys.path[0] + '/data/toeristische_evenementen_visit_gent.csv', sep=";")
#df_events=pd.DataFrame(df_events)

def get_app_description():
    description_text = '''Choose your preferred **dates** of stay with the calendar to see which **events** are taking place in Ghent. Underneath the map you can select your **theme** of interest and if you click on the markers across the map of Ghent you can find some additional information. All **museums** in Ghent are also visible on the map.'''
    return html.Div(children=dcc.Markdown(children=description_text), style={'margin':'auto', 'margin-top':'30px', 'margin-bottom':'30px', 'height':'110px', 'width': '70%', 'padding':'20px', 'border':'2px solid', 'border-color':'#E9E8E1', 'border-radius':'20px', 'background-color':'#F4F3ED', 'box-shadow': '5px 5px 2px -2px rgba(0, 0, 0, 0.1)'})


def get_data_insights():
    insights = '''
       
    '''
    return dcc.Markdown(children=insights)


def get_source_text():
    source_text = '''
    Data from [Stad Gent](https://data.stad.gent).
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
            html.H1(children='Gent Museums and Events',
                    style={"margin-top": "1rem", 'text-align':'center'}),
            get_app_description(),
            html.Div(
                [html.Div([html.H3('Select theme(s)', style={'text-align':'center'}), dcc.Dropdown(
                              id='event_theme',
                              options=[{'label': x,'value':x} for x in (sorted(df_events['Theme'].unique()))],
                              value = sorted(df_events['Theme'].unique()),
                              multi=True,
                              style={'margin':'auto', 'margin-top':'20px'}
                          )], style={'margin-top':'5px', 'width': '49%', 'display': 'inline-block', "verticalAlign": "top"}), html.Div([html.H3('Select date(s)', style={'text-align':'center'}),
                html.Center(dcc.DatePickerRange(
                    id='my-date-picker-range',
                    min_date_allowed=charts.get_min_date(),
                    max_date_allowed=charts.get_max_date(),
                    initial_visible_month=datetime.now().date(),
                    end_date=datetime.now().date() + timedelta(days=1),
                    start_date=datetime.now().date(),
                    style={'width':'100%', 'margin-top':'20px'}
                ))], style={'margin-top':'5px', 'width': '49%', 'display': 'inline-block', "verticalAlign": "top"})], style={'margin':'auto', 'height':'200px', 'width': '60%', 'padding':'20px', 'border':'2px solid', 'border-color':'#E9E8E1', 'border-radius':'20px', 'background-color':'#F4F3ED', 'box-shadow': '5px 5px 2px -2px rgba(0, 0, 0, 0.1)'}),
            html.Div(id='output-container-date-picker-range'),
            #get_map(),
            get_data_insights(),
            html.Div([html.H3(children='Website:'),
            html.Div(id='web_link', children=[])], style={'text-align':'center', 'margin':'auto', 'margin-top':'30px', 'height':'170px', 'width': '50%', 'padding':'20px', 'border':'2px solid', 'border-color':'#E9E8E1', 'border-radius':'20px', 'background-color':'white', 'box-shadow': '5px 5px 2px -2px rgba(0, 0, 0, 0.1)'}),
            dbc.Row(
                [
                    dbc.Col(html.P("Created by Hiba Hammi, Alexandra Ferreira, Elena Ontiveros, Inés Lallana Pérez and Lieven Ledegen.")),
                    dbc.Col(get_source_text(), width="auto")
                ],
                justify="between",
                style={"margin-top": "3rem"})
        ],
        fluid=True
    )
