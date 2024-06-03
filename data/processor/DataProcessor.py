import pandas as pd
import json


class DataProcessor:
    def __init__(self, csv_file_path, json_file_path):
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path
        self.features = self._load_features_from_json()

    def _load_features_from_json(self):
        with open(self.json_file_path, 'r') as file:
            features = json.load(file)
        return features

    def read_data(self):
        # Read the CSV file
        df = pd.read_csv(self.csv_file_path, usecols=self.features.keys())
        # Rename columns based on the JSON file
        df.rename(columns=self.features, inplace=True)
        return df
