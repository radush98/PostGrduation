import numpy as np

# Пример матрицы
with open ('bijective-non2-matrix-SAC4.txt', 'r') as f:
    for m in f:
        matrix = np.array(eval(m))
        
        print('>>>>>>>>>>>>>>>>>\n\n')
        print("Матрица:\n", matrix)

        # Ранг матрицы
        rank = np.linalg.matrix_rank(matrix)
        print("Ранг матрицы:", rank)

        # Определитель матрицы (для квадратной матрицы)
        if matrix.shape[0] == matrix.shape[1]:  # Проверка на квадратность
            determinant = np.linalg.det(matrix)
            print("Определитель матрицы:", determinant)

        # След матрицы (для квадратной матрицы)
        if matrix.shape[0] == matrix.shape[1]:  # Проверка на квадратность
            trace = np.trace(matrix)
            print("След матрицы:", trace)

        # Нормы матрицы
        frobenius_norm = np.linalg.norm(matrix, ord='fro')
        operator_norm = np.linalg.norm(matrix, ord=2)
        spectral_norm = np.linalg.norm(matrix, ord=np.inf)
        print("Норма Фробениуса матрицы:", frobenius_norm)
        print("Операторная норма матрицы:", operator_norm)
        print("Спектральная норма матрицы:", spectral_norm)

        # Кондиционное число матрицы
        if matrix.shape[0] == matrix.shape[1]:  # Проверка на квадратность
            condition_number = np.linalg.cond(matrix)
            print("Кондиционное число матрицы:", condition_number)

        # Собственные значения и векторы (для квадратной матрицы)
        if matrix.shape[0] == matrix.shape[1]:  # Проверка на квадратность
            eigenvalues, eigenvectors = np.linalg.eig(matrix)
            print("Собственные значения матрицы:", eigenvalues)
            print("Собственные векторы матрицы:", eigenvectors)
