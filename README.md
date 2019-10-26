# Aviation carbon emissions

## Abstract
The idea of the project is to fact check aviation myths. Aviation and its contribution to climate change are a thematic that is currently being talked about in our parliament. Let's not look at the media or our government to give us the facts, we want to extract the truth from the underlying facts to let the data speak for itself on the contribution of aviation to climate change. We would also like to explore other facts such as seasonal effects on delays in airports to see if there are periods in the year that are less likely to be affected. The aviation industry is quite protective of its data but some openSource datasets are available to allow users to do these analytics that we want. Sadly no estimates can be made on the ideal time to purchase tickets or more precisely any ticket price analysis since all of the data that we found online on this topic requires users to pay money.


## Research questions

* What is the average CO2 emissions per passenger by airline?
* Are new airplanes polluting less than old ones and by how much?
* Is there an ideal distance to travel to reduce our CO2 emissions per km?


* What routes are the most flown?
* Which country has the most airports?
* What country has the most airports by population?
* What country has the most airports by surface area of the country?
* Why not try to do a realtime CO2 calculation using a public API
* Are airplanes usually on time? What days of the week are better to avoid delays? Are delays more frequent in the winter? Are airplanes more likely to be diverted during the winter? (US bassed dataset for this provided by the Bureau of Transporation statistics)

## Datasets

* https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

Used for airplanes average seat number and fuel burn

* https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

ISO-3166 country code dataset

* https://openflights.org/data.html#route

List of airlines:


| Name       | Description                                                                                                                                                                                                                                                            |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Airline ID | Unique OpenFlights identifier for this airline.                                                                                                                                                                                                                        |
| Name       | Name of the airline.                                                                                                                                                                                                                                                   |
| Alias      | Alias of the airline. For example, All Nippon Airways is commonly known as "ANA".                                                                                                                                                                                      |
| IATA       | 2-letter IATA code, if available.                                                                                                                                                                                                                                      |
| ICAO       | 3-letter ICAO code, if available.                                                                                                                                                                                                                                      |
| Callsigne  | Airline callsign.                                                                                                                                                                                                                                                      |
| Country    | Country or territory where airline is incorporated.                                                                                                                                                                                                                    |
| Active     | "Y" if the airline is or has until recently been operational, "N" if it is defunct. This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as "Y". |


* https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat

List of routes if we don't manage to get access to more recent data.

* https://www.transtats.bts.gov/databases.asp?Mode_ID=1&Mode_Desc=Aviation&Subject_ID2=0

Delay information of the US aviation industry. Name of the dataset is Airline On- Time performance data


### Annexe

* https://ourairports.com

List of airports in the world.


* https://developers.google.com/maps/documentation/

Distance travelld by car

* https://github.com/juliuste/flix

Flix bus data.

* https://opensky-network.org/data/impala

ADS-B positionning history. Dataset partners by Swiss confederation, Bern university, Oxford University

* https://dev.blablacar.com/hc/en-us/articles/360009002899--API-documentation

BlaBla car API

## Milestones

Fetch clean and check integrity of datasets.
Merge datasets and compute awnsers to questions

## Questions for TA

* Can we 

