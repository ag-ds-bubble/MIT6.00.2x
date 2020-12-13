# Imports
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')

# Read the data
springData = pd.read_csv('../Raw Data/springData.txt', sep=' ')
springData['Force'] = springData.Mass*9.8


# Exploring the data and its concurrence to Hookes Law
# F =-kd
springData.set_index('Force').Distance.plot(linestyle='', color='k', marker='o')
plt.ylabel('Displacement (m)')
plt.title('Variation of Displacement w.r.t Force')
plt.show()