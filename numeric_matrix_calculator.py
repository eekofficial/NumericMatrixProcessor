def add_matrices(a, b):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] += b[i][j]
    return a

def scalar_matrix(a, scalar):
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] *= scalar
    return a

def multiply_matrices(a, b):
    new_matrix = [[0 for j in range(len(b[0]))] for i in range(len(a))]
    b = transpose_matrix(b)
    for i in range(len(a)):
        for j in range(len(b)):
            new_matrix[i][j] = sum(multiply_vectors(a[i], b[j]))
    return new_matrix

def multiply_vectors(v1, v2):
    new_vector = []
    for i in range(len(v1)):
        new_vector.append(v1[i] * v2[i])
    return new_vector

def transpose_matrix(a):
    new_matrix = []
    for j in range(len(a[0])):
        vector = []
        for i in range(len(a)):
            vector.append(a[i][j])
        new_matrix.append(vector)
    return new_matrix

def transpose_side_matrix(a):
    new_matrix = []
    for j in range(len(a) - 1, -1, -1):
        vector = []
        for i in range(len(a[0]) - 1, -1, -1):
            vector.append(a[i][j])
        new_matrix.append(vector)
    return new_matrix

def transpose_vertical_matrix(a):
    a = transpose_matrix(a)
    new_matrix = a[::-1]
    return transpose_matrix(new_matrix)

def transpose_horizontal_matrix(a):
    return a[::-1]

def calculate_determinent(a):
    if len(a) == 1:
        return a[0][0]
    if len(a) == 2:
        return a[0][0] * a[1][1] - a[0][1] * a[1][0]
    else:
        i = 0
        d = 0
        for j in range(len(a[i])):
            d += (-1) ** (i + 1 + j + 1) * a[i][j] * calculate_determinent(minor(a, i, j))
        return d

def minor(a, k, l):
    m = []
    for i in range(len(a)):
        if i != k:
            v = []
            for j in range(len(a[0])):
                if j != l:
                    v.append(a[i][j])
            m.append(v)
    return m

def calculate_inverse(a):
    return scalar_matrix(transpose_matrix(cofactor_matrix(a)), 1 / calculate_determinent(a))

def cofactor_matrix(a):
    m = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a[0])):
            m[i][j] = ((-1) ** (i + 1 + j + 1)) * calculate_determinent(minor(a, i, j))
    return m


def print_matrix(a):
    for i in range(len(a)):
        print(*a[i])

while True:
    print('1. Add matrices')
    print('2. Multiply matrix by a constant')
    print('3. Multiply matrices')
    print('0. Exit')
    print('4. Transpose matrix')
    print('5. Calculate a determinant')
    print('6. Inverse matrix')
    choice = input('Your choice: ')
    if choice == '0':
        break
    elif choice == '1':
        m1, n1 = map(int, input('Enter size of first matrix: ').split())
        print('Enter first matrix:')
        matrix1 = []
        for i in range(m1):
            matrix1.append(list(map(float, input().split())))
        m2, n2 = map(int, input('Enter size of second matrix: ').split())
        print('Enter second matrix:')
        matrix2 = []
        for i in range(m2):
            matrix2.append(list(map(float, input().split())))
        if m1 != m2 or n1 != n2:
            print('The operation cannot be performed.')
        else:
            result = add_matrices(matrix1, matrix2)
            print('The result is:')
            print_matrix(result)
    elif choice == '2':
        m1, n1 = map(int, input('Enter size of matrix: ').split())
        matrix1 = []
        print('Enter matrix:')
        for i in range(m1):
            matrix1.append(list(map(float, input().split())))
        scalar = int(input('Enter constant: '))
        result = scalar_matrix(matrix1, scalar)
        print('The result is:')
        print_matrix(result)
    elif choice == '3':
        m1, n1 = map(int, input('Enter size of first matrix: ').split())
        print('Enter first matrix:')
        matrix1 = []
        for i in range(m1):
            matrix1.append(list(map(float, input().split())))
        m2, n2 = map(int, input('Enter size of second matrix: ').split())
        print('Enter second matrix:')
        matrix2 = []
        for i in range(m2):
            matrix2.append(list(map(float, input().split())))
        if n1 != m2:
            print('The operation cannot be performed.')
        else:
            result = multiply_matrices(matrix1, matrix2)
            print('The result is:')
            print_matrix(result)
    elif choice == '4':
        print('1. Main diagonal')
        print('2. Side diagonal')
        print('3. Vertical line')
        print('4. Horizontal line')
        option = input('Your choice: ')
        m, n = map(int, input('Enter matrix size: ').split())
        print('Enter matrix:')
        matrix = []
        for i in range(m):
            matrix.append(list(map(float, input().split())))
        if option == '1':
            result = transpose_matrix(matrix)
            print_matrix(result)
        elif option == '2':
            result = transpose_side_matrix(matrix)
            print_matrix(result)
        elif option == '3':
            result = transpose_vertical_matrix(matrix)
            print_matrix(result)
        elif option == '4':
            result = transpose_horizontal_matrix(matrix)
            print_matrix(result)
    elif choice == '5':
        m, n = map(int, input('Enter matrix size: ').split())
        print('Enter matrix:')
        matrix = []
        for i in range(m):
            matrix.append(list(map(float, input().split())))
        result = calculate_determinent(matrix)
        print('The result is:')
        print(result)
    elif choice == '6':
        m, n = map(int, input('Enter matrix size: ').split())
        print('Enter matrix:')
        matrix = []
        for i in range(m):
            matrix.append(list(map(float, input().split())))
        if calculate_determinent(matrix) == 0:
            print("This matrix doesn't have an inverse.")
        else:
            print('The result is:')
            result = calculate_inverse(matrix)
            print_matrix(result)



