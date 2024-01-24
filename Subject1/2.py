def print_diagonals(matrix):
    rows, cols = len(matrix), len(matrix[0])


    if rows != cols:
        print("Матриця не є квадратною. Головна та побічна діагоналі не визначені.")
        return


    main_diagonal = [matrix[i][i] for i in range(rows)]
    anti_diagonal = [matrix[i][cols - 1 - i] for i in range(rows)]


    print("Головна діагональ:", main_diagonal)
    print("Побічна діагональ:", anti_diagonal)


# Приклад використання
matrix_example = [
    [1, 2, 3],
    [4, 5, 6],
]


print_diagonals(matrix_example)