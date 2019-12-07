# ANALYSIS PART 3

## Geographical trends in aviation CO2 emissions

So far we took into account the distance, the type of aircraft and the airlines. One logic way to expand our analysis is to see what does that represents in terms of countries.

As a warm-up for this part, let see the numbers of airplanes by countries.

### graph world

Well, US and China have a lot more airplanes than the others. After ensuring that these two huge numbers are not due to a data cleaning error or bad data. Indeed after a bit of Googling we realize that for example Americain Airlines is the largest airline in the world with a huge fleet and there are some really big carriers in those countries.

So let's see the rest of the world : 

### graph without US and China

This plot seems to be more representative. But there is some countries with to few airplanes. For example Botswana only has one aircraft. So our datasets do not cover all countries, we decided to put a threshold of 20 aircrafts and drop the countries that are below.

Now, we can plot the average CO2 emissions per seat for 100 km for each of the remaining countries.

### graph average CO2 emissions

This representation allows us to see where the other larger players in the aviation market are. Nevertheless, it is hard to see any trend between the number of planes and the CO2 that it is emitted per seat.

So we continue our analysis looking at a linear model for this.

### graph regression

Well, it is not successful at all. We can only conclude that there is no linear model that will explain the link between CO2 per seat (kg/100 km) and the number of planes a country has.

However, we can continue our analysis and try to find a factor between countries and average CO2 per seat (kg/100 km). So let's plot it on a map.

### graph map average CO2 per seat kg/100 km

What does this maps show us ? One first limitation that we do not have enough data for the African continent. But even excluding Africans countries, we can observe that Western countries (ie: USA, Canada, European countries) pollute more than the rest of the world. To explain that we can state two hypothesis : 

1. Higher income allow people to travel more short distances.

2. Poorer countries probably do not have a lot of internals flights.

Let's take the first one and show in a map ploting the income by person.

### graph income by person by country

The map looks good and we can say that our first hypothesis seems to be true.

However we are once again not able to show that he higher the GDP per capita is, the more a flight pollutes per seat with a regression.

### graph CO2 Emissions per seat by GPD

To go further, we tried a regression betwenn the number of planes and and the GPD per capita. In that case, we can say that the trend, Countries with higher GDP per capita tend to have more airplanes, is statistically relevant.

### graph GPD per capita vs number of planes

## Conclusion
We can see several things. First, there is big differences between countries in terms of number of airplanes and consequently air traffic. Secondly, there is indeed a group of rich country that pollute more. That could be obvious things but here we have numbers and statistics to show that.

# Analysis part 4
## Is there some better flight route for a Swiss traveller ? 

The last aspect that we want to explore with you are the flight routes. As we are based on Switzerland, we take into account only the flight route from Swiss airport.

We start with the long distance routes, so the one that go outside of the Europe.

## graph flight routes from Swiss airports

Well we do not see anything on this graph, let's remove the outliers in order to have a better view

## graph flight routes from Swiss airports without outliers

We can observe from the map above that flights that are not long hauls will have better CO2 emissions per seat than the long hauls that cross the Atlantic, or Asia. This confirms that flights that fly longer distances will pollute more per kilometer.

Let's now have a look at the European situation. We plot plot what are the less polluting by km routes from Switzerland to EU countries and we directly remove the outliers which remain the same.

## graph flight Europe

We can see from the graph above that shorter flights tend to use more fuel. This confirms the findings done in the first analysis where it was found that CO2 emissions per seat decrease rapidly when aircrafts increase their flight distance up until 6000 km. It is then not a surprise to see the longer flights on this map having higher CO2 emissions per seat.

Another element we can see on this plot is that there is better destination to go for if you care about the environment even for similar distances. In fact, we seee a broad range of colors for distances which are similar. 