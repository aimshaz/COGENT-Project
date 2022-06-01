# Define functions to return your charts in this file. You could also read in the data here.
import pandas as pd
import plotly.express as px
from dash import dcc
# added
import plotly.graph_objects as go
import json

import datetime as dt
import panel as pn

pn.extension()

df_museumLocations = pd.read_csv('../locaties-musea-gent.csv', sep=";")
df_events = pd.read_csv('../toeristische-evenementen-visit-gent.csv', sep=";")

columns = ['ID', 'Name_NL', 'Name_EN', 'Type', 'Lat', 'Lon', 'Date_Start', 'Date_End', 'Link']
data = []
all_start_dates = []
all_end_dates = []
    
def collectDataEvents(row):
    coords = row['location'].split()
    lat = coords[2]
    lon = coords[1][1:]
    all_start_dates.append(dt.datetime(int(row['date_start'][0:4]), int(row['date_start'][5:7]), int(row['date_start'][8:10])))
    all_end_dates.append(dt.datetime(int(row['date_end'][0:4]), int(row['date_end'][5:7]), int(row['date_end'][8:10])))
    data.append([row['identifier'], row['name_nl'], row['name_en'], 'EVENT', lat, lon, all_start_dates[len(all_start_dates)-1], all_end_dates[len(all_end_dates)-1], row['_event']])
df_events.apply(collectDataEvents, axis=1)

df_eventParsed = pd.DataFrame(data, columns = columns)
all_start_dates.sort()
all_end_dates.sort()

def getCoords(row):
    return [row['longitude'], row['latitude']]

def filterData(new_start_date, new_end_date):
    filteredDf = df_eventParsed.drop(df_eventParsed[df_eventParsed.Date_Start <= new_start_date].index)
    filteredDf = filteredDf.drop(filteredDf[filteredDf.Date_End >= new_end_date].index)
    return filteredDf

def map():
    #q1

    date_range_slider = pn.widgets.DateRangeSlider(
        name='Date Range Slider',
        start=all_start_dates[0], end=all_end_dates[len(all_end_dates)-1],
        value=(all_start_dates[0], all_end_dates[len(all_end_dates)-1]),
    )

    date_range_slider

    new_start_date = date_range_slider.value[0]
    new_end_date = date_range_slider.value[1]

    filteredDf = filterData(new_start_date, new_end_date)
    
    gent_map = json.load(open("../locaties-musea-gent.geojson"))

    fig = px.choropleth_mapbox(filteredDf, geojson=gent_map, 
                           mapbox_style="carto-positron",
                           zoom=12, center = {"lat": 51.049999, "lon": 3.733333},
                           opacity=0.5,
                          )
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    #q2
    fig.add_trace(go.Scattermapbox(lat=filteredDf['Lat'], lon=filteredDf['Lon'], name="event information", mode = 'markers', hoverinfo = 'text', marker=dict(color='LightSkyBlue'),
        hovertext = '<b>Name</b>: '+ filteredDf['Name_EN'].astype(str) +'<br>'
                    '<b>Start Date</b>: '+ filteredDf['Date_Start'].astype(str) +'<br>'
                    '<b>End Date</b>: '+ filteredDf['Date_End'].astype(str) +'<br>'
                    '<b>Link</b>: '+ filteredDf['Link'].astype(str) +'<br>'

        ,showlegend=True))

    fig.add_trace(go.Scattermapbox(lat=df_museumLocations['y'], lon=df_museumLocations['x'], name="museum information", mode = 'markers', hoverinfo = 'text', marker=dict(color='blueviolet'),
        hovertext = '<b>Name</b>: '+ df_museumLocations['naam'].astype(str) +'<br>'
        ,showlegend=True))
    
    #q3
    fig.update_layout(legend=dict(yanchor="top", x=0))

    graph = dcc.Graph(
        id="map",
        figure=fig
    )
    return graph
