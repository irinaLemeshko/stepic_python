st = input()
matrix = []
while st != 'end':
    matrix.append([int(i) for i in st.split()])
    st = input()
result_matrix = []
for i in range(len(matrix)):
    result_matrix.append([])
    for j in range(len(matrix[0])):
        result_matrix[i].append(matrix[i-1][j]
                                + matrix[(i+1) % len(matrix)][j]
                                + matrix[i][j-1]
                                + matrix[i][(j+1) % len(matrix[0])])
for i in range(len(result_matrix)):
    for j in range(len(result_matrix[0])):
        print(result_matrix[i][j], end=' ')
    print()