if __name__ == '__main__':
    n = int(input())
    border = n
    layer = 0
    s = 1
    result = [[0 for j in range(n)] for i in range(n)]
    while n > 0:
        for i in range(n):
            result[layer][i + layer] = s
            s += 1
        n -= 1
        for i in range(n):
            result[i + 1 + layer][border - layer - 1] = s
            s += 1
        for i in range(n):
            result[border - layer - 1][n - i - 1 + layer] = s
            s += 1
        n -= 1
        for i in range(n):
            result[n - i + layer][layer] = s
            s += 1
        layer += 1

    for line in result:
        print(*line)
