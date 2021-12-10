

def is_low_point(data, i, j):
    m, n = len(data), len(data[0])
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    is_low_point = True
    for d in directions:
        x, y = i+d[0], j+d[1]
        if x >= 0 and x < m and y >= 0 and y < n:
            if data[i][j] >= data[x][y]:
                is_low_point = False
    return is_low_point


def find_and_sum_low_points(data):
    m, n = len(data), len(data[0])
    ans = 0
    for i in range(m):
        for j in range(n):
            if is_low_point(data, i, j):
                ans += (data[i][j]+1)
    return ans


def get_basin_area(data, i, j):
    m, n = len(data), len(data[0])
    area = 1
    stack = [(i, j)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    visited = {(i, j)}
    while stack:
        new_stack = []
        for p in stack:
            for d in directions:
                x, y = p[0]+d[0], p[1]+d[1]
                if (
                    x >= 0
                    and x < m
                    and y >= 0
                    and y < n
                    and (x, y) not in visited
                    and data[x][y] != 9
                    and data[x][y] >= data[p[0]][p[1]]
                ):
                    new_stack.append((x, y))
                    visited.add((x, y))
                    area += 1
        stack = new_stack
    return area


def find_largest_basins(data):
    """Specifically, find the 3 largest basins and sum their value"""
    m, n = len(data), len(data[0])
    basin_areas = []
    for i in range(m):
        for j in range(n):
            if is_low_point(data, i, j):
                basin_areas.append(get_basin_area(data, i, j))
    basin_areas = sorted(basin_areas, reverse=True)
    return basin_areas[0] * basin_areas[1] * basin_areas[2]


def load_data(filename):
    with open(filename) as f:
        data = [[int(y) for y in list(x.strip())] for x in f.readlines()]
    return data


if __name__ == "__main__":
    data = load_data('../data/test_day9.txt')
    print(find_and_sum_low_points(data))
    print(find_largest_basins(data))

    data = load_data('../data/input_day9.txt')
    print(find_and_sum_low_points(data))
    print(find_largest_basins(data))
