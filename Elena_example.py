

class Neuron:

    def __init__(self):
        self.pre=[]
        self.post=[]
        self.voltage=0
        
    def add_pre(self,pre_n):
        self.pre.append(pre_n)
            
    def add_post(self,post_n):
        self.post.append(post_n)

    def update(self,current):
        self.voltage+=current
        if self.voltage>5:
            self.voltage=0
            return True
        return False

class Synapse:

    def __init__(self):
        self.cond=0


    def spike(self):
        self.cond+=1

    def update(self):
        self.cond*=1

    def get_current(self,voltage):
        return self.cond*voltage


def connect(pre_neuron,post_neuron,synapses):
    synapses.append(Synapse())
    synapse_n=len(synapses)-1

    pre_neuron.add_post(synapse_n)
    post_neuron.add_pre(synapse_n)

def do_neuron(neuron,synapses,spikes,electrode_current):
    voltage=neuron.voltage
    current=electrode_current
    for pre_s in neuron.pre:
        current+=synapses[pre_s].get_current(voltage)
        
    if(n.update(current)):
        for s in neuron.post:
            spikes.append(s)


ms=0.001

synapses=[]

gcs=[]
bcs=[]

electrode_current=0.01

for i in range(0,4):
    gcs.append(Neuron())

for i in range(0,2):
    bcs.append(Neuron())

gcs[1].voltage=2

#connect bc0 -> gc1

connect(bcs[0],gcs[1],synapses)
connect(bcs[0],gcs[2],synapses)
connect(bcs[1],gcs[1],synapses)

t0=0
t1=2
delta_t=1*ms
t=t0

while t<t1:
    
    print t,bcs[0].voltage,gcs[1].voltage,synapses[0].get_current(1)

    for s in synapses:
        s.update()

    spikes=[]

    for n in bcs:
        do_neuron(n,synapses,spikes,electrode_current)
 
    for n in gcs:
        do_neuron(n,synapses,spikes,electrode_current)


    for s in spikes:
        synapses[s].spike()

    t+=delta_t


