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
from matplotlib.animation import FuncAnimation


# https://medium.com/towards-artificial-intelligence/monte-carlo-simulation-an-in-depth-tutorial-with-python-bcf6eb7856c8
def fairCoinToss():
    return np.random.choice([0,1])

def create_circular_mask(h, w, center=None, radius=None):
    if center is None: # use the middle of the image
        center = (int(w/2), int(h/2))
    if radius is None: # use the smallest distance between the center and image walls
        radius = min(center[0], center[1], w-center[0], h-center[1])

    Y, X = np.ogrid[:h, :w]
    dist_from_center = np.sqrt((X - center[0])**2 + (Y-center[1])**2)

    mask = dist_from_center <= radius
    return mask

# Coin Toss Problem
def p1_main(N):
    def p1(n):
        res = [fairCoinToss() for _ in range(n)]
        heads_prob = sum(res)/n
        return heads_prob

    hprobs = []
    for n in tqdm(range(2,N)):
        hprobs.append(p1(n))
    plt.plot(hprobs, linestyle='-.')
    plt.hlines(0.5, 0, N, color='r')


# Pi Estimation through the area of rectangle and circle
def p2_main(N, grid=1000):

    canvas = np.ones((grid, grid), dtype=np.uint8)
    circular_mask = create_circular_mask(grid, grid)
    temp = canvas.nonzero()
    canvas *= 0
    GRID_POINTS = [(a,b) for a,b in zip(temp[0], temp[1])]
    est = []

    points = N

    while points > 0:
        ridx = np.random.choice(list(range(len(GRID_POINTS))))
        gy,gx = GRID_POINTS[ridx]
        canvas[gy,gx] = 1

        tot_rect = np.sum(canvas)
        tot_circle = np.sum(canvas*circular_mask)
        pi_est = 4 * (tot_circle/tot_rect)
        est.append(pi_est)

        del GRID_POINTS[ridx]
        
        points -= 1
    
    plt.plot(est, linestyle='-.', color='r')
    plt.hlines(np.pi,0,N,color='k', linewidth=3)


# Monty Halls Problem
# ----------------------------------------------------------------------
# Suppose you are on a game show, and you have the choice of picking
# one of three doors: Behind one door is a car; behind the other doors,
# goats. You pick a door, let’s say door 1, and the host, who knows
# what’s behind the doors, opens another door, say door 3, which has
# a goat. The host then asks you: do you want to stick with your choice 
# or choose another door? 

# >>>>>> Is it to your advantage to switch your choice of door?

def p3_main(N=10_000):
    car_pos = np.array([0,0,1])
    picks = np.array([0,1,2])
    stick = 0
    switch = 0

    stick_wining=[]
    switch_wining=[]

    _, pax = plt.subplots(2,1, figsize=(15,12))

    for i in tqdm(range(1,N)):

        # Shuffle the position of a car
        random.shuffle(car_pos)

        # Contestants pick
        pick = random.choice(picks)
        remaining_doors = np.array([k for k in picks if k!=pick])

        # Show 
        show_door = remaining_doors[np.argmax(car_pos[remaining_doors]==0)]
        switch_door = [k for k in remaining_doors if k!=show_door][0]

        # If the participant sticks to the original
        stick += int(car_pos[pick]==1)

        # If the participant switches
        switch += int(car_pos[switch_door]==1)

        stick_wining.append(stick/i)
        switch_wining.append(switch/i)
    
    pax[0].plot(stick_wining, linestyle='-.', color='r')
    pax[0].hlines(1/3,0,N,color='k', linewidth=3)
    pax[0].set_title('If Participant sticks to the original choice,\n probability of winning')

    pax[1].plot(switch_wining, linestyle='-.', color='r')
    pax[1].hlines(2/3,0,N,color='k', linewidth=3)
    pax[1].set_title('If Participant switches from the original choice,\n probability of winning')




class BuffonsNeedle:
    def __init__(self, interline_length = 10, nlines = 10):
            
        # Buffon Needle Experiment
        self.INTERLINE_LENGTH = interline_length
        self.NLINES = nlines
        self.CANVAS_SHAPE = (100 , self.INTERLINE_LENGTH*(self.NLINES+1))
        self.MATCHLEN = self.INTERLINE_LENGTH/2
        self.all_checks = []

    def run_simulation(self, nmatches = 100, print_res = True, return_resp = True):
        all_checks = []
        plotangle = []
        point_pairs = []
        for _ in range(nmatches):
            fallcentre = (np.random.random()*self.CANVAS_SHAPE[0], np.random.random()*self.CANVAS_SHAPE[1])
            fallcentre_nl = np.round(fallcentre,-1)
            fallangle = np.random.random()*0.5*np.pi
            check = abs(fallcentre[-1]-fallcentre_nl[-1]) <= self.MATCHLEN*0.5*np.sin(fallangle)
            all_checks.append(check)
            cosv = np.cos(fallangle+0.5*np.pi*np.random.randint(0,2))
            sinv = np.sin(fallangle+0.5*np.pi*np.random.randint(0,2))
            point_pairs.append((fallcentre[0]-0.5*self.MATCHLEN*cosv, fallcentre[0]+0.5*self.MATCHLEN*cosv))
            point_pairs.append((fallcentre[1]-0.5*self.MATCHLEN*sinv, fallcentre[1]+0.5*self.MATCHLEN*sinv))

        pi_c = np.round(nmatches/sum(all_checks), 3)
        pi = np.pi
        pi_del = np.round(abs(np.round((pi_c-pi)/pi, 5)*100), 2)
        if print_res:
            print(f'With {nmatches}..')
            print(f'\t Simulated value of π : {pi_c}')
            print(f'\t Simulated value of π : {pi_del} %')
        if return_resp:
            return nmatches, pi_c, pi_del, point_pairs

    def animate_sim(self, rangeL=100, rangeU=5_000, skip=100, save = True):
        
        simpiX_data = []
        simpiY_data = []
        floortxt = "Number of Matches : {0}"
        pitext = "Simulated Value of π : {0} @ Deviation : {1} %"
        mnlist = list(range(rangeL, rangeU, skip))
        print(len(mnlist))
        # MATPLOTLIB INITIALIZATION
        bfig, bax = plt.subplots(2,1, gridspec_kw={'height_ratios': [3, 1]}, figsize=(25, 15))
        floortitle = bax[0].set_title(floortxt.format(0), fontsize=25)
        pititle = bax[1].set_title(pitext.format(0,0), fontsize=25)
        bax[0].tick_params(axis='both', which='major', labelsize=20)
        picurve, = bax[1].plot(simpiX_data, simpiY_data, linewidth=3)

        def init():
            bax[1].grid()
            return bfig, floortitle, pititle, picurve,
        
        def animate(i):
            # if i%10==0:
            #     print(i)
            nmatches, pi_c, pi_del, point_pairs = self.run_simulation(mnlist[i], print_res=False)
            bax[0].clear()
            floortitle = bax[0].set_title(floortxt.format(nmatches), fontsize=25)
            bax[0].grid()
            bax[0].hlines(list(range(10,self.INTERLINE_LENGTH*(self.NLINES+1)+10,10)), 0, 100)

            simpiY_data.append(pi_c)
            simpiX_data.append(mnlist[i])

            bax[1].hlines(np.pi, 0, mnlist[i]+100, color='r', linewidth=2)
            bax[1].set_xlim(0, mnlist[i]+100)
            bax[1].set_ylim(min(simpiY_data)*0.95, max(simpiY_data)*1.05)
            
            floortitle.set_text(floortxt.format(nmatches))
            pititle.set_text(pitext.format(pi_c, pi_del))

            picurve.set_data(simpiX_data, simpiY_data)

            bax[0].plot(*point_pairs)

            return bfig, floortitle, pititle, picurve,

        anim = FuncAnimation(bfig, animate, init_func=init,
                                        frames=len(mnlist), interval=1, blit=True)
        anim.save('buffon_needle.gif', writer='pillow', fps=10)



# Coin Toss Problem
plt.figure()
p1_main(10_000)
plt.show()
# Pi Estimation
plt.figure()
p2_main(10_000)
plt.show()
# Buffons Needle Experiment
plt.figure()
p3_main(10_000)
plt.show()

# Buffons Needle Animation
expObj = BuffonsNeedle()
expObj.run_simulation(1_000_000)
expObj.animate_sim()

