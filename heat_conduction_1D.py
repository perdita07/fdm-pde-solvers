def initialize_temperature(N):
    u = np.full(N + 1, 25.0)
    u[0] = 100.0
    return u

def explicit_fd_step(N, num_steps, alpha_dt_by_dx2, u_init, snapshot_steps):
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
    x = np.linspace(0, 1.0, N + 1)
    plt.figure(figsize=(10, 6))
    for i, profile in enumerate(profiles):
        plt.plot(x, profile, label=f"Step {snapshot_steps[i]} ({snapshot_steps[i]*dt:.4f} s)")
    plt.xlabel("Position (m)")
    plt.ylabel("Temperature (°C)")
    plt.title(f"1D Heat Conduction: N = {N}")
    plt.legend()
    plt.grid(True)
    if save and filename:
        plt.savefig(filename, dpi=300)
    else:
        plt.show()

def simulate_1d_explicit(N, L=1.0, T=0.1, alpha=1.0, dt=1e-5, save_plots=False):
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
