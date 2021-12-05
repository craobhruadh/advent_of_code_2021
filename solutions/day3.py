from collections import Counter


def find_epsilon_and_gamma(data):
    n_chars = len(data[0])
    gamma = ''
    epsilon = ''
    for i in range(n_chars):
        c = Counter([x[i:i+1] for x in data])
        if c['1'] > c['0']:
            gamma += '1'
            epsilon += '0'
        elif c['1'] < c['0']:
            epsilon += '1'
            gamma += '0'
        else:
            Exception('equal numbers of 0 and 1')
    print(gamma, epsilon)
    print(int(gamma, 2), int(epsilon, 2))
    print(int(gamma, 2) * int(epsilon, 2))


def find_oxygen(data):
    n_chars = len(data[0])
    i = 0
    tolerance = n_chars * len(data)
    count = 0
    while len(data) > 1:
        c = Counter([x[i:i+1] for x in data])
        if c['1'] >= c['0']:
            data = [x for x in data if x[i:i+1] == '1']
        elif c['1'] < c['0']:
            data = [x for x in data if x[i:i+1] == '0']
        i += 1
        i = i % n_chars
        count += 1
        if count == tolerance:
            Exception('Too many iterations!')

    print('Oxygen: ', count, data, int(data[0], 2))
    return int(data[0], 2)


def find_CO2(data):
    n_chars = len(data[0])
    i = 0
    tolerance = n_chars * len(data)
    count = 0
    while len(data) > 1:
        c = Counter([x[i:i+1] for x in data])
        if c['0'] <= c['1']:
            data = [x for x in data if x[i:i+1] == '0']
        elif c['1'] < c['0']:
            data = [x for x in data if x[i:i+1] == '1']
        i += 1
        i = i % n_chars
        count += 1
        if count == tolerance:
            Exception('Too many iterations!')

    print('CO2: ', count, data, int(data[0], 2))
    return int(data[0], 2)


if __name__ == '__main__':
    with open('./data/input_day3.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    find_epsilon_and_gamma(data)

    print(find_oxygen(data) * find_CO2(data))
