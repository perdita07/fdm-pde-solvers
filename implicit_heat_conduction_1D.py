def solve_1d_implicit(L=1.0, alpha=1.0, T_total=0.1, N=100, Fo=100):
    dx = L / N
    dt = Fo * dx**2 / alpha
    num_steps = int(T_total / dt)
    u = np.full(N + 1, 25.0)
    u[0], u[-1] = 100.0, 25.0
    A = np.zeros((N + 1, N + 1))

    for i in range(1, N):
        A[i, i - 1], A[i, i], A[i, i + 1] = -Fo, 1 + 2 * Fo, -Fo
    A[0, 0], A[-1, -1] = 1, 1

    profiles, times = [], [0, int(num_steps * 0.25), int(num_steps * 0.5), int(num_steps * 0.75), num_steps - 1]
    for n in range(num_steps):
        u = np.linalg.solve(A, u)
        if n in times:
            profiles.append(u.copy())

    return np.linspace(0, L, N + 1), profiles, [dt * t for t in times]
