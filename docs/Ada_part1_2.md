Talk about where we got the data from (wiki), add CO2 emissions

#Analysis part 1: CO2 kg/km emissions per sector size

To be able to fully understand our beautiful story, you will need a few informations about the data we worked with. The aircrafts are classified in five different categories : commuter, regional, short haul, medium haul, long haul.

Each category corresponds to a specific sector size. The sector of an aircraft is its maximum range without re-fueling. Here is a table showing the sector size associated to each category of aircraft:

|Category|Sector|
|---|---|
|Commuter|560km|
|Regional|926 - 1267km|
|Short haul|1900km|
|Medium haul|3240 - 6300km|
|Long haul|8610 - 13330km|

Also, we will be talking a lot about "pollution". For the sake of this analysis, we will consider that "polluting more or less" means that more or less kilogram of CO2 is emitted per passenger for every 100km that he/she flies.

On a first sight, with a short simple preliminary analysis, short haul aircrafts seem to pollute a little bit less. Our hypothesis is that short haul flights have less material to carry around. For example, on short haul flights, a few bathrooms on board might be sufficient, while long haul flights are operated by aircrafts that have two aisles, more bathrooms and are usually a three classes configuration. Furthermore, depending on the destination, long haul aircrafts are equipped with life rafts, and other emergency equipment that is not required to be carried on board of short haul flights. People traveling long distances also tend to pack more, making their luggage and the aircraft heavier. Finally, long haul aircrafts need to carry more fuel for longer distance flights. 

But this is only an observation based on the mean carbon emissions per seat for each category of aircraft. Let's then dig a little bit further: buckle up and enjoy the journey !

The first thing that interested us was to see if there is a relation between the CO2 emissions of an aircraft and its sector size. Obviously, if we simply look at the the mean CO2 emissions in kg/km, the results will be biased. Why ? Well, look at this:

##plot "Mean number of seats by sector [km]"

Indeed, the bigger the distance is, the more seats the plane has (because, as said before, it is also a bigger plane). What would be more interesting, would be to plot the CO2 emissions relatively to the number of seats, and that's what we have done here:

##plot "Mean CO2 emission per seat per sector km"

With this graph, we can see that most of the flights shorter than approximately 2000km pollute a lot. Also, emissions seem to reduce until 6000km, and then slowly start to grow. We think that this growth is due to the extra fuel needed for longer flights. 

So far, we can already conclude that if we are looking for an "ideal distance" to travel, it should be more than 2000km and less than, let's say, 8000km (since even if it goes up from 6000km, it stays reasonable until 8000km). But now we may want to understand why. What you saw up here were the *mean* emissions. Plotting all the data and not only the means will help us to understand what is happening.

##plot "Co2 emission per seat by sector km"

Indeed, regional and commuter aircrafts are messy. Also, one short haul aircraft is an outlier. But by hovering the mouse over the point, we see that it is a Quest Kodiak, a plane with only 9 seats which explain its CO2 emissions.

About regional and commuter aircrafts, some models have very few seats as well, for short distances. This has a direct impact on the CO2 emissions per seat and explain why our graph is so messy. 

If you think the same way as we do, you would appreciate to see the relation between CO2 emission per seat and the number of seats of an aircraft. Well, please, be our guest and look at this: 

##plot "CO2 emission per seat by number of seat"

We can obviously see a global trend. Emissions goes drastically down until 200 seats, and then goes slightly up again. This curve looks a lot like the one we found when looking at the relation between CO2 emission per seat by sector size. This confirms the relation between the sector size and the number of seats.

Let's wrap up what we got so far:

- Aircrafts that travel longer distances have usually more seats
- Aircrafts with sector size between 2000km and 6000km are the less polluant in terms of CO2 emission per seat
- Aircrafts with few seats tend to have bigger CO2 emissions per seat

One aspect that we did not take into account is the build date of the aircrafts. Indeed, we could hope that more recent planes are more efficient in terms of carbon emissions. But instead of hoping, let's find out !

##Evolution of carbon emissions through the years

In our data, we have access to the year of the first flight of each plane. For the sake of this analysis, we will consider that an aircraft with a recent first flight year, is a recent aircraft. Since we want to have a global insight, we will look at a simple linear regression for every type of aircraft.

##plot "no title but linear regression first flight CO2"

*Note that if you are curious and you want to see the slope of the line, you can hover your mouse over the line and look at the first parameter of the equation "CO2 per seat kg/100km"*

This is reassuring. For every category, planes are becoming more fuel efficient. However, there is a noticeable difference between categories. While short haul aircrafts are decreasing from 4.3% per year, regional aircrafts are decreasing from more than 9% a year.

## Conclusion for part 1

With our analysis, we found an "ideal" distance to travel: more than 2000km. Longer distances (over 8000km) pollute more, but we think that travelling with stop overs is not a solution because it would probably increase the total travel distance.

Comparing the CO2 emissions of the aviation industry with cars, aviation remains a more ecological way of transportation when traveling alone. In 2020, newly registered cars need to have an on-average CO2 production lower than 9.5 kg/100km. Currently, the limit is 13kg/100km.

(reference: https://www.bfe.admin.ch/bfe/fr/home/efficacite/mobilite/prescriptions-concernant-les-emissions-de-co2-des-voitures-de-to.html)


#Analysis part 2: Which airlines should we avoid, which one should be chosen?

Now that we have a good understanding of the relation between distance and carbon emissions, we would like to identify what type of traffic is the most polluting. We are also interested in finding the factors, if any, that make some airlines less polluant than others.

For this part, we will need to get our hands on the fleets of each airline in details. To do that, we obviously need a dataset containing informations about airlines and their fleets. Well thanks to planespotter.net, we have all the informations that we need, and even more. They nicely agreed to share their data with us for research purposes only, and we would like to thank them again for that.

Since you are probably curious, here is a short parenthesis about one issue was that we encountered when merging all the data that we had. Some aircrafts of the same model can be equipped with different number of seats. This means that the overall mass of the aircraft is slightly different and leads to a slight difference in fuel burn / km. Since we needed to have unique aircrafts models (otherwise we would not know which version of a given model to take into account), we solved this issue by grouping the all the same aircrafts models together and averaging their values (i.e. a mean). Once it was done, we had a huge dataset with a lot of informations in it. 

Now that you know the story behind our data, let's have a look at what we are interested in, starting with the trends per operator.

The criterias of the fleet of aircrafts that we are interested in are:

    Status = Active (in operation)
    Config = Pax (passenger)
    Operator Category = Airline, Leasing Company, Business Airline


You may be wondering why we are considering three operator categories, given that airlines are our main focus. Well, given how often Airlines lease aircrafts to operate their flights, considering leasing company will allow us to include another large player in the passenger transport industry. To give an example of large airlines leasing flights, we can cite the example of Norwegian. During the summer 2018, Norwegian saw part of its Boeing 787 fleet grounded due to issues with their high-bypass turbofan engine, the "Rolls Royce Trent 1000". To still be able to operate flights from London to New York, Norwegian used wet leasing from High Fly with A380 aircrafts.

##twitter

Wet leasing is a lot different than leasing, because the leasing company provides crew, pilots, maintenance, fuel, service, and even aircraft certification. 

In addition to this, including business airlines will allow us to consider more of the private sector of private jets.

Talking about aircrafts types, we had a look at the Combi aircrafts type. For those of you that are not aviation experts, here is the definition from Wikipedia of a Combi aircraft :

"Combi aircraft in commercial aviation are aircraft that can be used to carry either passengers, as an airliner, or cargo as a freighter, and may have a partition in the aircraft cabin to allow both uses at the same time in a mixed passenger/freight combination. "

In our dataset, very few aircrafts are flying a Combi setup. Amongst those aircrafts, almost half of them belong to the air force. We decided to not consider them since they are too few to be of any impact in our analysis.


##Let's look at the largest airlines in the world

We want to look only at the "big" airlines. Let's say that a big airline has at least 30 aircrafts in its fleet. 30 is an arbitrary number that narrow down all of our airlines from almost 2000 to approximately 200. We thought that keeping 10% of all of our airlines for this analysis was a reasonable choice, and this explains the choice of "30". Looking at small companies is out of the scope of this analysis.

Now that we have selected our big airlines, let's look at their individual average CO2 production.

##plot "Airline average CO2 emission per seat in kg/100km Colors..."

If you look closely, you will see that some company names are very similar. Here is the trick : most of these airlines are subsidiaries of larger airlines and are the regional operators. For example, Lufthansa CityLine is a company that belongs entirely to Lufthansa and operates flights on their behalf. More precisely, most of Lufthansa CityLine fleet are Bombardier CRJ-900. The CRJ-900 is a regional jet developed by Bombardier that entered service in 2001.

Pro tip: Aviation geek jargon "A regional jet (RJ) is a jet airliner and a regional airliner with less than 100 seats."(https://en.wikipedia.org/wiki/Regional_jet)

From what we saw on this graph, a new "arbitrary" number came to our minds: 8.
8 is the threshold that we chose, that corresponds to the mean CO2/100km emission per seat above which an airline is considered to be a big polluter.

That being said, let's look at what aircrafts are mostly flown by the airlines from our big polluter list.

##plot "Jets used for regional flights...."

Apparently, airlines that pollute a lot per passenger (still CO2 kg/100km) are mostly operating Bombardier CRJ (Canadair Regional Jet) or Embraer ERJ (Embraer Regional Jet). These are aircrafts that were designed at the turn of the century and that are not engineered to fly long distances. And if we look look closely at these mostly used aircrafts:

##plot "Distane flown vs CO2...."

We can see that most of the aircrafts that pollute a lot are used for regional flights. The worst aircrafts with regards to pollution are the Bombardier CRJ-200 and CRJ-100. The picture below is one of a CRJ-200.

##photo

These small jets are used to connect small airports to main hubs, and this brings back what we said in part 1, where we found out that small distances are the worst.

Now that our analysis about big polluters is over, we want to know who are the heroes of aviation, the ones that allow people to travel without polluting too much.

## small polluters

Again, our criteria for an airline to be a "small polluter" is arbitrary. We chose the following treshold : less than 5.55 kg/100km of CO2 per seat.
Let's break the suspense, here is a list of the small polluters among the biggest airlines:

## !!!! LIST SORTED !!!!

From looking at this list, we can see that most of them are low cost airlines. This could be explained by the fact that low cost airlines tend to squeeze more seats into an aircraft and will reduce what is included with the flight, which would probably reduce the total mass of the plane. This question would require further research., and we will discuss it at the end of our analysis.

Let's look at what aircrafts are mostly flown by the airlines in our small polluter list.

##plot "jets used by the airlines producing...."

We can see that this is mostly recent aircrafts which, as said in part one, pollute less. The Neo and Max family at Airbus and Boeing respectively are the newest kind of aircrafts that are being produced.

If our statement about more recent airplanes polluting less is true, what about the sector of those less polluant aircrafts ?

##plot "Distance that the aircraft used by the least...."

From the graph above we can see that the aircraft that is the most flown by the small polluters has a range of less than 3000km. Except for two of the aircrafts (which are not used that much), they all lay within the "optimal" range found in part 1. That makes us happy (:

Finally, let's compare the sector of aircrafts operated by big polluters and the sector of aircrafts operated by small polluters.

##plot "Average range of the big polluter aircrafts"

We can see from the histogram above that airlines that are polluting less are operating flights with aircrafts that are designed to fly further.

We can conclude from this analysis that we have found significant differences between regional airlines and low cost airlines. Flying with a low cost airline will most likely reduce your CO2 emissions per kilometer compared to fly with a regional jet. The reason of being of these two types of flights is entirely different. The purpose of regional flights is to allow passengers to stop over in one of the main hubs of the airline before continuing on with another flight. So these flights can be more expensive (burn more fuel) than flights operated by a low cost airline.

Low cost are on the other hand trying to minimize their operating costs. Since fuel expenses represent approximately 25% of their operating costs (according to https://www.statista.com/statistics/591285/aviation-industry-fuel-cost/), low cost airlines have a large interest in operating fleets of aircrafts that burn less fuel.

We would like to thank planespotters.net and Gapminder for providing us the datasets that this research required.

