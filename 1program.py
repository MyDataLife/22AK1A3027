mport numpy as np

def add_matrices(A, B):
    return np.add(A, B)

def subtract_matrices(A, B):
    return np.subtract(A, B)

def multiply_matrices(A, B):
    return np.dot(A, B)

def trace_of_matrix(A):
    return np.trace(A)

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

addition_result = add_matrices(A, B)
print("Addition of matrices:\n", addition_result)

subtraction_result = subtract_matrices(A, B)
print("\nSubtraction of matrices:\n", subtraction_result)

multiplication_result = multiply_matrices(A, B)
print("\nMultiplication of matrices:\n", multiplication_result)

trace_result = trace_of_matrix(A)
print("\nTrace of matrix A:", trace_result)