# Lennard-Jones Simulator
>A 2D Lennard-Jones potential simulator implemented in Python to demonstrate a fundamental principle of molecular physics where interactions between particles can be approximated based off of distance.

## Features

* Pairwise Lennard-Jones forces are calculated to determine particle interactions every time-step.
* Velocity-Verlet integration for stable time stepping.
* Dynamic visualization using Pygame, with particle colors representing applied force.
* Collision detection with broad-phase distance checks and positional correction to prevent object sink.
* Collision handling using impulse-based resolution and restitution modeling to simulate energy loss.

## Lennard-Jones Potential
The Lennard-Jones potential is a standard model of intermolecular interactions:

<p align="center">
  <img src="assets/lj_potential.png" width="250">
</p>

The force exerted by the Lennard-Jones potential is obtained by taking the negative gradient of the potential:

<p align="center">
  <img src="assets/lj_force.png" width="300">
</p>

Where:
* **ε (epsilon)** controls the depth of the potential well.
* **σ (sigma)** is the distance at which the potential reaches zero.
* The **r⁻¹² term** models short-range repulsion.
* The **r⁻⁶ term** represents longer-range attraction.

By tuning ε and σ, different material behaviors can be approximated, making this model useful in molecular physics, chemistry, and material science simulations.

Learn more about the Lennard-Jones potential [here](https://en.wikipedia.org/wiki/Lennard-Jones_potential).

## Simulator in Action
<p align="center">
  <img src="assets/LJ_Sim_Ex.gif" width="500">
</p>

## How to Run
Clone this repository
```bash
git clone https://github.com/DavidSchineis/Lennard-Jones-Simulator.git
```

Ensure Python 3.8+ is installed and install required libraries:
```bash
pip install -r assets/requirements.txt
```

Run the simulation:
```bash
python main.py
```
