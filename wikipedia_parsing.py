#!/usr/bin/env python
# coding: utf-8

import pandas as _pd
from requests import get as _get
from requests import codes as _codes
from bs4 import BeautifulSoup as _BeautifulSoup
import lzma as _lzma
import os as _os
import pickle as _pickle


_path = _os.path.join(".", "data","wikipedia","wiki_page.data.zx")
if(_os.path.isfile(_path)): #Check that local version of website exists
    with _lzma.open(_path, "rb") as _wiki_file:
        print("loading wikipedia data from hard drive")
        _r = _pickle.load(_wiki_file)
else:
    try:
        _url = 'https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft'
        _r = _get(url)
        print("fetching online wikipedia page")
        if(_r.status_code == _codes.ok): 
            with _lzma.open(_path, "wb") as _wiki_file:
                _pickle.dump(_r, _wiki_file) # Store fetched page to local storage
        else:
            raise Exception("Cannot find local version of wikipedia data and website not responding with 200.")
    except:
        raise Exception("Cannot access the internet")
        
_soup = _BeautifulSoup(_r.text, 'html.parser')


# Parsing of the website to extract the relevant information
_dataframes = []
for _table in _soup.find_all("table"):
    _table_headers = []
    _dict_plane = {}
    for _header in _table.find_all("th"):
        _head = _header.text.replace("\n", "")
        _table_headers.append(_head)
        _dict_plane[_head] = []
    for _line in _table.find_all("tr"):
        for _i, _elem in enumerate(_line.find_all('td')):
            _dict_plane[_table_headers[_i]].append(_elem.text.replace("\n", ""))
    _dataframes.append(_dict_plane)
    
_dataframes = _dataframes[:-1] #We don't want the private jets
print("There are " + str(len(_dataframes))+ " dataframes")


# Aircraft information seperated by distance that they can fly
_commuter = _pd.DataFrame.from_dict(_dataframes[0]) # 560km
_regional = _pd.DataFrame.from_dict(_dataframes[1]) # 926km - 1267km
_short_haul = _pd.DataFrame.from_dict(_dataframes[2])# 1900km
_medium_haul = _pd.DataFrame.from_dict(_dataframes[3]) # 3240km - 6300km
_long_haul = _pd.DataFrame.from_dict(_dataframes[4]) # 8610km - 13330km

# Add missing sector
_commuter["Sector"] = "560"
_short_haul["Sector"] = "1900"

# Rename columns so that all the DF have same column names
_regional = _regional.rename(columns={"Fuel efficiency per seat": "Fuel per seat"})
_short_haul = _short_haul.rename(columns={"Fuel efficiency per seat": "Fuel per seat", "Fuel Burn": "Fuel burn"})

# Helper method to reorder the DF with sector at the end
def _reorder_df(df):
    return df[["Model", "First flight", "Seats", "Fuel burn", "Fuel per seat", "Sector"]]

_regional = _reorder_df(_regional)
_medium_haul = _reorder_df(_medium_haul)
_long_haul = _reorder_df(_long_haul)


# Clean fields

def _clean_sector(x):
    sector = x.split("(")
    # If no "(" in x, the sector is already clean
    if(len(sector) < 2):
        return float(x)
    return float(sector[1].split("k")[0].replace(",", ""))

def _clean_df(df):
    new_df = df[["Model", "Seats", "First flight", "Fuel burn", "Fuel per seat", "Sector"]].copy()
    new_df["First flight"] = new_df["First flight"].apply(lambda x: int(x))
    new_df["Fuel burn"] = new_df['Fuel burn'].apply(lambda x: float(x.split("k")[0]))
    new_df["Fuel per seat"] = new_df['Fuel per seat'].apply(lambda x: float(x.split("L")[0])) 
    new_df["Seats"] = new_df["Seats"].apply(lambda x: int(x))
    new_df["Sector"] = new_df["Sector"].apply(lambda x: _clean_sector(x))
    return new_df.rename(columns={"Fuel burn": "Fuel burn kg/km", "Fuel per seat": "Fuel per seat L/100km", "Sector": "Sector km"})


# public variables to be imported elewhere.
commuter = _clean_df(_commuter)
regional = _clean_df(_regional)
short_haul = _clean_df(_short_haul)
medium_haul = _clean_df(_medium_haul)
long_haul = _clean_df(_long_haul)
