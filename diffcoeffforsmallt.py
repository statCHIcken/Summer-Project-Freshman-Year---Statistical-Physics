import numpy as np
import matplotlib.pyplot as plt

# -------------------
# Parameters
# -------------------

m=1
gamma=1
kB=1
T=1

Nparticles=10000

dt=0.005
total_time=100

steps=int(total_time/dt)

# relaxation time
tau=m/gamma

# -------------------
# Arrays
# -------------------

x=np.zeros((Nparticles,steps))
v=np.zeros((Nparticles,steps))

# -------------------
# Langevin simulation
# -------------------

for i in range(steps-1):

    noise=np.random.randn(Nparticles)

    eta=np.sqrt(
        2*gamma*kB*T*dt
    )*noise

    v[:,i+1]=(
        v[:,i]
        -
        gamma*v[:,i]*dt
        +
        eta
    )

    x[:,i+1]=(
        x[:,i]
        +
        v[:,i]*dt
    )

# -------------------
# Time and MSD
# -------------------

time=np.arange(steps)*dt

msd=np.mean(
    x**2,
    axis=0
)

# -------------------
# Normal MSD graph
# -------------------

plt.figure(figsize=(10,6))

plt.plot(
    time,
    msd,
    linewidth=3,
    label="MSD"
)

plt.axvline(
    tau,
    linestyle="--",
    label="m/gamma"
)

plt.xlabel("Time")

plt.ylabel("MSD")

plt.title(
"Mean Squared Displacement vs Time"
)

plt.legend()

plt.grid()

plt.show()

# -------------------
# Log-log graph
# -------------------

plt.figure(figsize=(10,6))

plt.loglog(
    time[1:],
    msd[1:],
    linewidth=3,
    label="Simulation"
)

# reference slope 2
ref_t=time[1:200]

plt.loglog(
    ref_t,
    ref_t**2,
    "--",
    label="Slope = 2"
)

# reference slope 1
ref_t2=time[1000:]

plt.loglog(
    ref_t2,
    10*ref_t2,
    "--",
    label="Slope = 1"
)

plt.axvline(
    tau,
    linestyle=":"
)

plt.xlabel("log(Time)")

plt.ylabel("log(MSD)")

plt.title(
" Difference in slopes of log(MSD) vs log(t) with time " \
"Initial slope > 1 , with time slope tending to 1"
)

plt.legend()

plt.grid()

plt.show()