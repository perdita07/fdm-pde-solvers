def solve_poisson(N, C):
    dx = 1.0 / (N - 1)
    A = np.zeros((N**2, N**2))
    b = np.zeros(N**2)

    for j in range(N):
        for i in range(N):
            idx = i + j * N
            x, y = i * dx, j * dx

            if i == 0: A[idx, idx], b[idx] = 1, 100
            elif i == N - 1: A[idx, idx], b[idx] = 1, 400
            elif j == 0: A[idx, idx], b[idx] = 1, 200
            elif j == N - 1: A[idx, idx], b[idx] = 1, 300
            else:
                A[idx, idx] = -4
                A[idx, idx - 1] = A[idx, idx + 1] = 1
                A[idx, idx - N] = A[idx, idx + N] = 1
                b[idx] = C * np.exp(-((x - 0.5)**2 + (y - 0.5)**2)) * dx**2

    T = np.linalg.solve(A, b)
    return T.reshape((N, N))
