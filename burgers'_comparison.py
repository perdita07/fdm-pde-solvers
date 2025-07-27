def burgers_schemes(nu=1, nt=1000, dt=1e-5, L=1.0, nx=101):
    dx = L / (nx - 1)
    x = np.linspace(0, L, nx)
    u_initial = np.sin(2 * np.pi * x)
    u_left, u_right = 0.0, 0.0

    def solve_explicit():
        u, u_next = u_initial.copy(), u_initial.copy()
        sol = [u.copy()]
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
                sol.append(u.copy())
        return sol

    def solve_implicit():
        u, u_next = u_initial.copy(), u_initial.copy()
        sol = [u.copy()]
        main_diag = (1 + nu * dt / dx**2) * np.ones(nx - 2)
        off_diag = (-nu * dt / (2 * dx**2)) * np.ones(nx - 3)
        A = diags([off_diag, main_diag, off_diag], [-1, 0, 1]).tocsc()

        for n in range(nt):
            rhs = u[1:-1] + (nu * dt / (2 * dx**2)) * (u[2:] - 2 * u[1:-1] + u[:-2])
            u_next[1:-1] = spsolve(A, rhs)
            u_next[0], u_next[-1] = u_left, u_right
            u[:] = u_next
            if n in [0, nt // 2, nt - 1]:
                sol.append(u.copy())
        return sol

    return x, solve_explicit(), solve_implicit()
