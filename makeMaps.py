import pandas as pd
import geopandas as gpd
import geopy
from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import geopy.distance
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

#from plotly import graph_objects as go 
#import pandas as pd 
#
data = pd.read_csv("DataWithHSVGreenVals.csv")
df = data[["Latitude","Longitude", "HSVGreen2017"]]
df.dropna()

fig = px.scatter_mapbox(df, 
                        lat = df['Latitude'],
                        lon = df['Longitude'],
                        center={"lat": 38.2655, "lon": -122.4217},
                        color=df["HSVGreen2017"],
                        mapbox_style="carto-positron",
                        color_continuous_scale='Viridis',
                        zoom=10,
                        height=700,
                        width=800
                      )
fig.show()
#
#fig = go.Figure(data=go.Scattergeo(
#        lon = df['Longitude'],
#        lat = df['Latitude'],
#        mode = 'markers',
#        marker_color = df['HSVGreen2022'],
#        ))
#
#fig.update_layout(
#        geo_scope='usa',
#    )
#
#fig.write_image("map.svg")
