from dash.dependencies import Input, Output, State
import charts

#graph_A = charts.get_chart_A()
#graph_A_bis = charts.get_chart_A_bis()

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
