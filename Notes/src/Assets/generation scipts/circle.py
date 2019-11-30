from graph_func import graph_time_func
import numpy as np
r = 1
s = 1
f = lambda t: [r*np.cos(s*t),r*np.sin(s*t)]
graph_time_func(f,0,2*np.pi,360*4)