import pytest
from solutions.day4 import Board, load_board_data


def test_load_data():
    with open('./data/test_day4.txt', 'r') as f:
        data = f.readlines()
        numbers, boards = load_board_data(data)

    assert(len(numbers) == 27)
    assert(isinstance(numbers[0], int))

    assert(len(boards) == 3)
    for board in boards:
        assert(len(board) == 5)
        assert(len(board[0]) == 5)


def test_Board():
    with open('./data/test_day4.txt', 'r') as f:
        data = f.readlines()
        numbers, boards = load_board_data(data)

    boards = [Board(x) for x in boards]
    assert(len(boards[0].board) == 5)
    assert(len(boards[0].board[0]) == 5)

    for number in numbers[:12]:
        for board in boards:
            board.mark_number(number)

    assert(not boards[0].check_board())
    assert(not boards[1].check_board())
    assert(boards[2].check_board())

    assert(boards[2].score_board() == 188)

    vertical_board = Board([[1, 1, 1, 5, 1] for _ in range(5)])
    vertical_board.mark_number(5)
    assert(vertical_board.check_board())
