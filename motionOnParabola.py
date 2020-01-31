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
def normalForce(x, y, vx, vy):
	return m * (g + c * vx**2) / (1 + c**2 * x**2)


# define accelerations
def acc_x(x, y, vx, vy, Fn):
	return -c * Fn * x / m


def acc_y(x, y, vx, vy, Fn):
	return Fn / m - g


# initial conditions
y0 = 1
x0 = np.sqrt(2 * y0 / c)

# temporal resolution (sec)
dt = 1e-4

# set up arrays
t_arr = [0]
x_arr = [x0]
y_arr = [y0]
vx_arr = [0]
vy_arr = [0]
ax_arr = []
ay_arr = []
N_arr = []

# set up simulation
x = x0
y = y0
vx = 0
vy = 0
t = 0

while y >= 1e-6:
	# compute normal force
	N = normalForce(x, y, vx, vy)
	N_arr.append(N)

	# calculate accelerations
	ax = acc_x(x, y, vx, vy, N)
	ay = acc_y(x, y, vx, vy, N)
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

x_arr = np.array(x_arr[:-1])
y_arr = np.array(y_arr[:-1])
vx_arr = np.array(vx_arr[:-1])
vy_arr = np.array(vy_arr[:-1])
ax_arr = np.array(ax_arr)
ay_arr = np.array(ay_arr)
N_arr = np.array(N_arr)
t_arr = np.array(t_arr[:-1])

# calculate scalar variables
v_arr = np.sqrt(vx_arr**2 + vy_arr**2)
d_arr = np.sqrt(x_arr**2 + y_arr**2)
theta_arr = 180 * np.arctan2(vy_arr, vx_arr) / np.pi
a_arr = np.sqrt(ax_arr**2 + ay_arr**2)
T_arr = 0.5 * m * v_arr**2
U_arr = m * g * y_arr
E_arr = T_arr + U_arr

plt.plot(theta_arr, y_arr)
plt.show()
