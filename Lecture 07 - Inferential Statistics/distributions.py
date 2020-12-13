import numpy as np
import random
import matplotlib.pyplot as plt
import seaborn as sns
from warnings import filterwarnings
filterwarnings('ignore')

from scipy.integrate import quad

def plot_diff_dist():
    uniform_dist = [random.random() for _ in range(100_000)]
    triand_dist = [random.random()+random.random() for _ in range(100_000)]
    gauss_dist = [random.gauss(mu=0,sigma=.5) for _ in range(100_000)]

    sns.distplot(uniform_dist, label='Uniform')
    sns.distplot(triand_dist, label='Triangular')
    sns.distplot(gauss_dist, label='Gaussian')
    plt.legend()
    plt.show()


def gauss_func(x, mu, sigma):
    f1 = 1/(sigma*np.sqrt(2*np.pi))
    f2 = np.exp(-((x-mu)**2) / (2*(sigma**2)))
    return f1*f2


def checkEmperical(numTrials):
    for t in range(numTrials):
        mu = random.randint(-10,10)
        sigma = random.randint(1,10)
        print(f'For μ = {mu} & σ = {sigma}')
        for numStd in (1,1.96,3):
            area, emp_err = quad(gauss_func, mu-numStd*sigma, mu+numStd*sigma, (mu, sigma))
            print(f'\t for std={numStd}, area under the curve is = {round(area*100,3)}% with {round(emp_err,3)}')


checkEmperical(3)