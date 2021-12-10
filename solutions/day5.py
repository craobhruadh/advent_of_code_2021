def find_overlap_horizontal(data, m, n):
    arr = [[0] * m for _ in range(n)]
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            lower = min(y1, y2)
            upper = max(y1, y2)
            for y in range(lower, upper + 1):
                arr[x1][y] += 1
        elif y1 == y2:
            lower = min(x1, x2)
            upper = max(x1, x2)
            for x in range(lower, upper + 1):
                arr[x][y1] += 1

    n_overlap = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] >= 2:
                n_overlap += 1
    return n_overlap


def find_overlap_diagonals(data, m, n, verbose=False):
    arr = [[0] * n for _ in range(m)]
    for x1, y1, x2, y2 in data:
        if x1 == x2:
            lower = min(y1, y2)
            upper = max(y1, y2)
            for y in range(lower, upper + 1):
                arr[x1][y] += 1
        elif y1 == y2:
            lower = min(x1, x2)
            upper = max(x1, x2)
            for x in range(lower, upper + 1):
                arr[x][y1] += 1
        else:
            if x2 > x1:
                dx = 1
            else:
                dx = -1
            if y2 > y1:
                dy = 1
            else:
                dy = -1

            x, y = x1, y1
            while x != x2 or y != y2:
                arr[x][y] += 1
                x += dx
                y += dy
            arr[x][y] += 1

    if verbose:
        for i in range(len(arr)):
            print([x[i] for x in arr])
    n_overlap = 0
    for i in range(m):
        for j in range(n):
            if arr[i][j] >= 2:
                n_overlap += 1
    return n_overlap


if __name__ == "__main__":
    with open("../data/test_day5.txt", "r") as f:
        m, n = 10, 10
        data = f.readlines()
    data = [[int(y) for y in x.replace("->", ",").split(",")] for x in data]
    print(find_overlap_horizontal(data, m, n))
    print(find_overlap_diagonals(data, m, n))

    with open("../data/input_day5.txt", "r") as f:
        m, n = 1000, 1000
        data = f.readlines()
    data = [[int(y) for y in x.replace("->", ",").split(",")] for x in data]
    print(find_overlap_horizontal(data, m, n))
    print(find_overlap_diagonals(data, m, n))
