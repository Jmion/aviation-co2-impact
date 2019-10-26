# Aviation carbon emissions

## Abstract

Talking about being "eco responsible" is the trend. We are told by newspapers, scientists, social medias and Greta that we should consume less, or at least make efforts. Since in our team, we are true students, we were already talking about the next summer holidays. In the middle of the discussion, we suddenly became worried about a particular aspect of the holidays.

This is why, for this research, we decided to focus on planes. Indeed, planes are subject to more and more taxes, and are criticized for being extra pollutant. But is it really true ? In our analysis, we are going to compute and measure different metrics related to CO2 emissions of airplanes and airlines. The outcome should help us to be aware of the impact of our travel decisions. For example: "Does the choice of the airline company have an impact on my carbon footprint?".

## Research questions

We chose four main questions, that will be in the center of our research. We also selected three secondary questions, which aim to help us building our argumentation around the main questions.

### Main questions

* What is the average CO2 emissions per passenger?
* Is there significant difference in CO2 emissions between different airlines?
* Are new airplanes polluting less than old ones and by how much?
* Is there an ideal distance to travel to reduce our CO2 emissions per km?

### Secondary questions

* What routes are the most flown?
* Which country has the most airports?
* Are airplanes usually on time? Does this have an impact on CO2 emissions?

## Datasets

Even though the aviation industry is quite protective of its data, we were able to find several open source datasets that will help us to achieve our goal:

* https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

By scraping this page, we will infer the following informations: airplanes average seat number and fuel burn (CO2)

* https://github.com/lukes/ISO-3166-Countries-with-Regional-Codes/blob/master/all/all.csv

ISO-3166 country code dataset

* https://openflights.org/data.html

List of routes (up to 2014) and planes models

* https://www.transtats.bts.gov/databases.asp?Mode_ID=1&Mode_Desc=Aviation&Subject_ID2=0

Delay information of the US aviation industry. Name of the dataset is Airline On- Time performance data

* https://opensky-network.org/data/impala

Historical data of aircrafts. Dataset partners by Swiss confederation, Bern university, Oxford University

### Annexe

These annexe sources, will be used either for secondary questions or further analysis:

* https://ourairports.com

List of airports in the world

* https://developers.google.com/maps/documentation/

Google maps API (could be used for car comparison)

* https://github.com/juliuste/flix

Flix bus API (could be used for bus comparison)

* https://dev.blablacar.com/hc/en-us/articles/360009002899--API-documentation

BlaBla car API (could be used for car sharing comparison)

## Internal milestones up until milestone 2

* Data wrangling:
  * Explore the data
  * Fetch clean and check integrity of datasets (pre-processing)
* Merge datasets and compute anwsers to questions:
  * Check feasibility of unanswered questions 
* Analysis of obtained results
* Choose and test tools for visualization of results

## Questions for TAs

* None for now
