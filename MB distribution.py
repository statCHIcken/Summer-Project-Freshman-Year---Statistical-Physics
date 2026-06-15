import numpy as np
import matplotlib.pyplot as plt

# PARAMETERS
n_particles = 100000
m = 1.0
gamma = 2.0
kB = 1.0
T_bath = 5.0
dt = 0.01
total_time = 100
n_steps = int(total_time / dt)

x = np.zeros(n_particles)
v = np.zeros(n_particles)
time = []
msd = []

for step in range(n_steps):
    t = step * dt
    eta = np.sqrt(2 * gamma * kB * T_bath * dt / m) * np.random.normal(0, 1, n_particles)#random effect for nparticles

    v += (-gamma * v / m) * dt + eta

    x += v * dt

    time.append(t)
    msd.append(np.mean(x**2))

v2_mean = np.mean(v**2)

T_computed = m * v2_mean / kB #computed temperature from mean square velocity as per the simulation
print("========== TEMPERATURE ==========")
print("Bath Temperature      =", T_bath)
print("Computed Temperature  =", T_computed)
print("<v²>                  =", v2_mean)

vmin = np.min(v)
vmax = np.max(v)
#start of distribution plots
v_grid = np.linspace(vmin, vmax, 1000)
MB = np.sqrt(m / (2 * np.pi * kB * T_computed)) * np.exp(-m * v_grid**2 / (2 * kB * T_computed))
plt.figure(figsize=(8,6))

plt.hist(v,bins=1000,density=True,alpha=0.7,label=" Velocity Distribution",color='black')

plt.plot(v_grid,MB,linewidth=2,label="Maxwell-Boltzmann")

plt.xlabel("Velocity")
plt.ylabel("Probability Density")
plt.title("Velocity Distribution And MB Distribution Comparison")
plt.legend()
plt.grid()

plt.show()

