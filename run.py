import numpy as np
import pandas as pd
from bokeh.plotting import figure, output_file, show
from os import path



class nhanes_data:
    def __init__(self, datafile, delimiter):
        self.datafile = datafile
        self.delimiter = delimiter
        self.data = self._load_file()

    def _load_file(self):
        return pd.read_csv(open(self.datafile, "rb"), sep=",", index_col=1)


sections = ["demographic", "diet", "examination", "labs", "medications", "questionnaire"]
data_suffix = "csv"
index_suffix = "idx"
datalist = []


for section in sections:
    datalist.append(nhanes_data(path.join("data/", section + "." + data_suffix), ","))


for data in datalist:
    print(data.data)