
class Decoder:

    def __init__(self, filename):
        self.load_data(filename)

    def load_data(self, filename):
        with open(filename) as f:
            data = f.readlines()
        self.pairs = [[x.split() for x in d.split('|')] for d in data]

    def count_unique_values(self):
        n_unique = 0
        for pair in self.pairs:
            signal_pattern, output_value = pair
            for output in output_value:
                if len(output) in [2, 4, 3, 7]:
                    n_unique += 1
        return n_unique

    def decode_all(self):
        output = 0
        for pair in self.pairs:
            output += self.decode_output(pair[0], pair[1])
        return output

    def decode_output(self, signal_pattern, output_value):
        dict_values = {}
        dict_values[1] = set(
            [x for x in signal_pattern if len(x) == 2][0]
        )
        dict_values[4] = set(
            [x for x in signal_pattern if len(x) == 4][0]
        )
        dict_values[7] = set(
            [x for x in signal_pattern if len(x) == 3][0]
        )
        dict_values[8] = set(
            [x for x in signal_pattern if len(x) == 7][0]
        )
        dict_values[6] = set(
            [x for x in signal_pattern if len(x) == 6
             and not dict_values[1].issubset(x)][0]
        )
        dict_values[3] = set(
            [x for x in signal_pattern if len(x) == 5
             and dict_values[1].issubset(x)][0]
        )
        dict_values[9] = set(
            [x for x in signal_pattern if len(x) == 6
             and dict_values[4].issubset(x)][0]
        )
        dict_values[0] = set(
            [x for x in signal_pattern if len(x) == 6
             and (dict_values[9] != set(x))
             and (dict_values[6] != set(x))][0]
        )
        dict_values[5] = set(
            [x for x in signal_pattern if len(x) == 5
             and set(x).issubset(dict_values[6])][0]
        )
        dict_values[2] = set(
            [x for x in signal_pattern if len(x) == 5
             and (dict_values[5] != set(x))
             and (dict_values[3] != set(x))][0]
        )

        output = ''
        for val in output_value:
            output += str([key for key in dict_values
                           if dict_values[key] == set(val)][0])
        return int(output)


if __name__ == "__main__":
    decoder = Decoder('../data/test_day8.txt')
    print(decoder.count_unique_values())
    print(decoder.decode_all())

    decoder = Decoder('../data/input_day8.txt')
    print(decoder.count_unique_values())
    print(decoder.decode_all())
