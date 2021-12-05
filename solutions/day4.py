
class Board:

    def __init__(self, board):
        self.m, self.n = 5, 5

        assert(len(board) == self.m)
        for b in board:
            assert(len(b) == self.n)

        self.board = board
        self.marked = [[False] * self.n for _ in range(self.m)]

    def mark_number(self, number):
        for i in range(self.m):
            for j in range(self.n):
                if self.board[i][j] == number:
                    self.marked[i][j] = True

        return self.check_board()

    def check_board(self):
        for i in range(self.m):
            if all(self.marked[i]):
                return True

        for j in range(self.n):
            column = [x[j] for x in self.marked]
            if all(column):
                return True
        return False

    def score_board(self):
        total = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.marked[i][j]:
                    total += self.board[i][j]
        return total


def load_board_data(data):
    numbers = [int(x) for x in data[0].split(',')]
    boards = [[int(y) for y in x.split()] for x in data[2:]]

    all_boards = []
    n = 5
    while boards:
        this_board = boards[:n]
        boards = boards[n:]
        if boards and len(boards[0]) == 0:
            boards = boards[1:]
        all_boards.append(this_board)
    return numbers, all_boards


def find_first_winning_board(numbers, boards):
    boards = [Board(x) for x in boards]

    found_winner = False
    output = []
    for number in numbers:
        for board in boards:
            board.mark_number(number)
            if board.check_board():
                output.append((number, board.score_board()))
                found_winner = True
        if found_winner:
            if len(output) > 1:
                Exception('More than one solution!  Should this be able to handle it?')
            else:
                return output[0]
    return -1, -1


def find_last_winning_board(numbers, boards):
    boards = [Board(x) for x in boards]

    last_winner = None
    for number in numbers:
        new_boards = []
        for board in boards:
            board.mark_number(number)
            if board.check_board():
                last_winner = (number, board.score_board())
            else:
                new_boards.append(board)
        if new_boards:
            boards = new_boards
        else:
            break
    return last_winner


if __name__ == '__main__':
    with open('../data/input_day4.txt', 'r') as f:
        data = f.readlines()
        numbers, boards = load_board_data(data)

    print(find_first_winning_board(numbers, boards))
    print(find_last_winning_board(numbers, boards))
