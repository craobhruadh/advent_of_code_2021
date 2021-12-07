from collections import Counter


def find_minimum(data):
    c = Counter(data)
    min_position = min(c.keys())
    max_position = max(c.keys())
    min_cost = float("inf")
    for i in range(min_position, max_position+1):
        total_cost = 0
        for key in c.keys():
            total_cost += (abs(key-i) * c[key])
        min_cost = min(min_cost, total_cost)
    return min_cost


def find_sum(n):
    return int(n * (n+1)/2)


def find_minimum_part_two(data):
    c = Counter(data)
    min_position = min(c.keys())
    max_position = max(c.keys())
    min_cost = float("inf")
    for i in range(min_position, max_position+1):
        total_cost = 0
        for key in c.keys():
            total_cost += (find_sum(abs(key-i)) * c[key])
        min_cost = min(min_cost, total_cost)
    return min_cost


def read_data(file):
    with open(file) as f:
        data = [int(x) for x in f.read().split(',')]
    return data


if __name__ == '__main__':
    data = read_data('../data/test_day7.txt')
    print(find_minimum(data))
    print(find_minimum_part_two(data))

    data = read_data('../data/input_day7.txt')
    print(find_minimum(data))
    print(find_minimum_part_two(data))
