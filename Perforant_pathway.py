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
            
    def add_post (n) :
        self.post_v.append(n)