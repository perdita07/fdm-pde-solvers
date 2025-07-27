def solve_2d_steady(Nx, Ny, Lx=1.0, Ly=1.0, T_left=100, T_right=400, T_bottom=200, T_top=300):
    dx, dy = Lx / Nx, Ly / Ny
    N = (Nx - 1) * (Ny - 1)
    A = np.zeros((N, N))
    b = np.zeros(N)

    for i in range(Nx - 1):
        for j in range(Ny - 1):
            idx = i * (Ny - 1) + j
            if i > 0: A[idx, (i - 1) * (Ny - 1) + j] = 1
            else: b[idx] -= T_left
            if i < Nx - 2: A[idx, (i + 1) * (Ny - 1) + j] = 1
            else: b[idx] -= T_right
            if j > 0: A[idx, i * (Ny - 1) + (j - 1)] = 1
            else: b[idx] -= T_bottom
            if j < Ny - 2: A[idx, i * (Ny - 1) + (j + 1)] = 1
            else: b[idx] -= T_top
            A[idx, idx] = -4

    T_interior = np.linalg.solve(A, b)
    T_grid = np.zeros((Nx + 1, Ny + 1))
    T_grid[0, :], T_grid[-1, :] = T_left, T_right
    T_grid[:, 0], T_grid[:, -1] = T_bottom, T_top

    for i in range(1, Nx):
        for j in range(1, Ny):
            idx = (i - 1) * (Ny - 1) + (j - 1)
            T_grid[i, j] = T_interior[idx]

    return T_grid
