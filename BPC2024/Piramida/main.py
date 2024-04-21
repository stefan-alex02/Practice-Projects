import sys


def matrix_mult(A, B):
    """Matrix multiplication function."""
    # Initialize the result matrix as a zero matrix
    result = [[0, 0, 0, 0] for _ in range(4)]

    # Perform matrix multiplication
    for i in range(4):
        for j in range(4):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(4))

    return result


def matrix_exponentiation(matrix, exp):
    """Matrix exponentiation function using exponentiation by squaring."""
    # Initialize result as identity matrix
    result = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

    base = matrix
    while exp > 0:
        if exp % 2 == 1:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2

    return result


def calculate_x_n(n):
    """Calculate x[n] using matrix exponentiation."""
    # Define the transformation matrix
    T = [
        [1, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0]
    ]

    # Perform matrix exponentiation
    T_exp = matrix_exponentiation(T, n)

    # Define the initial state vector
    initial_state = [1, 0, 0, 0]

    # Calculate the result vector by multiplying T_exp with the initial state vector
    result_vector = [sum(T_exp[0][j] * initial_state[j] for j in range(4))]

    return result_vector[0]

def main():
    n = int(sys.stdin.readline().strip())
    print(calculate_x_n(n-1))

if __name__ == '__main__':
    main()
