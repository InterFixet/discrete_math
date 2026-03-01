def disjunction(A, B): # Дизъюнкция
    n, m = len(A), len(A[0])
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] or B[i][j]
    return C

def transpose(A): # Транспонирование
    n, m = len(A), len(A[0])
    return [[A[i][j] for i in range(n)] for j in range(m)]

def inverse(A): # Инвертирование
    At = transpose(A)
    n, m = len(At), len(At[0])
    return [[1 - At[i][j] for j in range(m)] for i in range(n)]

def subtraction(A, B): # Вычитание
    n, m = len(A), len(A[0])
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            C[i][j] = A[i][j] and (1 - B[i][j])
    return C

def multiplication(A, B): # Умножение
    n, m = len(A), len(B[0])
    k = len(A[0])  # = len(B)
    C = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            for t in range(k): # или по k
                if A[i][t] and B[t][j]:
                    C[i][j] = 1
                    break
    return C

def print_matrix(name, matrix):
    print(f"\n{name}:")
    for row in matrix:
        print(row)

# Пример
R1 = [
    [0, 1, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 0, 0, 0]
]

R2 = [
    [1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0]
]

print("ИСХОДНЫЕ МАТРИЦЫ:")
print_matrix("R1", R1)
print_matrix("R2", R2)

print("\n1. Дизъюнкция R1 ∨ R2")
print_matrix("Результат", disjunction(R1, R2))

print("\n2. Транспонирование R1ᵀ")
print_matrix("Результат", transpose(R1))

print("\n3. Инвертирование R1̄")
print_matrix("Результат", inverse(R1))

print("\n4. Вычитание R1 - R2")
print_matrix("Результат", subtraction(R1, R2))

print("\n5. Умножение R1 × R1ᵀ")
print_matrix("Результат", multiplication(R1, transpose(R1)))