import plotly.figure_factory as ff
import statistics as st
import random
import pandas as pd
import csv

df = pd.read_csv("G:\Whitehat Junior\Python Projects\Whitehat jr Projects\Whitehat Jr Projects\medium_data.csv")

data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["reading_time"])

fig.show()



print("population mean:- ",st.mean(data))
def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = st.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_set_of_mean(10)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    print("sampling mean:- ", st.mean(mean_list))
setup()