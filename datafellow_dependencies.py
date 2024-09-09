#data
from census import Census
from us import states
from pyzipcode import ZipCodeDatabase

#generic plotting
from matplotlib import pyplot as plt

#standard
import pandas as pd
import geopandas as gpd
import numpy as np

#bokeh
from bokeh.transform import linear_cmap
from bokeh.palettes import Blues6, Reds6 
from bokeh.palettes import RdYlBu11 as palette
from bokeh.io import output_notebook, show, curdoc, output_file
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, HoverTool
from bokeh.plotting import figure, save, show, output_notebook
from bokeh.layouts import layout


# !pip/conda install bokeh pandas geopandas pyzipcode matplotlib numpy census us