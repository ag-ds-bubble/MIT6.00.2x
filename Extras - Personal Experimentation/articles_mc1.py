# Imports
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from scipy.stats import norm
import random
import seaborn as sns
from tqdm import tqdm
style.use('ggplot')


# Reading the Data
data_path = '../raw_data/banknifty_ohlcv.csv'
data = pd.read_csv(data_path, index_col=0)
data.Date = pd.to_datetime(data.Date)
data.set_index('Date', inplace=True)
data_close = data[['Close']].copy()
data_dates = data.index.tolist()

pred_data = data_close.copy()
pred_data['Close_S1'] = pred_data.Close.shift(1)

# ARTICLE : https://www.quantnews.com/introduction-monte-carlo-simulation/#_edn1
NUM_EXPERIMENTS = 10
for i, eidx in enumerate(data_dates[2:]):
    _data = data_close.loc[:eidx-pd.DateOffset(days=1)].copy()
    log_returns = np.log(1+_data.pct_change())
    pred_data.loc[eidx, 'lr_mean'] = log_returns.mean().values[0]
    pred_data.loc[eidx, 'lr_std'] = log_returns.std().values[0]
    pred_data.loc[eidx, 'lr_var'] = log_returns.var().values[0]

pred_data['drift'] = pred_data.apply(lambda x : x.lr_mean-0.5*x.lr_var, axis=1)
for i in tqdm(range(NUM_EXPERIMENTS)):
    vol = pred_data['lr_std']*norm.ppf(np.random.random(pred_data.shape[0]))
    r = np.exp(pred_data['drift'].values+vol)
    pred_price = pred_data['Close_S1']*r
    plt.plot(pred_price.values, linestyle='-.')

plt.show()
