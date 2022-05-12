# Define functions to return your charts in this file. You could also read in the data here.
import pandas as pd
import plotly.express as px
from dash import dcc
# added
import plotly.graph_objects as go
import json


df_museumLocations = pd.read_csv('../locaties-musea-gent.csv', sep=";")
df_events = pd.read_csv('../toeristische-evenementen-visit-gent.csv', sep=";")

columns = ['ID', 'Name_NL', 'Name_EN', 'Type', 'Lat', 'Lon', 'Date_Start', 'Date_End', 'Link']
data = []

def collectDataMuseum(row):
    data.append([row['objectid'], row['naam'], row['naam'], 'MUSEUM', row['y'], row['x'], '', '', ''])  
def collectDataEvents(row):
    coords = row['location'].split()
    lat = coords[2]
    lon = coords[1][1:]
    data.append([row['identifier'], row['name_nl'], row['name_en'], 'EVENT', lat, lon, row['date_start'], row['date_end'], row['_event']])

df_museumLocations.apply(collectDataMuseum, axis=1) 
df_events.apply(collectDataEvents, axis=1)

df = pd.DataFrame(data, columns = columns)

def getCoords(row):
    return [row['longitude'], row['latitude']]

def map():
    #q1
    gent_map = json.load(open("../locaties-musea-gent.geojson"))

    fig = px.choropleth_mapbox(df, geojson=gent_map, color=df.Type,
                            color_continuous_scale="Viridis",
                           range_color=(50, 150),
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 51.049999, "lon": 3.733333},
                           opacity=0.5,
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    #q2
    fig.add_trace(go.Scattermapbox(lat=df['Lat'], lon=df['Lon'], name="museum and event information", mode = 'markers', hoverinfo = 'text', 
        hovertext = '<b>Name</b>: '+ df['Name_EN'].astype(str) +'<br>'
        ,showlegend=True))
    
    #q3
    fig.update_layout(legend=dict(yanchor="top", x=0))

    graph = dcc.Graph(
        id="map",
        figure=fig
    )
    return graph
