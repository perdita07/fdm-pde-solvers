# Finite Difference Methods for PDEs in Python

This repository contains Python scripts that numerically solve partial differential equations (PDEs) using finite difference methods (FDM). It includes explicit and implicit schemes for time-dependent problems and steady-state solvers for 1D and 2D cases.

---

## Contents

### 1D Heat Conduction

#### `heat_conduction_1D.py`
Simulates 1D transient heat conduction using **explicit FDM**.

- Solves: ∂u/∂t = α ∂²u/∂x²
- Boundary conditions: Dirichlet (fixed ends)
- Features:
  - Stability check (`α·dt/dx² < 0.5`)
  - Supports multiple spatial resolutions (grid intervals)
  - Visualises temperature evolution over time

#### `implicit_heat_conduction_1D.py`
Simulates the same 1D transient heat conduction using the **implicit method**.

- Uses matrix inversion at each time step (better stability)
- Allows larger time steps without CFL restriction

---

### 2D Steady-State Heat Equation

#### `2D_stead_state_heat_eqn.py`
Solves the **Laplace equation** for a 2D rectangular plate using **iterative relaxation** (Jacobi/Gauss-Seidel).

- Assumes Dirichlet boundary conditions (constant T on edges)
- Visual output using 3D surface and contour plots

---

### 2D Poisson Equation

#### `2D_poisson_eqn.py`
Solves the **2D Poisson equation**:
Δu = f(x, y)

- Includes predefined source terms (e.g., point sources or sinusoids)
- Boundary conditions: fixed at all edges
- Outputs a 3D plot of the potential field

---

### 1D Burgers' Equation

#### `burgers'.py`
Solves the **nonlinear 1D Burgers' equation** using:
- Explicit upwind method
- With and without viscosity

Useful for exploring shock formation and nonlinear wave behaviour.

#### `burgers'_comparison.py`
Compares multiple numerical schemes for Burgers' equation (e.g., FTCS, upwind, Lax, etc.)

- Plots side-by-side the evolution of solutions
- Highlights differences in numerical diffusion and stability

---

## Requirements

```bash
pip install -r requirements.txt
```

Dependencies:
- `numpy`
- `matplotlib`
- `scipy` (optional, for matrix solvers)

---

## How to Run

```bash
python filename.py
```

Each script is standalone and prompts or shows visualisations upon execution.



---

## Folder Structure

```
.
├── 2D_poisson_eqn.py
├── 2D_stead_state_heat_eqn.py
├── burgers'.py
├── burgers'_comparison.py
├── heat_conduction_1D.py
├── implicit_heat_conduction_1D.py
├── requirements.txt
└── README.md
```

---

## Concepts Covered

- Finite Difference Discretisation (Explicit & Implicit)
- CFL condition & Stability analysis
- Matrix-based solvers for PDEs
- Time evolution vs Steady-State solvers
- Nonlinear PDE handling (Burgers')



## Notes

- You can modify boundary/initial conditions directly in the scripts.
- Useful for coursework, numerical methods projects, or as FDM templates.

---

## Future work

- Add Crank–Nicolson method
- Modularise shared plotting/utilities
- Add test cases and validation with analytical solutions
