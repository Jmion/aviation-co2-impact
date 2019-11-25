# Aviation and global carbon emissions

## Milestone 2 deliverable 
All the milestone 2 materials are in the notebook Milestone2.ipynb. As there is some interactive visualization in the notebook, you can find the rendered version here : https://nbviewer.jupyter.org/github/Jmion/aviation-co2-impact/blob/master/Milestone2.ipynb

Note : all graphs are not finalized, there could be some missing colorscales or caption.

## Abstract

Talking about being "eco responsible" is the trend. We are told by newspapers, scientists, social medias and Greta that we should consume less, or at least make efforts. Since in our team, we are true students, we were already talking about the next summer holidays. In the middle of the discussion, we suddenly became worried about a particular aspect of the holidays.

This is why, for this research, we decided to focus on planes. Indeed, planes are subject to more and more taxes, and are criticized for being extra pollutant. But is it really true ? In our analysis, we are going to compute and measure different metrics related to CO2 emissions of airplanes and airlines. The outcome should help us to be aware of the impact of our travel decisions. For example: "Does the choice of the airline company have an impact on my carbon footprint?".

## Research questions

We chose four questions that will help us to approach our research theme, which is the role of aviation in the global carbon emissions.

### Questions

## Initial questions

* What role does aviation play in the global carbon emissions?
  * Is there significant difference in CO2 emissions between different airlines?
  * Is there an ideal distance to travel to reduce our CO2 emissions per km?
  * Are airplanes usually on time? Does this have an impact on CO2 emissions?
  
## Updated questions - **NEW**

During our analysis, we noticed that it could also be interesting, in addition to the airlines, to focus on carbon emissions by country. We also spent some time trying to look at delays, but we realized that it would produce irrelevant results, since aircrafts tend to catch up departure delays on route, leading to on-time arrivals. It would have been complicated calculating the increase of fuel burn, due to the dependance of multiple variable and the specificity of every aicraft.

* What role does aviation play in the global carbon emissions?
  * Is there an ideal distance to travel to reduce our CO2 emissions per km?
  * Is there significant difference in CO2 emissions between different airlines?
  * ~~Are airplanes usually on time? Does this have an impact on CO2 emissions?~~
  * **Is there a significant difference in CO2 emissions between different countries ?**
  * **Are there better destinations for a Swiss traveller according to the CO2 emissions per kilometer ?** 

## Datasets

**Note :** Some of the listed datasets are not available in the data folder. This is due to licence constraints of the following datasets.

Even though the aviation industry is quite protective of its data, we were able to find several open source datasets that will help us to achieve our goal:

*Update Milestone 2 : only the dataset used are listed, others that were mentionned in Milestone 1 and not used are removed*

* https://en.wikipedia.org/wiki/Fuel_economy_in_aircraft

By scraping this page, we will infer the following informations: airplanes average seat number and fuel burn (CO2). 

*Used for answering all the questions as it is the based for the CO2 emissions computations*

* https://openflights.org/data.html

List of routes (up to 2014) and planes models. *Used for answering the second question*

* ~~https://www.transtats.bts.gov/databases.asp?Mode_ID=1&Mode_Desc=Aviation&Subject_ID2=0~~

~~Delay information of the US aviation industry. Name of the dataset is Airline On- Time performance data~~

*We did not use this data because we are not looking at whether aircrafts are on time or not anymore.*

* https://opensky-network.org/data/impala

Historical data of aircrafts. Dataset partners by Swiss confederation, Bern university, Oxford University 

*Used for answering the 4th question*

**NEW** 

* https://www.planespotters.net

All aircrafts models by airline *Used for answering all the questions as it is the based for the CO2 emissions computations*

* Gapminder (https://www.gapminder.org/data/)

Only the dataset income_per_person_gdppercapita_ppp_inflation_adjusted.csv was downloaded and used in this analysis.

*Used for comparison with income per person in the third question (about country)*

## Internal milestones up until milestone 2

* Data wrangling:
  * Explore the data
  * Fetch clean and check integrity of datasets (pre-processing)
* Merge datasets and compute anwsers to questions:
  * Check feasibility of unanswered questions 
* Analysis of obtained results
* Choose and test tools for visualization of results

## Internal milestones up until Presentation
* Week 11 :
  * Extracting main information from Milestone 2 to put in the data story
* Week 12 :
  * Writting the text of the data story for questions 1 and 2 (about distance and airlines)
  * Plot meaningful information for those questions
* Week 13:
  * Writting the text of the data story for questions 2 and 3 (about countries and routes)
  * Plot meaningful information for those questions
* Week 14: 
  * Clean the final notebook
  * Put all parts of the data story together
  * Format and clean the data story
  * **Milestone 3 on 20th of December**
* Chrismas break :
  * Produce the poster
    * Select informations to integrate on the poster
    * Make data visualisation for the poster
    * Format the poster
* January 6 - 10 : 
  * print the poster at https://repro.epfl.ch (closed until January 3)
  * Logistic for presentation
* January 13 - 19 :
  * Presentation fine tuning
* January 20 :
  * **Presentation**

## Questions for TAs

* None for now
