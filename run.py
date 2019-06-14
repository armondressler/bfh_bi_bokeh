#!/usr/bin/env python3
import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column
from os import path


class NhanesReader:

    def __init__(self, csvfile, delimiter):
        self.csvfile = csvfile
        self.delimiter = delimiter
        self.data = self._load_file()

    def _load_file(self):
        try:
            return pd.read_csv(open(self.csvfile, "rb"), sep=",")
        except FileNotFoundError:
            return None


csv_base_path = "data"
csv_time_ranges = ["2013_2014", "2007_2008"]
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
        print("----------\nshape: {}".format(nhanes_data[timerange][section].data.shape))
        print("summary:\n{}".format(nhanes_data[timerange][section].data.describe()))



timerange_of_interest = "2007_2008"
columns_of_interest = ["DPQ0"+str(count) for count in range(10,61,10)]
for variable in columns_of_interest:
    print("Section {}".format(variable))
    df = nhanes_data[timerange_of_interest]["questionnaire"].data[variable]
    df.dropna(inplace=True)
    for unique_val in sorted(df.unique()):
        print("Counted {} in {} cases.".format(unique_val,len(df.loc[df == unique_val])))
    print()

###### Depression by Age
df_q = nhanes_data["2013_2014"]["questionnaire"].data
df_d = nhanes_data["2013_2014"]["demographic"].data
df = pd.concat([df_q,df_d], axis=1)
df = df[["DMDHRAGE", "DPQ010"]]
df.dropna(inplace=True)
df = df.loc[df["DPQ010"] == 3]

bracketed_list = []
for agebracket in range(20,81,10):
    columns_of_interest = 0
    for index,person in df.iterrows():
        bracketed_list.append(person["DMDHRAGE"])

hist, bins = np.histogram(bracketed_list, bins = [20,30,40,50,60,70,80])
plot1 = figure(title="Depression Symptoms by Age (DPQ010)", tools='')
plot1.quad(top=hist, bottom=0, left=bins[:-1], right=bins[1:],line_width=0.8)

###### Depression by GENDER
df_q = nhanes_data["2013_2014"]["questionnaire"].data
df_d = nhanes_data["2013_2014"]["demographic"].data
df = pd.concat([df_q,df_d], axis=1)
df = df[["RIAGENDR", "DPQ090"]]
df.dropna(inplace=True)
df = df.loc[df["DPQ090"] == 3]

bracketed_list = []
for index, person in df.iterrows():
    bracketed_list.append(person["RIAGENDR"])

hist, bins = np.histogram(bracketed_list)
plot2 = figure(title="Depression Symptoms by Gender (DPQ090)", tools='')
plot2.quad(top=hist, bottom=0, left=bins[:-1], right=bins[1:])




bokeh_column = column(plot1,plot2)

show(bokeh_column)








