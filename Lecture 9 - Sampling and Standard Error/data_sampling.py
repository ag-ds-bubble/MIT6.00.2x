import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../Raw Data/temperatures.csv', parse_dates=True)
data.DATE = pd.to_datetime(data.DATE,format='%Y%m%d')
data.set_index('DATE', inplace=True)


def get_samplemean(sdata, datadesc):
    print('Mean of the Temperature : ', sdata.TEMP.mean())
    print('Std of the Temperature : ', sdata.TEMP.std())

    sdata.TEMP.plot.hist(bins=50, title=datadesc)
    plt.xlabel('Temperature')
    plt.ylabel('Frequency')
    plt.show()


get_samplemean(data, datadesc='All population')
get_samplemean(data.sample(100), datadesc='Sample')