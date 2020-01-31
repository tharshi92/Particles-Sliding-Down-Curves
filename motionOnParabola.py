import numpy as np
import matplotlib.pyplot as plt

# problem parameters

# mass in kg
m = 0.1

# gravitational acceleration in m/s^2
g = 9.81

# concavity of parabola y = c x^2 / 2
c = 2.0

# normal force exerted by parabola
def normalForce(x, vx):
	return (m * g + m * c * vx**2) / (1 + c**2 * x**2)
	
# initial conditions
y0 = 1
x0 = np.sqrt(2 * y0 / c)

# temporal resolution (sec)
dt = 1e-3

# set up arrays
t_arr = [0]
x_arr = [x0]
y_arr = [y0]
vx_arr = [0]
vy_arr = [0]
ax_arr = [0]
ay_arr = [0]
N_arr = []

# set up simulation
x = x0
y = y0
vx = 0
vy = 0
ax = 0
ay = 0
t = 0

while x >= 0 and y >= 0:
	# compute normal force
	N = normalForce(x, vx)
	N_arr.append(N)
	
	# calculate accelerations
	ax = - c * N * x / m
	ay = - g + N / m
	ax_arr.append(ax)
	ay_arr.append(ay)
	
	# calculate velocities
	vx += ax * dt
	vy += ay * dt
	vx_arr.append(vx)
	vy_arr.append(vy)
	
	# calculate positions
	x += vx * dt
	y += vy * dt
	x_arr.append(x)
	y_arr.append(y)
	
	# update time
	t += dt
	t_arr.append(t)


x_arr = np.array(x_arr)
y_arr = np.array(y_arr)
vx_arr = np.array(vx_arr)
vy_arr = np.array(vy_arr)
ax_arr = np.array(ax_arr)
ay_arr = np.array(ay_arr)
t_arr = np.array(t_arr)

# calculate scalar variables
v_arr = np.sqrt(vx_arr**2 + vy_arr**2)
theta_arr = 180 * np.arctan2(vy_arr, vx_arr) / np.pi
a_arr = np.sqrt(ax_arr**2 + ay_arr**2)
T_arr = 0.5 * m * v_arr**2
U_arr = m * g * y_arr
E_arr = T_arr + U_arr

# plot 
plt.plot(N_arr, y_arr[:-1])
plt.show()
