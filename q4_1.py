import matplotlib.pyplot as plt
import numpy as np

class Neuron:

    def __init__(self,e_l,v_t,v_r,tau_m):
        self.e_l=e_l
        self.v_t=v_t
        self.v_r=v_r
        self.tau_m=tau_m
        self.v=self.e_l
        self.spike_number=0

    def dVdt(self,rmIe):
        return (self.e_l - self.v + rmIe) / self.tau_m

    def update(self,rmIe,delta_t):
        self.v=self.v+self.dVdt(rmIe)*delta_t

    def spike(self):
        if self.v>self.v_t:
            self.v=self.v_r
            self.spike_number+=1
            return True
        return False

    def reset(self):
        self.v=self.e_l
        self.spike_number=0



mV=0.001
ms=0.001

v_t=-55*mV
e_l=-70*mV
v_r=-70*mV
tau_m=10*ms
delta_t=0.025*ms
v=e_l

t0=0
t1=10.

rmIe0=10*mV
rmIe1=50*mV
delta_rmIe=0.1*mV

neuron1=Neuron(e_l,v_t,v_r,tau_m)

input_currents = []
firing_rates = []

rmIe=rmIe0
while rmIe<=rmIe1:
    input_currents.append(rmIe)
    neuron1.reset()
    t=t0
    while t<t1:
        neuron1.update(rmIe,delta_t)
        neuron1.spike()
        t+=delta_t
    firing_rates.append(neuron1.spike_number/(t1-t0))
    rmIe+=delta_rmIe
    
plt.xlabel("rmIe")
plt.ylabel("f")
plt.plot(input_currents, firing_rates)
plt.show()


