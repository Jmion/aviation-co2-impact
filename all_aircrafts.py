from wikipedia_parsing import commuter as commuter_aircraft
from wikipedia_parsing import long_haul as long_haul_aircraft
from wikipedia_parsing import medium_haul as medium_haul_aircraft
from wikipedia_parsing import regional as regional_aircraft
from wikipedia_parsing import short_haul as short_haul_aircraft

import open_flight_exploratory
import pandas as pd

"""aircraft data from wiki with labels"""
aircraft_data = [(commuter_aircraft, "commuter_aircraft"),
                 (regional_aircraft, "regional_aircraft"),
                 (short_haul_aircraft, "short_haul_aircraft"),
                 (medium_haul_aircraft, "medium_haul_aircraft"),
                 (long_haul_aircraft, "long_haul_aircraft")]

DENSITY_OF_NONANE = 0.718
CO2_PER_G_OF_NONANE = 3.087
CO2_RATIO = 3.086

def add_co2_per_seat(data: pd.DataFrame) -> pd.DataFrame:
    data['CO2 per seat kg/100km'] = data['Fuel per seat L/100km'].apply(lambda x: x * DENSITY_OF_NONANE * CO2_PER_G_OF_NONANE)
    return

def add_co2_per_km(data: pd.DataFrame) -> pd.DataFrame:
    data['CO2 kg/km'] = data["Fuel burn kg/km"].apply(lambda x: x*CO2_RATIO)
    return

"""Adding CO2 per seat using math and chemistry described above and label on what type of plane category it is in"""
for a in aircraft_data:
    add_co2_per_seat(a[0])
    add_co2_per_km(a[0])
    a[0]["Aircraft type"] = a[1]
    
all_aircrafts = pd.concat([commuter_aircraft, regional_aircraft, short_haul_aircraft, medium_haul_aircraft, long_haul_aircraft])