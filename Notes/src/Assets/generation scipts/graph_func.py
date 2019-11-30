import matplotlib.pyplot as plt
import numpy as np

def graph_func(func,lower_bound=-10,upper_bound=10, steps = 100):
	fig = plt.figure()
	ax = plt.axes()

	x = np.linspace(lower_bound, upper_bound, steps)
	y = [func(i) for i in x]
	ax.plot(x,y)
	ax.set_ylabel("f(x)")
	ax.set_xlabel("x")
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.show()

def graph_time_func(func,t_start=0, t_end=10, steps=100):
	fig = plt.figure()
	ax = plt.axes()

	t_steps = np.linspace(t_start, t_end, steps)
	x,y = np.split(np.array([func(t) for t in t_steps]), 2, 1)
	ax.plot(x,y)
	ax.set_ylabel("y(t)")
	ax.set_xlabel("x(t)")
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	plt.show()

def graph_time_func_3D(func, t_start=0, t_end=10, steps=100):
	from mpl_toolkits import mplot3d
	fig = plt.figure()
	ax = plt.axes(projection='3d')

	t_steps = np.linspace(t_start, t_end, steps)
	x,y,z = np.split(np.array([func(t) for t in t_steps]), 3, 1)
	x, y, z = np.squeeze(x), np.squeeze(y), np.squeeze(z)
	ax.plot3D(x,y,z)
	ax.set_xlabel("x(t)")
	ax.set_ylabel("y(t)")
	ax.set_zlabel("z(t)")
	ax.set_yticklabels([])
	ax.set_xticklabels([])
	ax.set_zticklabels([])
	plt.show()