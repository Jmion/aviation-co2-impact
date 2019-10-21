# Aviation impact on the world

## Abstract
The idea of the project is to fact check aviation myths. Aviation and it's contribution to climate change are a thematic that is currently being talked about in our parliament. Let's not look at the media or our government to give us the facts, we want to extract the truth from the underlying facts to let the data speak for itself on the contribution of aviation to climate change. We would also like to explore other facts such as seasonal effects on delays in airports to see if there are periods in the year that are less likely to be affected. The aviation industry is quite protective of it's data but there are some openSource datasets that are available to allow use to do these analytics that we want. Sadly no estimates can be made on the ideal time to purchase tickets or more precisely any ticket price analysis since all of the data that we found online on this topic requires use to pay money.


## Datasets


* Airplanes pollute a lot?
* CO2 estimation by aircraft,  type / airline
* What routes are the most flown?
* Which country has the most airports?
* What country has the most airports by population?
* What country has the most airports by surface area of the country?
* How old are planes? (by destination, departure / airport and country)
* Why not try to do a realtime CO2 calculation using a public API
* Average CO2 per passenger by airline
* Are new airplanes polluting less than old ones and by how much?
* Are airplanes usually on time? What days of the week are better to avoid delays? Are delays more frequent in the winter? Are airplanes more likely to be diverted during the winter? (US bassed dataset for this provided by the Bureau of Transporation statistics)

## Datasets

* https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

Used for airplanes average seat number and fuel burn

* https://ourairports.com

List of airports in the world


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

List of routes if we don't manage to get access to more recent data
* https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat

* https://www.transtats.bts.gov/Fields.asp

