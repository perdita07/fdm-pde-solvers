def burgers_explicit(nu=0, nt=1000, dt=0.0001, L=1.0, nx=101):
    dx = L / (nx - 1)
    x = np.linspace(0, L, nx)
    u = np.sin(2 * np.pi * x)
    u_next = u.copy()
    u_left, u_right = 0.0, 0.0
    solutions = [u.copy()]
    for n in range(nt):
        for i in range(1, nx - 1):
            u_next[i] = (
                u[i]
                - dt / dx * u[i] * (u[i] - u[i - 1])
                + nu * dt / dx**2 * (u[i + 1] - 2 * u[i] + u[i - 1])
            )
        u_next[0], u_next[-1] = u_left, u_right
        u[:] = u_next
        if n in [0, nt // 2, nt - 1]:
            solutions.append(u.copy())

    return x, solutions

def plot_burgers(x, solutions, label, title):
    plt.figure(figsize=(10, 6))
    for i, u in enumerate(solutions):
        plt.plot(x, u, label=f'Time Step {i * (len(solutions)-1) * 0.5:.0f}')
    plt.axhline(0, color='black', linestyle='--', linewidth=0.5)
    plt.axvline(0, color='black', linestyle='--', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('u')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()
