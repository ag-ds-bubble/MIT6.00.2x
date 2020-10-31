import scipy.stats as st
import pandas as pd
import warnings
warnings.filterwarnings('ignore')
import time
import scipy
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
import inspect


DISTRIBUTIONS = ['alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 'burr',
                 'cauchy', 'chi', 'chi2', 'cosine', 'dgamma', 'dweibull', 'erlang', 'expon',
                 'exponnorm', 'exponweib', 'exponpow', 'f', 'fatiguelife', 'fisk', 'foldcauchy',
                 'foldnorm', 'frechet_r', 'frechet_l', 'genlogistic', 'genpareto', 'gennorm',
                 'genexpon', 'genextreme', 'gamma', 'gengamma', 'genhalflogistic', 
                 'gilbrat', 'gompertz', 'gumbel_r', 'gumbel_l', 'halfcauchy', 'halflogistic',
                 'halfnorm', 'halfgennorm', 'hypsecant', 'invgamma', 'invgauss', 'invweibull',
                 'johnsonsb', 'johnsonsu', 'ksone', 'kstwobign', 'laplace', 'levy', 'levy_l',
                 'logistic', 'loggamma', 'loglaplace', 'lognorm', 'lomax', 'maxwell', 'mielke',
                 'nakagami', 'norm', 'pareto', 'pearson3','bernoulli',
                 'powerlaw', 'powerlognorm', 'powernorm', 'rdist', 'reciprocal', 'rayleigh', 'rice',
                 'recipinvgauss', 'semicircular', 't', 'triang', 'truncexpon', 'truncnorm',
                 'uniform', 'vonmises', 'vonmises_line', 'wald', 'weibull_min', 'weibull_max', 'wrapcauchy'] # 'gausshyper', 'tukeylambda', 'ncx2', 'ncf', 'nct', 


class MonteCarloSimulation:

    def __init__(self, calc_func:callable, data:pd.DataFrame=None,  distributions:[str,dict]='auto'):
        """
        Monte Carlo Simulation with the data w.r.t to the formulae

        arguments
        -----------------------------------------------------
            data (pd.DataFrame):
                Data corresponsing to the variables in the formulae

            formulae (str):
                Formulae to the calculation of the target variable

            distributions (str, optional): Defaults to 'auto'.
                Distributions corresponding to each of the variables
                to sample from. When 'auto', the distribution is calculated automatically.

                distributions : {'var_x' : 
                                    {'dist_name' : 'gauss',
                                     'dist_params' : {'std':0.5, 'mean' : 1}
                                     },
                                    ....
                                    }
        """
        self.data = data
        self.calc_func = calc_func
        self.distribution = distributions
        self.variables = None
        self.simDF = pd.DataFrame()
        self.sanity_checks_DUpdate()

    def sanity_checks_DUpdate(self):

        dist_check = isinstance(self.distribution, str) or isinstance(self.distribution, dict)
        data_check = isinstance(self.data, pd.DataFrame) or self.data==None

        if not data_check:
            raise ValueError("'data' should only of type 'pd.DataFrame'")
        if not (dist_check or data_check):
            raise ValueError("Either one of the 'data' or 'distribution' should be provided")
        if not callable(self.calc_func):
            raise ValueError("'calc_func' should be a 'callable'")

        self.variables = inspect.getargspec(self.calc_func)[0]

        if isinstance(self.distribution, dict):
            # Check if the dictionary has the value is one of [dict] or [callable]
            check1 = all(isinstance(v, dict) for k,v in self.distribution.items())
            check2 = all(callable(v) for k,v in self.distribution.items())

            if check1 or check2:
                if check1:
                    # Check for the parameters in the distribution
                    for var, var_dict in self.distribution.items():
                        if not ('dist_name' in var_dict):
                            raise ValueError("'dist_name' should be in the parameters.")
                        if var_dict['dist_name'] not in DISTRIBUTIONS:
                            raise ValueError(f"{var} x {var_dict['dist_name']}, {var_dict['dist_name']} is not one of the available..")
                        dist = getattr(st, var_dict['dist_name'])
                        dist_kwargs = var_dict.copy(); del dist_kwargs['dist_name']
                        dist = dist(**dist_kwargs)
                        self.distribution[var] = dist
                # elif check2:
            else:
                raise ValueError("The type of value in key:value of distribution should be one of ['dict','function']")

        elif isinstance(self.distribution, str) and self.distribution == 'auto' and data_check:
            self.distribution = {}
            # Find the best probability distribution fit for the variables
            if not all([k in self.data.columns.tolist() for k in self.variables]):
                missing_cols = [k for k in self.variables if k not in self.data.columns.tolist()]
                raise ValueError(f"'data' doesnt contain {missing_cols} which are there in the 'formulae'")
            
            for evar in self.variables:
                data_vals = self.data[evar].values
                data_valsN = len(data_vals)
                max_pvalue = 0
                max_pvalue_dist, max_pvalue_distname = None, None

                for each_distname in DISTRIBUTIONS:
                    check_dist = getattr(st, each_distname)
                    try:
                        check_distparams = check_dist.fit(data_vals)
                        ## Check for the AIC values
                        # k = len(check_distparams)
                        # logLik = np.sum(check_dist.logpdf(data_vals, *check_distparams))
                        # aic = 2*k - 2*(logLik)
                        D, pvalue = st.ks_1samp(data_vals, check_dist.cdf, args=check_distparams)
                        if pvalue > max_pvalue and pvalue>=0:
                            max_pvalue = pvalue
                            max_pvalue_dist = check_dist(*check_distparams)
                            max_pvalue_distname = each_distname
                    except:
                        pass
                self.distribution[evar] = max_pvalue_dist
        
    def run_simulation(self, iterations=100, samplesize=10_000, no_sampling=False):

        if no_sampling:
            for e_iter in tqdm(range(1,iterations)):
                dist_vals = {k:v.rvs(e_iter) for k,v in self.distribution.items()}
                self.simDF = self.simDF.append(self.calc_func(**dist_vals), ignore_index=True)
        else:
            for _ in tqdm(range(1,iterations)):
                dist_vals = {k:v.rvs(samplesize) for k,v in self.distribution.items()}
                self.simDF = self.simDF.append(self.calc_func(**dist_vals), ignore_index=True)

    def plot_results(self):
        pass


commDF = pd.DataFrame(columns=['SalesTarget', 'ActualSales','PercentToPlan','CommisionRate','CommisionAmount'])

ndist = st.norm(loc=1_75_000, scale=20_000)
ldist = st.lognorm(s=1.05, loc=70)
ldist1 = st.lognorm(s=0.5, loc=3, scale=.7)

commDF['SalesTarget'] = ndist.rvs(size=1_00_000)
commDF['PercentToPlan'] = ldist.rvs(size=1_00_000).round(2)
commDF['ActualSales'] = (commDF['SalesTarget'] * commDF['PercentToPlan'])/100
commDF['CommisionRate'] = ldist1.rvs(size=1_00_000).round(2)
commDF['CommisionAmount'] = (commDF['ActualSales'] * commDF['CommisionRate'])/100

_dist = {'SalesTarget' : {'dist_name' : 'norm',
                          'loc' : 1_75_000,
                          'scale' : 20_000},

         'PercentToPlan' : {'dist_name' : 'lognorm',
                            's' : 1.05,
                            'loc' : 70},

         'CommisionRate' : {'dist_name' : 'lognorm',
                            's' : 0.5,
                            'loc' : 3,
                            'scale' : 0.7}
         }

# def calcF(SalesTarget, PercentToPlan, CommisionRate):
#     return {'Total_Commision_Amt':sum(SalesTarget*PercentToPlan*CommisionRate*1e-4)}

# mc_sim = MonteCarloSimulation(calc_func=calcF, distributions=_dist, data=None)
# mc_sim.run_simulation(iterations=100)


