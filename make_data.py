import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt

def each_3hour(old_data):
    new_data = pd.DataFrame(np.zeros((1461, 1)))

    count = 0
    for i in range(1461):
        for j in range(8):
            for k in range(18):
                new_data.ix[count] = old_data.ix[i, j]
                count += 1
        print(count)

    return new_data


electricity = pd.read_csv("train_kwh.tsv", delimiter="\t")

dataset = pd.DataFrame(electricity.ix[:, "datetime"])
dataset["Year"] = dataset.ix[:, "datetime"]//100000000
dataset["Month"] = (dataset.ix[:, "datetime"]%100000000)//1000000
dataset["Day"] = (dataset.ix[:, "datetime"]%1000000)//10000
dataset["Hour"] = (dataset.ix[:, "datetime"]%10000)//100
dataset["Minute"] = dataset.ix[:, "datetime"]%100
dataset = pd.concat([dataset, electricity.ix[:, 1]], axis=1)

forecast_kanagawa = pd.read_csv("./forecast/forecast/forecast_kanagawa.tsv", "\t")

new_file = each_3hour(forecast_kanagawa.ix[:, 9:17])
new_file.to_csv(time.time())
