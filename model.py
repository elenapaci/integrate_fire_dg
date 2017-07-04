import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from RasterPlot_color import raster
from Neuron_Synapse import Neuron
from Neuron_Synapse import Synapse
from Perforant_pathway import Perforant_pathway
import pandas 


#parameters

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

electrode_current=0.01

n_pp = 6
n_gc = 2
n_sy=6

#create functions for connectivity and neuron

def connect(pre_neuron,post_neuron,synapses):
    synapses.append(Synapse(e_s, rmg_bars, p, tau_s, s))
    synapse_n=len(synapses)-1

    pre_neuron.add_post(synapse_n)
    post_neuron.add_pre(synapse_n)

def do_neuron(neuron,synapses,spikes,electrode_current):
    voltage=neuron.v
    current=electrode_current
    for pre_s in neuron.pre:
        current+=synapses[pre_s].get_current(voltage)
        
    if(n.update(current)):
        for s in neuron.post:
            spikes.append(s)
            
#create 
  
pp_spikes=[[] for i in range(n_pp)]
pp=[Perforant_pathway(lambd,t_ref,t0) for i in range(n_pp)]
    
gc_spikes=[[] for i in range(n_gc)]
gc=[Neuron(e_l,v_t,v_r,tau_m,v) for i in range(n_gc)]



#connect pp -> gc

connect(pp[0],gc[1],synapses)
connect(pp[1],gc[1],synapses)
connect(pp[1],gc[2],synapses)
connect(pp[2],gc[1],synapses)
connect(pp[2],gc[2],synapses)   
connect(pp[3],gc[2],synapses)
    
#update

while t<t1:
    
    for s in synapses:
        s.update()
        
    spikes=[]

    for p in pp:
        do_neuron(neuron,synapses,spikes,electrode_current)
 
    for g in gc:
        do_neuron(neuron ,synapses,spikes,electrode_current)


    for s in spikes:
        synapses[s].spike()
                
    
    t+=delta_t

spikes=np.concatenate((pp_spikes,gc_spikes))

spikes_color=["g" for i in range(len(pp_spikes))]
for i in range (len(gc_spikes)):
    spikes_color.append("r")
  
 #plot spikes      
fig = plt.figure()
ax = raster(spikes,colors)
plt.title('Example raster plot')
plt.xlabel('time')
plt.ylabel('trial')
fig.show()