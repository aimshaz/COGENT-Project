from dash.dependencies import Input, Output, State
import charts
from datetime import datetime
import pandas as pd


def register_callbacks(app):
    """Function to register all callbacks from withing app.py
    Insert all your callback functions in the body of this function.

    e.g.

    @app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
    )
    def update_output_div(input_value):
        return f'Output: {input_value}'

    """
    """ @app.callback(
    Output('my-output', 'figure'),
    Input('xaxis-type', 'value'),
    )
    def update_graph(xaxis_type):
        if xaxis_type=="Availability":
            return graph_A
        else:
            return graph_A_bis"""
    @app.callback(
    Output('output-container-date-picker-range', 'children'),
    Input('my-date-picker-range', 'start_date'),
    Input('my-date-picker-range', 'end_date'),
    Input(component_id='event_theme', component_property='value'))

    def update_output(start_date, end_date, theme):
        start_date_object = datetime.fromisoformat(start_date)
        timestamp_start = pd.Timestamp(start_date_object)
        end_date_object = datetime.fromisoformat(end_date)
        timestamp_end = pd.Timestamp(end_date_object)
        themeType=theme
        return charts.map(timestamp_start,timestamp_end, themeType)
