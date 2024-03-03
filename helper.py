import numpy as np


def space_open_np(board):
    return np.any(board == 0)


# Calculates differnce between 2 numbers
def calculate_diff(num1: int, num2: int):
    if num2 - num1 == 0:
        return 0
    # Return the difference (as a positive number)
    elif num2 - num1 < 0:
        return num1 - num2
    else:
        return num2 - num1


# list[list[int]] tuple[int]
def place_queen_np(board, coords):
    x_coord = coords[0]
    y_coord = coords[1]

    # Gets rid of row
    board[x_coord, :] = [1 for _ in range(8)]

    # Get rid of column
    board[:, y_coord] = [1 for _ in range(8)]

    # Remove diagnols - cba to figure out a good way to do this, can add row and column into this
    board_shape = board.shape
    for x in range(board_shape[0]):
        for y in range(board_shape[1]):
            # If the differnce between the two axis is equal, then it is on a diagnol
            if calculate_diff(x, x_coord) == calculate_diff(y, y_coord):
                board[x, y] = 1


if __name__ == "__main__":
    print("Helper for queen problem")
