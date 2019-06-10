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
        return pd.read_csv(open(self.csvfile, "rb"), sep=",", index_col=1)


sections = ["demographic", "diet", "examination", "labs", "medications", "questionnaire"]
csv_path = "data/2013_2014"
data_suffix = "csv"
index_suffix = "idx"
nhanes_data = {key: {} for key in sections}


for section in sections:
    dataframe = NhanesReader(path.join(csv_path, section + "." + data_suffix), ",")
    dataframe.data.set_index("SEQN")
    nhanes_data[section] = (dataframe)


for data in nhanes_data.values():
    print(data.data.shape)
