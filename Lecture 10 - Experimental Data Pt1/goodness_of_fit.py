# R2
# Imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
plt.style.use('ggplot')

# Reading the simdata
simdata = pd.read_csv('../Raw Data/fitdata.csv', index_col=0)

def get_r2(y,yhat):
    ymean = np.mean(y)
    sse = sum((y-yhat)**2)
    mdeviat = sum((y-ymean)**2)
    r2 = 1-(sse/mdeviat)
    return r2

def fit_data(x, y, polyorder):

    model = np.polyfit(x,y,polyorder)
    predictions = np.polyval(model, x)
    _SSE = sum((predictions-y)**2)
    _R2 = get_r2(y, predictions)
    print(f'SSE : {round(_SSE, 3)}; R2 : {round(_R2, 3)}')
    plt.plot(x, predictions, label=f'Poly Fit of {polyorder}, R2={_R2}', linestyle=':')
    
plt.plot(simdata.index.values, simdata.data.values, color='darkgray',  linestyle='', marker='o')
fit_data(simdata.index.values, simdata.data.values, 1)
fit_data(simdata.index.values, simdata.data.values, 2)
fit_data(simdata.index.values, simdata.data.values, 4)
fit_data(simdata.index.values, simdata.data.values, 6)
fit_data(simdata.index.values, simdata.data.values, 12)
fit_data(simdata.index.values, simdata.data.values, 16)
fit_data(simdata.index.values, simdata.data.values, 18)

plt.legend()
plt.show()