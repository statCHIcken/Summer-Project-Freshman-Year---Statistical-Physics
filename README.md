# Summer-Project-Freshman-Year---Statistical-Physics
This repository contains work completed during my summer project at IISER Mohali under the guidance of Prof. Prasenjit Das.

## 1. Emergence of Gaussian Distribution
This assignment explores how averaging random numbers leads to the emergence of a Gaussian (bell-curve) distribution.



### Output Graph
The comparison below shows how distributions evolve for averaging:
- 2 random numbers  
- 3 random numbers  
- 4 random numbers  
- 5 random numbers  
- 10 random numbers



### Concepts Explored
- Gaussian Distribution
- Central Limit Theorem
- Random Variables

## 2. One Particle Simulation As Per The Langevin Model

Simulation of a Brownian particle using the Langevin equation in Python.

The system models the motion of a particle under:

- Friction (dissipation)
- Random Gaussian thermal noise (fluctuations)

The Langevin equation used:

m(dv/dt) = -γv + η(t)


### Features

- Velocity vs Time
- Velocity Squared vs Time
- Position vs Time
- Position Squared vs Time

### Parameters Used

- Mass (m)
- Friction coefficient (γ)
- Time step (dt)
- Thermal energy (kBT)

## Concepts Used

- Brownian Motion
- Langevin Equation
- Gaussian Noise
- Fluctuation-Dissipation
- Statistical Mechanics

## 3. Multiple Particles Simulation As Per The Langevin Model

This project extends the single-particle Langevin simulation to study the **emergence of statistical behavior** in systems with increasing particle number.

The simulation was performed for:

* 2 particles
* 10 particles
* 50 particles
* 100 particles
* 500 particles

Each particle evolves independently under **Langevin dynamics**, receiving:

* **Frictional damping (dissipation)**
* **Independent Gaussian thermal noise (fluctuations)**

The Langevin equation used is:

m(dv/dt) = -γv + η(t)

where random thermal kicks are modeled using Gaussian noise satisfying thermal fluctuations.

### Objective

The goal of this simulation is to observe how **statistical mechanics behavior emerges** as the number of particles increases.

For a small number of particles, the dynamics are highly stochastic and fluctuate strongly. As the particle number increases, ensemble averages become smoother and approach expected statistical behavior.

### Quantities Studied

The following quantities were computed and plotted:

* Average Velocity vs Time ⟨v⟩
* Average Velocity Squared vs Time ⟨v²⟩
* Average Position vs Time ⟨x⟩
* Average Position Squared vs Time ⟨x²⟩

### Observations

#### Small Particle Number (2–10 particles)

* Strong fluctuations are observed.
* Individual stochastic effects dominate.
* Equilibrium behavior is less apparent.

#### Intermediate Particle Number (50–100 particles)

* Ensemble averages become smoother.
* Velocity fluctuations begin approaching thermal equilibrium.
* Diffusive behavior becomes clearer.

#### Large Particle Number (500 particles)

* Statistical behavior becomes clearly visible.
* Fluctuations reduce significantly.
* Ensemble properties emerge more cleanly, illustrating core ideas of statistical mechanics.

### Physics Concepts Used

* Brownian Motion
* Langevin Equation
* Gaussian Noise
* Diffusion
* Thermal Equilibrium
* Ensemble Averaging
* Fluctuation–Dissipation
* Statistical Mechanics
* Non-equilibrium Statistical Mechanics

### Computational Tools

* Python
* NumPy
* Matplotlib

## 4. Thermalization, Maxwell–Boltzmann Distribution and Diffusion:
Extended the Langevin dynamics simulation to multi-particle to investigate the emergence of equilibrium statistical behaviour.

### Work Completed
* Extended the analysis to **100000 particles** for statistical measurements
* Computed temperature from **mean squared velocity**
* Generated **velocity distribution functions**
* Compared numerical results with the **Maxwell–Boltzmann distribution**
* Computed and analysed the **diffusion coefficient**
* Compared simulation and theoretical predictions

### Additional Analysis
* Computed **Mean Squared Displacement (MSD)**
* Generated **MSD vs Time** plots
* Generated **log(MSD) vs log(Time)** plots
* Observed:

  * **Ballistic regime:** (MSD proportional t^2)
  * **Diffusive regime:** (MSD proportional t)
* Identified the crossover between short-time and long-time behaviour

### Key Concepts Explored

* Langevin Equation
* Brownian Motion
* Thermalization
* Maxwell–Boltzmann Distribution
* Fluctuation–Dissipation Relation
* Mean Squared Displacement (MSD)
* Diffusion

* # Summer-Project-Freshman-Year---Statistical-Physics
This repository contains work completed during my summer project at IISER Mohali under the guidance of Prof. Prasenjit Das.

## 1. Emergence of Gaussian Distribution
This assignment explores how averaging random numbers leads to the emergence of a Gaussian (bell-curve) distribution.

[Python Code](Code%20files/Gaussian%20Emergence%20from%20random%20numbers.py)

### Output Graph
The comparison below shows how distributions evolve for averaging:
- 2 random numbers  
- 3 random numbers  
- 4 random numbers  
- 5 random numbers  
- 10 random numbers

[Output Plots](Random%20Number%20Plots%20tending%20to%20Gaussian%20Distribution.pdf)

### Concepts Explored
- Gaussian Distribution
- Central Limit Theorem
- Random Variables

## 2. One Particle Simulation As Per The Langevin Model

Simulation of a Brownian particle using the Langevin equation in Python.

The system models the motion of a particle under:

- Friction (dissipation)
- Random Gaussian thermal noise (fluctuations)

The Langevin equation used:

m(dv/dt) = -γv + η(t)

[Python Code](Simulating%20one%20%20particle%20as%20per%20Langevin%20model.py)

### Features

- Velocity vs Time
- Velocity Squared vs Time
- Position vs Time
- Position Squared vs Time

### Parameters Used

- Mass (m)
- Friction coefficient (γ)
- Time step (dt)
- Thermal energy (kBT)

### Sample Output
[Output Plots](One%20Particle%20Simulation.png)


## Concepts Used

- Brownian Motion
- Langevin Equation
- Gaussian Noise
- Fluctuation-Dissipation
- Statistical Mechanics

## 3. Multiple Particles Simulation As Per The Langevin Model

This project extends the single-particle Langevin simulation to study the **emergence of statistical behavior** in systems with increasing particle number.

The simulation was performed for:

* 2 particles
* 10 particles
* 50 particles
* 100 particles
* 500 particles

Each particle evolves independently under **Langevin dynamics**, receiving:

* **Frictional damping (dissipation)**
* **Independent Gaussian thermal noise (fluctuations)**

The Langevin equation used is:

m(dv/dt) = -γv + η(t)

where random thermal kicks are modeled using Gaussian noise satisfying thermal fluctuations.

### Objective

The goal of this simulation is to observe how **statistical mechanics behavior emerges** as the number of particles increases.

For a small number of particles, the dynamics are highly stochastic and fluctuate strongly. As the particle number increases, ensemble averages become smoother and approach expected statistical behavior.

### Quantities Studied

The following quantities were computed and plotted:

* Average Velocity vs Time ⟨v⟩
* Average Velocity Squared vs Time ⟨v²⟩
* Average Position vs Time ⟨x⟩
* Average Position Squared vs Time ⟨x²⟩

### Observations

#### Small Particle Number (2–10 particles)

* Strong fluctuations are observed.
* Individual stochastic effects dominate.
* Equilibrium behavior is less apparent.

#### Intermediate Particle Number (50–100 particles)

* Ensemble averages become smoother.
* Velocity fluctuations begin approaching thermal equilibrium.
* Diffusive behavior becomes clearer.

#### Large Particle Number (500 particles)

* Statistical behavior becomes clearly visible.
* Fluctuations reduce significantly.
* Ensemble properties emerge more cleanly, illustrating core ideas of statistical mechanics.

### Physics Concepts Used

* Brownian Motion
* Langevin Equation
* Gaussian Noise
* Diffusion
* Thermal Equilibrium
* Ensemble Averaging
* Fluctuation–Dissipation
* Statistical Mechanics
* Non-equilibrium Statistical Mechanics

### Computational Tools

* Python
* NumPy
* Matplotlib
[Code](Simulating%20Multiple%20Particles%20As%20Per%20Langevin%20Model.py)

### Simulation Outputs

* [2 Particles](Two%20Particle%20Simulation.png)
* [10 Particles](Ten%20Particles%20Simulation.png)
* [50 Particles](Fifty%20Particles%20Simulation.png)
* [100 Particles](Hundred%20Particles%20Simulation.png)
* [500 Particles](Five%20Hundred%20Particles%20Simulation.png)

## 4. Thermalization, Maxwell–Boltzmann Distribution and Diffusion:
Extended the Langevin dynamics simulation to multi-particle to investigate the emergence of equilibrium statistical behaviour.

### Work Completed
* Extended the analysis to **100000 particles** for statistical measurements
* Computed temperature from **mean squared velocity**
* Generated **velocity distribution functions**
* Compared numerical results with the **Maxwell–Boltzmann distribution**
* Computed and analysed the **diffusion coefficient**
* Compared simulation and theoretical predictions

### Additional Analysis
* Computed **Mean Squared Displacement (MSD)**
* Generated **MSD vs Time** plots
* Generated **log(MSD) vs log(Time)** plots
* Observed:

  * **Ballistic regime:** (MSD proportional t^2)
  * **Diffusive regime:** (MSD proportional t)
* Identified the crossover between short-time and long-time behaviour

### Key Concepts Explored

* Langevin Equation
* Brownian Motion
* Thermalization
* Maxwell–Boltzmann Distribution
* Fluctuation–Dissipation Relation
* Mean Squared Displacement (MSD)
* Diffusion

### Code
#### Computed temperature , maxwell-boltzmann distribution :
[Code](MB%20distribution.py)

[Computed Temperature Value](Computed%20Temperature.png)

[Maxwell-Boltzmann Distribution](Maxwell%20Boltzmann%20Simulation.png)


#### Diffusion Coefficient , Mean Square Displacement :
[Code](Diffusion%20coeff%20and%20mean%20square%20displacement.py)

[Diffusion Coefficient Value](Diffusion%20coefficients.png)

[Mean Square Diplacement vs Time Plot](MSD%20vs%20time.png)

#### Mean Square Displacement Nature for short (ballistic) vs long(Diffusive) time :

[Code](diffcoeffforsmallt.py)

[MSD vs Time plot](MSDvst.png)

[log (MSD) vs log (Time)](logMSD%20vs%20logt.png)

### Observations
* Computed temperature converged close to bath temperature
* Velocity distribution approached the Maxwell–Boltzmann prediction
* Diffusion behaviour agreed with theoretical expectations
* Larger particle counts produced smoother statistical behaviour and reduced fluctuations


### Observations
* Computed temperature converged close to bath temperature
* Velocity distribution approached the Maxwell–Boltzmann prediction
* Diffusion behaviour agreed with theoretical expectations
* Larger particle counts produced smoother statistical behaviour and reduced fluctuations
