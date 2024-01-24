import numpy as np
A = np.array([
    [-1, 1, 2],
    [0, -1, -3],
    [4, -3, 2]
])
B = np.array([1, -4, 7])

def solve_gausse(a, b, verbose=False):
  try:
    n = len(b)
    augmented_matrix = np.column_stack((a, b))
    for i in range(n):
      augmented_matrix[i, :] /= augmented_matrix[i, i]
      for j in range(n):
        if i != j:
          augmented_matrix[j, :] -= augmented_matrix[j, i] * augmented_matrix[i, :]
      
    x = augmented_matrix[:, -1]
    if verbose:
        print("Матриця після прямого ходу:")
        print(augmented_matrix)
        
        print("\nВектор розв'язку x:")
        print(x)
    return x
  except ZeroDivisionError:
    print("Система рівнянь є виродженою або невирішеною.")
  return None

result = solve_gausse(A, B, verbose=True)
print(f"Вектор рішення: \r\n {result}")