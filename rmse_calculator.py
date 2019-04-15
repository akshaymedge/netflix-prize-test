import os
from math import sqrt
# import movie_movie_similarity_calculation as movsc
from sklearn.metrics import mean_squared_error

DATA_PATH = 'C:/Users/amedge/Downloads/netflix-prize-data/{}'

def calculate_rmse(actual_output):
    predictions = []
    if os.path.isfile("Probe_Predictions.txt"):
        with open(DATA_PATH.format("Probe_Predictions.txt")) as probe_pred:
            for line in probe_pred:
                predictions.append(line.split(":")[1])

    return sqrt(mean_squared_error(actual_output, predictions))
