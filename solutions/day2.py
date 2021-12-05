
def find_position(data):
    position, depth = 0, 0

    for d in data:
        command, distance = d.split()
        distance = int(distance)
        if command == 'forward':
            position += distance
        elif command == 'up':
            depth -= distance
        elif command == 'down':
            depth += distance

    return position, depth


def find_position_and_aim(data):
    position, depth, aim = 0, 0, 0

    for d in data:
        command, distance = d.split()
        distance = int(distance)
        if command == 'forward':
            position += distance
            depth += aim*distance
        elif command == 'up':
            aim -= distance
        elif command == 'down':
            aim += distance

    return position, depth


if __name__ == '__main__':
    with open('./data/input_day2.txt', 'r') as f:
        data = [x.strip() for x in f.readlines()]

    position, depth = find_position(data)
    print(position, depth, position * depth)

    position, depth = find_position_and_aim(data)
    print(position, depth, position * depth)
