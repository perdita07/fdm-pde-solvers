import numpy as np
import matplotlib.pyplot as plt

def initialize_temperature(N):
    """
    Initializes temperature profile for a 1D rod.
    
    Parameters:
        N (int): Number of spatial intervals (grid points = N+1)
    
    Returns:
        np.ndarray: Initial temperature array
    """
    u = np.full(N + 1, 25.0)  # Initial temperature = 25°C
    u[0] = 100.0              # Left boundary condition
    return u

def explicit_fd_step(N, num_steps, alpha_dt_by_dx2, u_init, snapshot_steps):
    """
    Runs the explicit finite difference time stepping.
    
    Parameters:
        N (int): Number of spatial intervals
        num_steps (int): Number of time steps to run
        alpha_dt_by_dx2 (float): Stability factor
        u_init (np.ndarray): Initial temperature profile
        snapshot_steps (list of int): Time steps at which to store snapshots
    
    Returns:
        List of np.ndarray: Stored temperature profiles
    """
    profiles = []
    u = u_init.copy()

    for step in range(num_steps):
        u_new = u.copy()
        for i in range(1, N):
            u_new[i] = u[i] + alpha_dt_by_dx2 * (u[i + 1] - 2 * u[i] + u[i - 1])
        u = u_new.copy()

        if step in snapshot_steps:
            profiles.append(u.copy())

    return profiles

def plot_temperature_profile(N, profiles, snapshot_steps, dt, save=False, filename=None):
    """
    Plots the temperature profiles at selected time steps.
    
    Parameters:
        N (int): Number of spatial intervals
        profiles (List[np.ndarray]): Temperature profiles at selected time steps
        snapshot_steps (List[int]): Time steps corresponding to the profiles
        dt (float): Time step size
        save (bool): Whether to save the plot
        filename (str): Filename to save plot to (only if save=True)
    """
    x = np.linspace(0, 1.0, N + 1)
    plt.figure(figsize=(10, 6))

    for i, profile in enumerate(profiles):
        plt.plot(x, profile, label=f"Step {snapshot_steps[i]} ({snapshot_steps[i]*dt:.4f} s)")

    plt.xlabel("Position along rod (m)")
    plt.ylabel("Temperature (°C)")
    plt.title(f"1D Heat Conduction: N = {N}")
    plt.legend()
    plt.grid(True)

    if save and filename:
        plt.savefig(filename, dpi=300)
        print(f"[+] Plot saved as {filename}")
    else:
        plt.show()

def simulate(N, L=1.0, T=0.1, alpha=1.0, dt=1e-5, save_plots=False):
    """
    Runs the full simulation for a given N and plots results.
    
    Parameters:
        N (int): Number of spatial intervals
        L (float): Length of rod (m)
        T (float): Total simulation time (s)
        alpha (float): Thermal diffusivity (m²/s)
        dt (float): Time step size (s)
        save_plots (bool): Whether to save the plot as a PNG
    """
    dx = L / N
    alpha_dt_by_dx2 = alpha * dt / dx**2
    num_steps = int(T / dt)

    if alpha_dt_by_dx2 > 0.5:
        print(f"[!] Skipping N = {N}: Unstable (α·dt/dx² = {alpha_dt_by_dx2:.3f} > 0.5)")
        return

    u_init = initialize_temperature(N)
    snapshot_steps = [0, int(num_steps * 0.25), int(num_steps * 0.5), int(num_steps * 0.75), num_steps - 1]
    profiles = explicit_fd_step(N, num_steps, alpha_dt_by_dx2, u_init, snapshot_steps)

    filename = f"temperature_profile_N_{N}.png" if save_plots else None
    plot_temperature_profile(N, profiles, snapshot_steps, dt, save=save_plots, filename=filename)

def main():
    # Run simulation for multiple N values
    N_values = [10, 20, 40, 80, 160, 200]
    for N in N_values:
        simulate(N, save_plots=True)

if __name__ == "__main__":
    main()
