# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random
plt.style.use('ggplot')

# Data Generation
def genData(a,b,c,size):
    x = np.linspace(-int(size/2), int(size/2), size)
    y = a*x**2 + b*x**1 + c
    y += np.random.randint(0,350, size=len(y))
    return x, y

def getDataPlot(x,y,legend):
    plt.scatter(x,y, edgecolors='k', label=legend)

def exploreData(dataX1, dataY1, dataX2, dataY2):
    getDataPlot(dataX1, dataY1, 'Dataset1')
    getDataPlot(dataX2, dataY2, 'Dataset2')
    plt.legend()

def get_r2(y,yhat):
    ymean = np.mean(y)
    sse = sum((y-yhat)**2)
    mdeviat = sum((y-ymean)**2)
    r2 = 1-(sse/mdeviat)
    return r2


# Fitting Model
def modelFit(x,y,orders,name='Dataset1'):
    print(f'\nFor Model {name}')
    models = []
    for eorder in orders:
        model = np.polyfit(x,y,eorder)
        predictions = np.polyval(model, x)
        _SSE = sum((predictions-y)**2)
        _R2 = get_r2(y, predictions)
        print(f'\tPoly Order @ {eorder} SSE : {round(_SSE, 3)}; R2 : {round(_R2, 3)}')
        plt.plot(x, predictions, label=f'Poly Fit of {eorder}, R2={round(_R2, 2)}', linestyle='-.')
        models.append(model)
    return models

# Tests Models
def modelTest(models,orders,x,y,train_name='Dataset1',test_name='Dataset2'):
    print(f'\n Training on {train_name}, testing on {test_name}')
    for emodel, eorder in zip(models, orders):
        predictions = np.polyval(emodel, x)
        _SSE = sum((predictions-y)**2)
        _R2 = get_r2(y, predictions)
        print(f'\tPoly Fit of {eorder}, SSE : {round(_SSE, 3)}; R2 : {round(_R2, 3)}')
        plt.plot(x, predictions, label=f'Poly Fit of {eorder}, R2={round(_R2, 2)}', linestyle='-.')


dataX1, dataY1 = genData(1,2,-100, 50)
dataX2, dataY2 = genData(1,2,-100, 50)

# Exploring the datasets
exploreData(dataX1, dataY1, dataX2, dataY2)
model_orders = (2,6,12,16)

# Fitting Model
getDataPlot(dataX1, dataY1, 'Dataset1')
modelsD1 = modelFit(dataX1, dataY1, model_orders)
plt.legend()
plt.show()

# Cross Validation
getDataPlot(dataX2, dataY2, 'Dataset1')
modelsD2 = modelFit(dataX2, dataY2, model_orders)
plt.legend()
plt.show()

print('\n\n\n\n\n')
modelTest(modelsD2, model_orders, dataX1, dataY1, train_name='Dataset2', test_name='Dataset1')
modelTest(modelsD1, model_orders, dataX2, dataY2, train_name='Dataset1', test_name='Dataset2')


