# 1D Heat Conduction Simulation using Explicit Finite Difference

Simulates 1D transient heat conduction in a rod using the explicit finite difference method. Includes temperature profile plots, stability checks, and support for multiple grid resolutions.

## Method

Solves the heat equation:

∂u/∂t = α ∂²u/∂x²

Boundary conditions:
- Left end fixed at 100°C
- Initial temperature elsewhere: 25°C

The simulation uses an explicit time-stepping scheme and enforces the CFL condition:

α · (dt / dx²) < 0.5

## Features

- Explicit finite difference method for the heat equation
- CFL stability check
- Supports multiple values of N (number of grid intervals)
- Plots temperature profiles at fixed time steps
- Optionally saves plots as PNG files

## Requirements

- Python 3.x
- numpy
- matplotlib

Install dependencies with:
pip install -r requirements.txt

## How to Run

Clone the repository and run the script: python heat_conduction_1D.py

This will run the simulation for several values of N and generate plots.

# Sample Outputs

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/857839ee-900c-4a52-8a0b-3b482d06077f" />

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/cd029881-c925-4ed6-8994-74b88b3160da" />

<img width="850" height="547" alt="image" src="https://github.com/user-attachments/assets/ef960e1e-c991-4f55-bf86-9e673004c6d0" />


