import pandas as pd


class CsvReader():

    def __init__(self, url):
        self.csv_data = []

        self.read_csv(url)

    def read_csv(self, url):
        self.csv_data = pd.read_csv(url).values.tolist()
