"""You are given a result of a game and you must determine if the game ends in a win or a draw as well as who will be the winner. Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
A game's result is presented as a list of strings, where "X" and "O" are players' marks and "." is the empty cell.

Input: A game result as a list of strings (unicode).
Output: "X", "O" or "D" as a string.
Precondition:
There is either one winner or a draw.
len(game_result) == 3
all(len(row) == 3 for row in game_result)"""

from typing import List


def checkio(game_result: List[str]) -> str:
    board = []
    for row in game_result:
        for c in row:
            board += c

    if (board[0] == board[1] == board[2] or  board[0] == board[3] == board[6] or board[0] == board[4] == board[8]) and (board[0] == 'X' or board[0] == 'O'):
        return board[0]
    elif (board[3] == board[4] == board[5] or board[1] == board[4] == board[7] or board[2] == board[4] == board[6]) and (board[4] == 'X' or board[4] == 'O'):
        return board[4]
    elif (board[6] == board[7] == board[8] or board[2] == board[5] == board[8]) and (board[8] == 'X' or board[8] == 'O'):
        return board[8]
    else:
        return 'D'
if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
