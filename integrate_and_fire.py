import matplotlib.pyplot as plt

class Neuron:

    def __init__(self,e_l,v_t,v_r,tau_m):
        self.e_l=e_l
        self.v_t=v_t
        self.v_r=v_r
        self.tau_m=tau_m
        self.v=self.e_l

    def dVdt(self,rmIe):
        return (self.e_l-self.v+rmIe)/self.tau_m

    def update(self,rmIe,delta_t):
        self.v=self.v+self.dVdt(rmIe)*delta_t

    def spike(self):
        if self.v>self.v_t:
            self.v=self.v_r
            return True
        return False


mV=0.001
ms=0.001

v_t=-40*mV
e_l=-70*mV
v_r=-70*mV
tau_m=10*ms

neuron1=Neuron(e_l,v_t,v_r,tau_m)

t_0=0
t_1=1
delta_t=1*ms
rmIe=31*mV
v_spike=0.

t=t_0

vs=[]

while t<=t_1:
    neuron1.update(rmIe,delta_t)
    if neuron1.spike():
        vs.append(v_spike)
    else:
        vs.append(neuron1.v)
    t+=delta_t
    
 


plt.plot(vs)
plt.show()

