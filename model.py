import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from RasterPlot_color import raster
from Neuron_Synapse import Neuron
from Neuron_Synapse import Synapse
from Perforant_pathway import Perforant_pathway
import pandas 

hz=1.
sec=1.
ms=0.001
mV=0.001
 
t0=0*sec
t1=0.5*sec
delta_t=1*ms
t=t0
 
lambd = 5*hz
t_ref=5*ms

v_t=-54*mV
e_l=-70*mV
v_r=-80*mV
tau_m=20*ms
rmIe=18*mV
v=v_t

rmg_bars=0.15
p=0.5
tau_s=10*ms
e_s=0*mV
s=0

v_spike=0.

n_pp = 6
n_gc = 2
n_sy=6

synapses=[[] for i in range(n_sy)]
synapses=[Synapse(e_s,rmg_bars,p,tau_s,s) for i in range(n_sy)]

    
pp_spikes=[[] for i in range(n_pp)]
pp_v=[Perforant_pathway(lambd,t_ref,t0) for i in range(n_pp)]
    
while t<t1:
    for pp_c,pp in enumerate(pp_v):
        if pp.update(t):
            pp_spikes[pp_c].append(t)
    t+=delta_t
    
gc_spikes=[]
gc_v=[Neuron(e_l,v_t,v_r,tau_m,v) for i in range(n_gc)]

while t<t1:
    for gc_c,gc in enumerate(gc_v):
        gc.update(rmIe,delta_t)
        if gc.spike():
                gc_spikes.append(gc.spike)
    t+=delta_t
          
spikes=np.concatenate((pp_spikes,gc_spikes))
spikes_color=["g" for i in range(len(pp_spikes))]
for i in range (len(gc_spikes)):
    spikes_color.append("r")

        
for pp in pp_v:
    if pp.update(t):
        syn_list=pp.post_v
        for syn_i in syn_list:
            synapses[syn_i].spike()
            
synapses.append(synapses(-1))
new_syn_i=len(synapses)-1
pp[0].add_post(new_syn_i)
gc[0].add_pre(new_syn_i)


fig = plt.figure()
ax = raster(spikes,colors)
plt.title('Example raster plot')
plt.xlabel('time')
plt.ylabel('trial')
fig.show()
