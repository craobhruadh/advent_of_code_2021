def problem1(filename):
    with open(filename) as f:
        data = [int(x) for x in f.readlines()]

    n_increase = 0
    for i in range(1, len(data)):
        if data[i] > data[i-1]:
            n_increase += 1
    return n_increase


def problem2(filename):
    with open(filename) as f:
        data = [int(x) for x in f.readlines()]

    stack = []
    for i in range(len(data)-2):
        stack.append(sum(data[i:i+3]))

    n_increase = 0
    for i in range(1, len(stack)):
        if stack[i] > stack[i-1]:
            n_increase += 1
    return n_increase


if __name__ == '__main__':
    filename = '../data/input_day1.txt'
    print(problem1(filename))
    print(problem2(filename))
