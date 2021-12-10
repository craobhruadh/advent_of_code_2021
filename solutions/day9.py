
class Basin:

    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    def __init__(self, filename):
        self.load_data(filename)
        self.m, self.n = len(self.data), len(self.data[0])

    def is_low_point(self, i, j):
        is_low_point = True
        for d in self.directions:
            x, y = i+d[0], j+d[1]
            if x >= 0 and x < self.m and y >= 0 and y < self.n:
                if self.data[i][j] >= self.data[x][y]:
                    is_low_point = False
        return is_low_point

    def find_and_sum_low_points(self):
        ans = 0
        for i in range(self.m):
            for j in range(self.n):
                if self.is_low_point(i, j):
                    ans += (self.data[i][j]+1)
        return ans

    def get_basin_area(self, i, j):
        area = 1
        stack = [(i, j)]
        visited = {(i, j)}
        while stack:
            new_stack = []
            for p in stack:
                for d in self.directions:
                    x, y = p[0]+d[0], p[1]+d[1]
                    if (
                        x >= 0
                        and x < self.m
                        and y >= 0
                        and y < self.n
                        and (x, y) not in visited
                        and self.data[x][y] != 9
                        and self.data[x][y] >= self.data[p[0]][p[1]]
                    ):
                        new_stack.append((x, y))
                        visited.add((x, y))
                        area += 1
            stack = new_stack
        return area

    def find_largest_basins(self):
        """Specifically, find the 3 largest basins and sum their value"""
        basin_areas = []
        for i in range(self.m):
            for j in range(self.n):
                if self.is_low_point(i, j):
                    basin_areas.append(self.get_basin_area(i, j))
        basin_areas = sorted(basin_areas, reverse=True)
        return basin_areas[0] * basin_areas[1] * basin_areas[2]

    def load_data(self, filename):
        with open(filename) as f:
            self.data = [[int(y) for y in list(x.strip())] for x in f.readlines()]


if __name__ == "__main__":
    basin = Basin('../data/test_day9.txt')
    print(basin.find_and_sum_low_points())
    print(basin.find_largest_basins())

    basin = Basin('../data/input_day9.txt')
    print(basin.find_and_sum_low_points())
    print(basin.find_largest_basins())
