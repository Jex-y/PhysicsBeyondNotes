from graph_func import graph_time_func_3D
import numpy as np
r = 1
w = 1
v = 1
f = lambda t: [r*np.cos(w*t),r*np.sin(w*t),v*t]
graph_time_func_3D(f,0,6*np.pi,360*24)