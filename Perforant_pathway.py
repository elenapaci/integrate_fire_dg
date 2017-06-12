import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from RasterPlot import raster

class Perforant_pathway:

    def __init__ (self, lambd, t_ref,t0):
        self.lambd=lambd
        self.t_ref=t_ref
        self.t=t0+self.t_ref+rnd.expovariate(self.lambd)

    def update(self, t):
        if t>self.t:
            self.t = t+self.t_ref+rnd.expovariate(self.lambd)
            return True
        else:
            return False

hz=1.
sec=1.
ms=0.001
 
t0=0*sec
t1=0.5*sec
delta_t=1*ms
 
lambd = 5*hz
t_ref=5*ms

n_pp=50



pp_spikes=[[] for i in range(n_pp)]

pp_v=[Perforant_pathway(lambd,t_ref,t0) for i in range(n_pp)]
    
t=t0
while t<t1:
    for pp_c,pp in enumerate(pp_v):
        if pp.update(t):
            pp_spikes[pp_c].append(t)
    t+=delta_t

 
fig = plt.figure()
ax = raster(pp_spikes)
plt.title('Perforant pathway')
plt.xlabel('time')
plt.ylabel('pp')
fig.show()