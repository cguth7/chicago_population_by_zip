Hello this is charlie's data sample. In this data sample I plot population change in chicago by zipcode between 2015 and 2020. 
Notebooks should be read in order | 1. data.ipynb | 2. cleaning.ipynb | 3. maps.ipynb | 

1. I use a python zipcode package to get chicago zipcodes. Then I use the census API with - https://github.com/datamade/census - a python wrapper created by datamade. 
You can find this code in the notebook called data.ipynb

2. Next I clean the data in the notebook called cleaning.ipynb

3. Finally I plot the data (and do a bit more cleaning) in the notebook called maps.ipynb

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Folders: 
- chi_zips: where I saved the dataframes with zip and population data
- mapping: Contains chicago zipcodes shapefile, I used this to plot the map. Found it on https://data.cityofchicago.org/Facilities-Geographic-Boundaries/Boundaries-ZIP-Codes/gdcf-axmw -> export -> shapefile
- outputs: Where I saved the bokeh plots. 

dependencies: 
- listed in datafellow_dependencies.py, added a small note in data.ipynb about how to install them, not sure the level of coding familiarity of the reader. 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

inspiration: https://twitter.com/mattyglesias/status/1778800447140110649 

I find the discourse about cities growing/shrinking to often be confusing. Most cities in america are composed of sections that don't really feel like cities at all. 
In chicago, really only the 2.5 mile radius around the loop and the northside next to the lake "feel" like a city. Both these areas are growing quickly, while the rest of the city shrinks. 
So is the city growing or shrinking? 

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Thanks for reading!