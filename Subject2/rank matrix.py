import numpy as np


# Задання матриці (приклад)
matrix_example = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])


# Обчислення рангу матриці
rank = np.linalg.matrix_rank(matrix_example)


# Виведення результату
print("Матриця:")
print(matrix_example)
print("Ранг матриці:", rank)