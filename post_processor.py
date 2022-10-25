# Date of the first creation: 2022/10/18
# This file is for Energyplus parametric simulation
import pandas as pd
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.pyplot as plt

def plot_1D_results(output_paths, plot_column_name, 
y_axis_title, plot_title):