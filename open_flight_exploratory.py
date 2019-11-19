#!/usr/bin/env python
# coding: utf-8

# # Datasets openflights
# https://openflights.org/data.html
# 
# ### Unique IDs :
# 
# Airports : Airport_ID
# 
# Airlines : Airline_ID
# 
# Planes : Name  


import numpy as np
import pandas as pd
import os #Concatenate path for file


# Load the data
def __load_dataset(filename, sep=','):
    dirpath = os.path.join(".","data", "openflight")
    filepath = os.path.join(dirpath, filename)
    raw_data = pd.read_csv(filepath, sep, header=None, encoding='utf-8')
    return raw_data


# Load data
_airports_raw = __load_dataset('airports.dat.xz')
_airlines_raw = __load_dataset('airlines.dat.xz')
_planes_raw = __load_dataset('planes.dat.xz')
_routes_raw = __load_dataset('routes.dat.xz')
# Name the columns
_airports_raw.columns = ['Airport_ID', 'Name', 'City', 'Country', 'IATA', 'ICAO', 'Latitude', 'Longitude', 'Altitude', 'Timezone', 'DST', 'Tz_database', 'Type', 'Source']
_airlines_raw.columns = ['Airline_ID', 'Name', 'Alias', 'IATA', 'ICAO', 'Callsign', 'Country','Active']
_planes_raw.columns   = ['Name', 'IATA', 'ICAO']
_routes_raw.columns   = ['Airline', 'Airline_ID', 'src_airport', 'src_airport_ID', 'dest_airport', 'dest_airport_ID', 'Codeshare', 'Stops', 'Equipment']


def __remove_backslash_n(dataset):
    return dataset.replace('\\N', np.nan)



def __clean_airlines(airlines_data_raw):
    airlines = airlines_data_raw.drop(airlines_data_raw[airlines_data_raw.Airline_ID == -1].index).reset_index()
    airlines = __remove_backslash_n(airlines)
    airlines[airlines.Airline_ID == 1] = airlines[airlines.Airline_ID == 1].replace('-', np.nan)
    return airlines


# Cleaned dataset
airports  = __remove_backslash_n(_airports_raw)
airlines  = __clean_airlines(_airlines_raw)
planes    = __remove_backslash_n(_planes_raw)
routes    = __remove_backslash_n(_routes_raw)

