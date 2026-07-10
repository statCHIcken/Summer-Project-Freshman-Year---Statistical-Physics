import numpy as np
import matplotlib.pyplot as plt

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
    eta = np.sqrt(2 * gamma * kB * T_bath * dt / m) * np.random.normal(0, 1, n_particles)
    v += (-gamma * v / m) * dt + eta
    x += v * dt
    time.append(t)
    msd.append(np.mean(x**2))

v2_mean = np.mean(v**2)
T_computed = m * v2_mean / kB


#Mean square dispacement plot
time = np.array(time)
msd = np.array(msd)
plt.figure(figsize=(8,6))
plt.plot(time, msd)

plt.xlabel("Time")
plt.ylabel("Mean Squared Displacement")
plt.title("MSD vs Time")
plt.grid()
plt.show()

fit_start = int(0.3 * len(time)) # for diffusion start from 0.3 of total time 
slope, intercept = np.polyfit(time[fit_start:],msd[fit_start:],1)
#diffuson coefficient
D_sim = slope / 2 #<x^2(t)>=2Dt

D_theory = kB * T_computed / (m * gamma)

print("========== DIFFUSION ==========")
print("D (Simulation) =", D_sim)
print("D (Theory)     =", D_theory)

#linear fit for mean sq dispacement graph
fit_line = slope * time + intercept
plt.figure(figsize=(8,6))
plt.plot(time,msd,label="Mean Square Displacement", color='black')

plt.plot(time,fit_line,'--',linewidth=2,label="Linear Fit")

plt.xlabel("Time")
plt.ylabel("Mean Squared Displacement and its linear fit")

plt.title(f"Diffusion Coefficient\n"f"D simulation = {D_sim:.4f}, "f"D theoretical = {D_theory:.4f}")

plt.legend()
plt.grid()

plt.show()