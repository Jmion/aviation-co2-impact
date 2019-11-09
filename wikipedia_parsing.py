#!/usr/bin/env python
# coding: utf-8

# In[32]:

import pandas as _pd
from requests import get
from bs4 import BeautifulSoup as _BeautifulSoup


# In[33]:


_url = 'https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft'
_r = get(_url)
_soup = _BeautifulSoup(_r.text, 'html.parser')


# In[34]:


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


# In[35]:


_commuter = _pd.DataFrame.from_dict(_dataframes[0]) # 560km
_regional = _pd.DataFrame.from_dict(_dataframes[1]) # 926km - 1267km
_short_haul = _pd.DataFrame.from_dict(_dataframes[2])# 1900km
_medium_haul = _pd.DataFrame.from_dict(_dataframes[3]) # 3240km - 6300km
_long_haul = _pd.DataFrame.from_dict(_dataframes[4]) # 8610km - 13330km


_regional.columns = ["Model", "First flight", "Seats", "Sector", "Fuel burn", "Fuel per seat"]



_short_haul.columns = ["Model", "First flight", "Seats", "Fuel burn", "Fuel per seat"]

# # CO2 emissions
# 
# For 1kg of fuel, 3.304kg of CO2 is emitted

# In[41]:


CO2_ratio = 3.086


# ## Keep only useful field

# In[46]:


def _clean_fuel_burn(x):
    return float(x.split("k")[0])

def _clean_fuel_per_seat(x):
    return float(x.split("L")[0])

def _clean_df(df):
    new_df = df[["Model", "Fuel burn", "Fuel per seat"]].copy()
    new_df["Fuel burn"] = [_clean_fuel_burn(x) for x in new_df["Fuel burn"]]
    new_df["Fuel per seat"] = [_clean_fuel_per_seat(x) for x in new_df["Fuel per seat"]]
    new_df["CO2 kg/km"] = [x*CO2_ratio for x in new_df["Fuel burn"]]
    return new_df.rename(columns={"Fuel burn": "Fuel burn kg/km", "Fuel per seat": "Fuel per seat L/100km"})


# In[47]:


commuter = _clean_df(_commuter)
regional = _clean_df(_regional)
short_haul = _clean_df(_short_haul)
medium_haul = _clean_df(_medium_haul)
long_haul = _clean_df(_long_haul)
