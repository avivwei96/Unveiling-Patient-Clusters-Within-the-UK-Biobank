from data.processor.DataProcessor import DataProcessor

semi_path = "/home/avivwe@mta.ac.il/"

data_loader = DataProcessor(semi_path + "blood_biochemistry_features.json", verbose=True)
data_loader.read_data()
data_loader.save_df(semi_path + "blood_biochemistry_features.csv")
