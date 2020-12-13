# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
plt.style.use('ggplot')
# np.random.seed(0)

def get_r2(y,yhat):
    ymean = np.mean(y)
    sse = sum((y-yhat)**2)
    mdeviat = sum((y-ymean)**2)
    r2 = 1-(sse/mdeviat)
    return r2


# Data Read
dataTemp = pd.read_csv('../Raw Data/temperatures.csv')
dataTemp.DATE = pd.to_datetime(dataTemp.DATE, format='%Y%m%d')
dataTemp.set_index('DATE', inplace=True)
dataTemp.index = dataTemp.index.year
dataTemp = dataTemp.groupby(dataTemp.index).TEMP.mean()
# dataTemp.plot(title='Temperature (Agg over country)')
# plt.show()

sampSets = 10
testSize = int(dataTemp.shape[0]*0.2)
modelOrders = (1,2,3)

print('R2 for Testing Data (Random Sampling):')
for eorder in modelOrders:
    order_r2 = []
    # np.random.seed(0)
    for _ in range(sampSets):
        # Split the data
        test_idx  = np.random.choice(list(range(dataTemp.shape[0])), size=testSize)
        # test_idx  = list(range(dataTemp.shape[0]))[-20:]
        train_idx = [k for k in list(range(dataTemp.shape[0])) if k not in test_idx]
        trainData = dataTemp.iloc[train_idx].to_frame().copy()
        testData = dataTemp.iloc[test_idx].to_frame().copy()
        trainData.sort_index(inplace=True)
        testData.sort_index(inplace=True)
        # Fit the model
        model = np.polyfit(trainData.index.values, trainData.TEMP.values, eorder)
        # Make Predictions
        yhat = np.polyval(model, testData.index.values)
        plt.scatter(testData.index, yhat, label=str(eorder))
        _r2 = get_r2(testData.TEMP.values, yhat)
        # Append the r2
        order_r2.append(_r2)

    # Pring the r2 mean and std
    _mean = round(np.mean(order_r2),3)
    _sdev = round(np.std(order_r2),3)
    print(f'\tFor order={eorder}, Mean = {_mean} & Std = {_sdev}')
    
plt.legend()
plt.show()