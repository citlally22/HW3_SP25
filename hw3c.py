import math
from DoolittleMethod import Doolittle
from matrixOperations import Transpose, MatrixMultiply

def is_symmetric(matrix):
    """Check if the matrix is symmetric."""
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True

def is_positive_definite(matrix):
    """Check if the matrix is positive definite."""
    try:
        n = len(matrix)
        for i in range(1, n + 1):
            sub_matrix = [row[:i] for row in matrix[:i]]
            det = determinant(sub_matrix)
            if det <= 0:
                return False
        return True
    except Exception:
        return False

def determinant(matrix):
    """Compute the determinant of a matrix."""
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c + 1:] for row in matrix[1:]]
        det += ((-1) ** c) * matrix[0][c] * determinant(sub_matrix)
    return det

def cholesky_decomposition(matrix):
    """Perform Cholesky decomposition on a symmetric positive definite matrix."""
    n = len(matrix)
    L = [[0.0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(matrix[i][i] - sum_k)
            else:
                L[i][j] = (matrix[i][j] - sum_k) / L[j][j]
    return L

def forward_substitution(L, b):
    """Solve Ly = b for y using forward substitution."""
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y

def backward_substitution(U, y):
    """Solve Ux = y for x using backward substitution."""
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

def solve_cholesky(matrix, b):
    """Solve Ax = b using Cholesky decomposition."""
    L = cholesky_decomposition(matrix)
    y = forward_substitution(L, b)
    LT = Transpose(L)
    x = backward_substitution(LT, y)
    return x

def main():
    print("Matrix Solver: Cholesky and Doolittle Methods")

    # Problem 1
    A1 = [
        [1, -1, 3, 2],
        [-1, 5, -5, -2],
        [3, -5, 19, 3],
        [2, -2, 3, 21]
    ]
    b1 = [15, -35, 94, 1]

    # Problem 2
    A2 = [
        [4, 2, 4, 0],
        [2, 2, 3, 2],
        [4, 3, 6, 3],
        [0, 2, 3, 9]
    ]
    b2 = [20, 36, 60, 122]

    problems = [(A1, b1, "Problem 1"), (A2, b2, "Problem 2")]

    for A, b, label in problems:
        print(f"\n{label}:")
        print("Matrix A:")
        for row in A:
            print(row)
        print("\nVector b:")
        print(b)

        if is_symmetric(A) and is_positive_definite(A):
            print("\nMatrix is symmetric and positive definite. Using Cholesky Decomposition.")
            x = solve_cholesky(A, b)
        else:
            print("\nMatrix is not symmetric and/or not positive definite. Using Doolittle Method.")
            # Convert A and b into augmented matrix format expected by Doolittle
            A_augmented = [row + [b[i]] for i, row in enumerate(A)]
            x = Doolittle(A_augmented)

        print("\nSolution vector x:")
        print(x)

if __name__ == "__main__":
    main()
