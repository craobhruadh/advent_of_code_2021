from collections import Counter


class LanternFish:
    def __init__(self, timer=8):
        self.timer = timer

    def iterate(self):
        if self.timer == 0:
            self.timer = 6
            return True
        else:
            self.timer -= 1
            return False


def simulate_fish(data, n_days):
    fish = []
    for d in data:
        fish.append(LanternFish(timer=d))

    for day in range(n_days):
        new_fish = 0
        for f in fish:
            if f.iterate():
                new_fish += 1
        for _ in range(new_fish):
            fish.append(LanternFish())

    return len(fish)


def simulate_fish_counter(data, n_days):
    """You tricked us advent of code!  Doing it via hashmap"""
    c = Counter(data)

    for _ in range(n_days):
        new_fish = c[0]
        keys = [x for x in sorted(c.keys()) if x != 0]
        for key in keys:
            c[key - 1] = c[key]
            c[key] = 0
        c[6] += new_fish
        c[8] += new_fish

    total = 0
    for key in c.keys():
        total += c[key]
    return total


def read_data(file):
    with open(file) as f:
        data = [int(x) for x in f.read().split(",")]
    return data


if __name__ == "__main__":
    data = read_data("../data/test_day6.txt")
    print(simulate_fish(data, 18))
    print(simulate_fish_counter(data, 18))
    print(simulate_fish_counter(data, 80))
    print(simulate_fish_counter(data, 256))

    data = read_data("../data/input_day6.txt")
    print(simulate_fish_counter(data, 80))
    print(simulate_fish_counter(data, 256))

    # This takes too long and will fill your hard drive, don't run it
    # print(simulate_fish(data, 256))
