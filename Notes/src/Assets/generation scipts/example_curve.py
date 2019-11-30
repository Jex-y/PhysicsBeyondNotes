from graph_func import graph_time_func

f = lambda t: [t**2-(7*t),t**3-t]
graph_time_func(f,-1.5,1.5,1000)