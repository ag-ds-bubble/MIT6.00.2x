import random, pylab
import seaborn as sns
import matplotlib.pyplot as plt
plt.style.use('ggplot')

xVals = []
yVals = []
wVals = []
for i in range(1000):
    xVals.append(random.random())
    yVals.append(random.random())
    wVals.append(random.random())
xVals = pylab.array(xVals)
yVals = pylab.array(yVals)
wVals = pylab.array(wVals)
xVals = xVals + xVals
zVals = xVals + yVals
tVals = xVals + yVals + wVals

# # Problem 1&2
# sns.distplot(tVals, label='tVals')
# sns.distplot(xVals, label='xVals')
# plt.legend()
# plt.show()

# Problem 3
pylab.plot(xVals, zVals)
plt.show()

pylab.plot(xVals, yVals)
plt.show()


pylab.plot(xVals, sorted(yVals))
plt.show()


pylab.plot(sorted(xVals), yVals)
plt.show()


pylab.plot(sorted(xVals), sorted(yVals))
plt.show()







