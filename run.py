#!/usr/bin/env python3
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from os import path


class NhanesReader:

    def __init__(self, csvfile, delimiter):
        self.csvfile = csvfile
        self.delimiter = delimiter
        self.data = self._load_file()

    def _load_file(self):
        try:
            return pd.read_csv(open(self.csvfile, "rb"), sep=",", index_col=1)
        except FileNotFoundError:
            return None


csv_base_path = "data"
csv_time_ranges = ["2013_2014","2007_2008"]
sections = ["demographic", "diet", "examination", "labs", "medications", "questionnaire"]
data_suffix = "csv"
index_suffix = "idx"

nhanes_data = {key: {} for key in csv_time_ranges}
for timerange in csv_time_ranges:
    nhanes_data[timerange] = {key: {} for key in sections}

for timerange in nhanes_data.keys():
    for section in nhanes_data[timerange].keys():
        dataframe = NhanesReader(path.join(csv_base_path, timerange, section + "." + data_suffix), ",")
        dataframe.data.set_index("SEQN")
        nhanes_data[timerange][section] = dataframe


for timerange in nhanes_data.keys():
    print("Using timerange {}".format(timerange))
    for section in nhanes_data[timerange].keys():
        print(nhanes_data[timerange][section].data.shape)
