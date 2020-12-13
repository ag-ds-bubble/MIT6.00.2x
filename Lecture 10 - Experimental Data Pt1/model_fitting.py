# Imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('ggplot')

# Read the data
springData = pd.read_csv('../Raw Data/springData.txt', sep=' ')
springData['Force'] = springData.Mass*9.8


# Exploring the data and its concurrence to Hookes Law
# F =-kd
def exploreData(data):
    data.copy().set_index('Force').Distance.plot(linestyle='', color='k', marker='o', label='Actual')
    plt.ylabel('Displacement (m)')
    plt.title('Variation of Displacement w.r.t Force')
    

# exploreData(springData)
# plt.show()

def fitData(x, y):
    model = np.polyfit(x,y,1)
    m,c = np.polyfit(x,y,1)
    print(f'Slope = {m}, Intercept = {c}')
    exploreData(springData)
    # predictedD = m*x + c
    predictedD = np.polyval(model, x)
    SSE = sum((predictedD-y)**2)
    print(f'SSE : {SSE}')
    plt.plot(x, predictedD, color='r', label=f'Fitted Values, k={round(1/m, 3)}', linestyle=':', marker='o')

fitData(springData.Force, springData.Distance)
plt.legend()
plt.show()




