import pandas as pd
import json


class DataProcessor(object):
    def __init__(self, json_path, verbose=False):
        self.csv_file_path = "/home/avivwe@mta.ac.il/biobank/ukb672220.csv"
        self.json_file_path = json_path
        self.verbose = verbose
        self.features = self._load_features_from_json()
        self.df = None

    def _load_features_from_json(self):
        """ Loads feature names from a JSON file where each feature has associated metadata. """
        try:
            with open(self.json_file_path, 'r') as file:
                data = json.load(file)
                features = {value['field_id']: key for key, value in data.items()}
                if self.verbose:
                    print(f"Loaded features: {features}")
                return features
        except FileNotFoundError:
            print(f"Error: File not found {self.json_file_path}")
        except json.JSONDecodeError:
            print("Error: JSON file is malformed.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def read_data(self):
        """ Reads data from a CSV file using the predefined features list. """
        if not self.features:
            print("Error: Features not loaded.")
            return
        try:
            if self.verbose:
                print("Reading data...")
                print(f"CSV file path: {self.csv_file_path}")
            # Use the feature keys as column names for reading specific columns
            df = pd.read_csv(self.csv_file_path, usecols=self.features.keys())
            # Rename columns based on the JSON mapping
            df.rename(columns=self.features, inplace=True)
            self.df = df
            return df
        except pd.errors.EmptyDataError:
            print("Error: CSV file is empty.")
        except pd.errors.ParserError:
            print("Error: Error parsing CSV file.")
        except FileNotFoundError:
            print(f"Error: File not found {self.csv_file_path}")
        except KeyError as e:
            print(f"Error: One or more columns not found in the CSV file: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_df(self, path):
        """ Saves the DataFrame to a CSV file at the specified path. """
        if self.df is not None:
            self.df.to_csv(path, index=False)
            if self.verbose:
                print(f"DataFrame saved to {path}")
        else:
            print("Error: No DataFrame to save.")


