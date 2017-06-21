import matplotlib.pyplot as plt
import numpy as np
import random as rnd

class Neuron:

    def __init__(self,e_l,v_t,v_r,tau_m,v):
        self.e_l=e_l
        self.v_t=v_t
        self.v_r=v_r
        self.tau_m=tau_m
        self.spike_number=0
        self.v=v

    def dVdt(self,rmIe):
        return (self.e_l-self.v+rmIe)/self.tau_m

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
        
    def add_post (n) :
        self.post_v.append(n)
        
    def add_pre(n):
        self.pre_v.append(n)

class Synapse:
    
    def __init__(self, e_s, rmg_bars, p, tau_s,s):
        self.e_s=e_s
        self.rmg_bars=rmg_bars
        self.s=s
        self.p=p
        self.tau_s=tau_s
    
    def update(self, delta_t):
        self.s-=(self.s*delta_t)/self.tau_s

    def spike(self):
        self.s+=1.

    def current (self, v):
        return self.rmg_bars*self.p*self.s*(self.e_s-v)

    def g (self, s):
        return self.g_bars*self.s
        