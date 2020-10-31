import random
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import pandas as pd
import numpy as np
import seaborn as sns


def rollUnfairDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll<=50:
        return False
    elif 50<roll<100:
        return True

def rollFairDice():
    roll = random.randint(1,100)
    if roll == 100:
        return False
    elif roll<50:
        return False
    elif 50<=roll<100:
        return True


# Strategies
def simple_bettor(funds, initial_wager, wager_count, pltax = None, multiple=None, increment=None):
    value = funds
    wager = initial_wager
    curr_wager = 1

    pltax.grid('both')
    pltax.set_xlabel('Wager Count')
    pltax.set_ylabel('Account Value')

    wX = []
    vY = []
    while curr_wager <= wager_count:
        if rollUnfairDice():
            value += wager
        else:
            value -= wager

        wX.append(curr_wager)
        vY.append(value)
        
        curr_wager += 1

        if value < 0:
            break
    pltax.plot(wX, vY, linewidth = 0.5)
    return value

def martingale_bettor(funds, initial_wager, wager_count, pltax=None, multiple=2, increment=None):
    value = funds
    wager = initial_wager

    if pltax:
        pltax.grid('both')
        pltax.set_xlabel('Wager Count')
        pltax.set_ylabel('Account Value')

    wX = []
    vY = []

    curr_wager = 1
    prev_wager = 'win'
    prev_wager_amt = wager

    while curr_wager <= wager_count:
        if prev_wager == 'win':
            if rollUnfairDice():
                value+=wager
                prev_wager='win'
            else:
                value-=wager
                prev_wager='loss'
                
        elif prev_wager == 'loss':
            wager = prev_wager_amt*multiple
            if wager > value:
                wager = value
            if rollUnfairDice():
                value+=wager
                wager = initial_wager
                prev_wager = 'win'
            else:
                value-=wager
                prev_wager='loss'
        
        prev_wager_amt = wager
        wX.append(curr_wager)
        vY.append(value)
        curr_wager += 1

        if value <= 0:
            break
        
    if pltax:
        pltax.plot(wX, vY, linewidth = 0.5, linestyle='-.') #, marker='o', markersize=1,
    return value

def dAlembert_bettor(funds, initial_wager, wager_count, pltax=None, multiple = None, increment=None):
    value = funds
    wager = initial_wager
    if increment == None:
        increment = initial_wager

    if pltax:
        pltax.grid('both')
        pltax.set_xlabel('Wager Count')
        pltax.set_ylabel('Account Value')

    wX = []
    vY = []

    curr_wager = 1
    prev_wager = 'win'
    prev_wager_amt = wager

    while curr_wager <= wager_count:
        if prev_wager == 'win':
            if abs(wager - increment) >= initial_wager :
                wager -= increment
            else:
                wager = initial_wager

            if rollFairDice():
                value += wager
                prev_wager='win'
            else:
                value -= wager
                prev_wager='loss'
                
        elif prev_wager == 'loss':
            wager = prev_wager_amt+increment
            if wager>value:
                wager=value
            if rollFairDice():
                value+=wager
                wager = initial_wager
                prev_wager = 'win'
            else:
                value-=wager
                prev_wager='loss'
        
        prev_wager_amt = wager
        wX.append(curr_wager)
        vY.append(value)
        curr_wager += 1

        if value <= 0:
            break
        
    if pltax:
        pltax.plot(wX, vY, linewidth = 0.5, linestyle='-.') #, marker='o', markersize=1,
    return value

def labouchere_bettor(funds, initial_wager, wager_count, pltax=None, multiple = None, increment=None, wage_system=[10, 10, 20]):
    
    system = list(np.array(wage_system)*10)
    goal = sum(wage_system)
    not_broke = True
    value = funds
    wager_count = 1

    if pltax:
        pltax.grid('both')
        pltax.set_xlabel('Wager Count')
        pltax.set_ylabel('Account Value')

    wX = []
    vY = []

    while value-funds<goal and not_broke:
        if len(system)==1:
            system = [system[0]/2, system[0]/2]
        wager = system[0]+system[-1]
        if rollFairDice():
            # Won the bet
            value += wager
            del system[0]
            del system[-1]
        else:
            # Lost the bet
            value -= wager
            system.append(wager)

        if value<=0:
            not_broke=False

        wager_count+=1
        wX.append(wager_count)
        vY.append(value)

    if pltax:
        pltax.plot(wX, vY, linewidth = 0.5, linestyle='-.')
    return value


def run_waging_strategies(STRAT_FUNC, STARTING_FUND = 10_000, WAGER_PCT = 0.01, NUMBER_OF_WAGERS = 1000, NUM_EXPERIMENTS=1000, **kwargs):
    
    WAGER_SIZE = STARTING_FUND*WAGER_PCT
    # Plotting
    _, sax = plt.subplots(len(STRAT_FUNC), 1)
    if type(sax).__name__ == 'AxesSubplot':
        sax = [sax]

    for strat_idx, sfunc in enumerate(STRAT_FUNC):
        xx = 0
        broke_count = 0
        profit_count = 0
        loss_count = 0
        while xx < NUM_EXPERIMENTS:
            final_value = sfunc(STARTING_FUND, WAGER_SIZE, NUMBER_OF_WAGERS, sax[strat_idx], **kwargs)
            if final_value<=0:
                broke_count += 1
            elif final_value<=STARTING_FUND:
                loss_count += 1
            elif final_value>STARTING_FUND:
                profit_count += 1
            xx+=1
        
        broke_rate = (broke_count/NUM_EXPERIMENTS)*100
        loss_rate = (loss_count/NUM_EXPERIMENTS)*100
        profit_rate = (profit_count/NUM_EXPERIMENTS)*100

        fname = sfunc.__name__
        fname = " ".join(fname.split('_')).upper()
        print(f'{fname} STRATEGY : Broke Rate : {broke_rate} %')
        print(f'{fname} STRATEGY : Loss Rate : {loss_rate} %')
        print(f'{fname} STRATEGY : Profit Rate : {profit_rate} %\n')

# run_waging_strategies([labouchere_bettor], 
#                       increment = 100, multiple=1.7391,
#                       STARTING_FUND = 10000, WAGER_PCT = 0.01,
#                       NUMBER_OF_WAGERS = 100, NUM_EXPERIMENTS=100)
# plt.show()


def optimize_martingale(STARTING_FUND = 10_000, WAGER_PCT = 0.01, NUMBER_OF_WAGERS = 100, NUM_EXPERIMENTS=100_000):
    """
    1) Multiplier of 1.7391 was the most efficient with Profit Rate @ 71.005% and Broke Rate : 16.863%, Loss Rate : 12.132%
    """
    broke_ulimit = 32.235
    profit_llimit = 63.208
    WAGER_SIZE = STARTING_FUND*WAGER_PCT

    while True:
        random_multiple = random.uniform(1, 2)
        xx = 0
        broke_count = 0
        profit_count = 0
        loss_count = 0

        while xx < NUM_EXPERIMENTS:
            final_value = martingale_bettor(STARTING_FUND, WAGER_SIZE, NUMBER_OF_WAGERS, multiple=random_multiple)
            print(final_value)
            if final_value<=0:
                broke_count += 1
            elif final_value<=STARTING_FUND:
                loss_count += 1
            elif final_value>STARTING_FUND:
                profit_count += 1
            xx+=1
        broke_rate = (broke_count/NUM_EXPERIMENTS)*100
        loss_rate = (loss_count/NUM_EXPERIMENTS)*100
        profit_rate = (profit_count/NUM_EXPERIMENTS)*100
        
        
        if broke_rate < broke_ulimit and profit_rate > profit_llimit:
            print(f'For {random_multiple} as multiplier')
            print(f'\t MARTINGALE STRATEGY : Broke Rate : {broke_rate} %')
            print(f'\t MARTINGALE STRATEGY : Loss Rate : {loss_rate} %')
            print(f'\t MARTINGALE STRATEGY : Profit Rate : {profit_rate} %\n')

def optimize_dalembert(STARTING_FUND = 10_000, NUM_EXPERIMENTS=100_0):
    """
    Optimize the WAGEr_PCT and NUMBER_OF_WAGERS.
    1) Wager Pct : , NWagers  and Increment : 
       the most efficient with Profit Rate @ % and Broke Rate : %, Loss Rate : %
    """
    metricDF = pd.read_csv('results/dalmbert_optmdf.csv', index_col=0)
    broke_ulimit = 100
    profit_llimit = 0
    idx = metricDF.shape[0]

    while True:
        random_wpct = random.uniform(0.01, 0.02)
        random_nwagers = int(random.uniform(100, 200))
        random_incr = int(random.uniform(100, 150))

        xx = 0
        broke_count = 0
        profit_count = 0
        loss_count = 0
        random_wagersize = STARTING_FUND*random_wpct

        while xx < NUM_EXPERIMENTS:
            final_value = dAlembert_bettor(STARTING_FUND, random_wagersize, random_nwagers, increment=random_incr)
            if final_value<=0:
                broke_count += 1
            elif final_value<=STARTING_FUND:
                loss_count += 1
            elif final_value>STARTING_FUND:
                profit_count += 1
            xx+=1
        
        broke_rate = (broke_count/NUM_EXPERIMENTS)*100
        loss_rate = (loss_count/NUM_EXPERIMENTS)*100
        profit_rate = (profit_count/NUM_EXPERIMENTS)*100
        
        metricDF.loc[idx, 'wager_pct'] = random_wpct
        metricDF.loc[idx, 'wager_count'] = random_nwagers
        metricDF.loc[idx, 'wager_increments'] = random_incr
        metricDF.loc[idx, 'profit_rate'] = profit_rate
        metricDF.loc[idx, 'loss_rate'] = loss_rate
        metricDF.loc[idx, 'broke_rate'] = broke_rate
        
        metricDF.to_csv('results/dalmbert_optmdf.csv')
        
        if broke_rate < broke_ulimit and profit_rate > profit_llimit:
            broke_ulimit = broke_rate
            profit_llimit = profit_rate
            print(f'For Wager Pct : {random_wpct}, NWagers {random_nwagers} and Increment : {random_incr} as multiplier')
            print(f'\t MARTINGALE STRATEGY : Broke Rate : {broke_rate} %')
            print(f'\t MARTINGALE STRATEGY : Loss Rate : {loss_rate} %')
            print(f'\t MARTINGALE STRATEGY : Profit Rate : {profit_rate} %\n')
        idx+=1


# optimize_dalembert()
# optimize_martingale()

metricDF = pd.read_csv('results/dalmbert_optmdf.csv', index_col=0)
metricDF['combined_metric'] = metricDF['profit_rate']/(metricDF['loss_rate']+metricDF['broke_rate'])
metricDF.sort_values('combined_metric', ascending=False, inplace=True)
metricDF = metricDF.head(200)

sns.distplot(metricDF['wager_pct'])
plt.show()



