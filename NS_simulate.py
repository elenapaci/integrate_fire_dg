import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from Neuron_Synapse import Neuron
from Neuron_Synapse import Synapse


mV=0.001
ms=0.001

v_t=-54*mV
e_l=-70*mV
v_r=-80*mV
tau_m=20*ms
rmIe=18*mV

rmg_bars=0.15
p=0.5
tau_s=10*ms
e_s1=0*mV
e_s2=-80*mV

t_0=0
t_1=1
t=t_0
delta_t=1*ms
v_spike=0.
e_s=e_s2

vs1=[]
vs2=[]
s=0

current_1_v=[]
current_2_v=[]

neuron1=Neuron(e_l,v_t,v_r,tau_m,rnd.uniform(v_r, v_t))
neuron2=Neuron(e_l,v_t,v_r,tau_m,rnd.uniform(v_r, v_t))

synapse1=Synapse(e_s,rmg_bars,p,tau_s,s)
synapse2=Synapse(e_s,rmg_bars,p,tau_s,s)
    
while t<=t_1:
    synapse1.update(delta_t)
    synapse2.update(delta_t)
    neuron1.update(rmIe+synapse2.current(neuron1.v),delta_t)
    neuron2.update(rmIe+synapse1.current(neuron2.v),delta_t)
    current_1_v.append(synapse1.current(neuron2.v))
    current_2_v.append(synapse2.current(neuron1.v))    

    if neuron1.spike():
        synapse1.spike()
        vs1.append(v_spike)
    else:
        vs1.append(neuron1.v)
        
    if neuron2.spike():
        synapse2.spike()
        vs2.append(v_spike)
    else:
        vs2.append(neuron2.v)

    t+=delta_t

fig = plt.figure()
plt.plot(vs1, 'g')
plt.plot(vs2, 'r')
plt.show()

plt.plot(current_1_v, 'g')
plt.plot(current_2_v, 'r')
plt.show()


