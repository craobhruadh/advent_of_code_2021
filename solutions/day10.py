class SyntaxChecker:

    pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
    score = {")": 3, "]": 57, "}": 1197, ">": 25137}
    completion_score = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4,
    }

    def __init__(self, filename):
        with open(filename) as f:
            self.data = [x.strip() for x in f.readlines()]
        self.reverse_pairs = {self.pairs[k]: k for k in self.pairs}

    def check_line(self, line):
        """return -1 if it's fine"""
        stack = []
        for c in line:
            if c in self.pairs.keys():
                stack.append(c)
            else:
                if stack:
                    if self.reverse_pairs[c] == stack[-1]:
                        stack.pop()
                    else:
                        return self.score[c]
                else:
                    return self.score[c]
        return -1

    def score_syntax_checker(self, verbose=False):
        error_score = 0
        for line in self.data:
            score = self.check_line(line)
            if score != -1:
                error_score += score
            if verbose:
                print(f"{line}: {score}")
        return error_score

    def autocomplete_line(self, line):
        score = 0
        stack = []
        for c in line:
            if c in self.pairs.keys():
                stack.append(c)
            elif c in self.reverse_pairs.keys():
                stack.pop()
            else:
                raise Exception("This string is corrupted")
        while stack:
            score *= 5
            score += self.completion_score[self.pairs[stack[-1]]]
            stack.pop()
        return score

    def autocomplete_data(self):
        incomplete = [x for x in self.data if self.check_line(x) == -1]
        all_scores = []
        for line in incomplete:
            all_scores.append(self.autocomplete_line(line))
        return sorted(all_scores)[len(all_scores) // 2]


if __name__ == "__main__":
    checker = SyntaxChecker("../data/test_day10.txt")
    print(checker.score_syntax_checker())
    print(checker.autocomplete_data())

    checker = SyntaxChecker("../data/input_day10.txt")
    print(checker.score_syntax_checker())
    print(checker.autocomplete_data())
