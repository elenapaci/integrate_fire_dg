#from https://scimusing.wordpress.com/2013/05/06/making-raster-plots-in-python-with-matplotlib/
#01.06.2017

import numpy as np
import matplotlib.pyplot as plt

def raster(event_times_list, colors):
    """
    Creates a raster plot

    Parameters
    ----------
    event_times_list : iterable
                       a list of event time iterables
    color : string
            color of vlines

    Returns
    -------
    ax : an axis containing the raster plot
    """
    ax = plt.gca()
    for ith, trial in enumerate(event_times_list):
        plt.vlines(trial, ith + .5, ith + 1.5, color=colors[ith])
    plt.ylim(.5, len(event_times_list) + .5)
    return ax

if __name__ == '__main__':
    # example usage
    # Generate test data
    nbins = 100
    ntrials = 10
    spikes = []
    colors=["r" for i in range(9)]
    colors.append("b")
    for i in range(ntrials):
        spikes.append(np.arange(nbins)[np.random.rand(nbins) < .2])

    fig = plt.figure()
    ax = raster(spikes,colors)
    plt.title('Example raster plot')
    plt.xlabel('time')
    plt.ylabel('trial')
    fig.show()
