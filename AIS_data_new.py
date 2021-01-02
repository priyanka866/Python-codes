# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
#from shapely.geometry import Point
import geopandas as gpd

#read and clean data
# file = pd.read_csv("/home/musthafa/Desktop/aisdk_20181101.csv")
# df = file.loc[:,['# Timestamp', 'MMSI', 'Latitude', 'Longitude']]
# df.to_csv("/home/musthafa/Desktop/ais_data.csv")

df = pd.read_csv("/home/musthafa/Desktop/ais_data.csv")
#check for NA values
df.isnull().values.any()

#checking min and max value

min_lat = df['Latitude'].min()
max_lat = df['Latitude'].max()

min_lon = df['Longitude'].min()
max_lon =df['Longitude'].max()

# To check outlier and most of the data concentrated
#plt.scatter(df['Longitude'],df['Latitude'])
#plt.show()
#plt.savefig("/home/musthafa/Desktop/scatter_plot.jpg")
df_new= df[(df['Latitude']>25) & (df['Latitude']< 75) &
            (df['Longitude']>0) & (df['Longitude']<25)]
#df_new =df_new.head()

# creating a geometry column 
geometry = gpd.points_from_xy(df_new['Latitude'], df_new['Latitude'])
crs = {'init': 'epsg:4326'}
gdf = gpd.GeoDataFrame(df_new, crs=crs, geometry=geometry)

#this is a simple map that goes with geopandas
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
gdf.plot(ax=world.plot(figsize=(10, 6)), marker='o', color='red', markersize=1)
plt.show()
plt.savefig("/home/musthafa/Desktop/ais_plot.jpg")