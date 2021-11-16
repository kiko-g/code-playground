def floodFill(matrix, n, m):
    flow(matrix, 0, 0, n, m, 0)


def flow(matrix, x, y, n, m, score):
    if x >= m or y >= n: return
    score += matrix[y][x]
    flow(matrix, x+1, y, n, m, score)
    flow(matrix, x, y+1, n, m, score)
    print(f'score: {score}')


if __name__ == '__main__':
    [n, m] = [int(elem) for elem in input().split()]
    matrix = []
    for i in range(0, n):
        matrix.append([int(elem) for elem in input().split()])

    print('--------')
    print(floodFill(matrix, n, m))
