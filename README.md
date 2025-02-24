# LJ-Simulator
>A 2D Lennard-Jones potential simulator implemented in Python.

## Features

Models particle interactions using the Lennard-Jones potential, commonly used in molecular dynamics. In each time-step of the simulation, pairwise Lennard-Jones forces are calculated to determine particle interactions.

* Real-time simulation of particles interacting via the Lennard-Jones potential.
* Dynamic visualization using Pygame with force-dependent particle coloring.
* Collision handling with .
* Velocity-Verlet integration for stable time stepping.

## Lennard-Jones Potential
The Lennard-Jones potential describes interactions between a pair of neutral atoms or molecules:


The force exerted by the Lennard-Jones potential is obtained by taking the negative gradient of the potential:


This simulator demonstrates a fundamental principle of molecular dynamics. Interactions between particles can be approximated using modular force laws based on distance. The Lennard-Jones potential effectively models repulsion at very close distances, attraction at medium disatances, and minimal interaction at long distances.

* **ε (epsilon)** controls the depth of the potential well.
* **σ (sigma)** is the distance at which the potential reaches zero.
* The **r⁻¹² term** models short-range repulsion.
* The **r⁻⁶ term** represents longer-range attraction.

By tuning ε and σ, different material behaviors can be approximated, making this model useful in particle physics, chemistry, and material science simulations. The default implementation 

Learn more about the Lennard-Jones potential [here](https://en.wikipedia.org/wiki/Lennard-Jones_potential).

## How to Run
Ensure Python 3.8+ is installed and install pygame:
```bash
pip install pygame
```

Run the simulation:
```bash
python main.py
```
