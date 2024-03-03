# Built
from helper import place_queen_np, space_open_np

# Pre-Built
import random
import numpy as np

best_num_queens = 0
best_coord_list = []
iterations = 1000

print(f"Running {iterations} times")
for _ in range(iterations):
    # 0 represents that queen can be places in that space
    board = np.zeros((8, 8), int)
    num_queens = 0
    coord_list = []
    while space_open_np(board):
        coords_valid = False
        random_num_x = -1
        random_num_y = -1
        # We know that there is a open space
        # So loop through random coords until it finds a valid one, and place a queen there
        while coords_valid == False:
            random_num_x = random.randint(0, 7)
            random_num_y = random.randint(0, 7)
            if board[random_num_x, random_num_y] == 0:
                coords_valid = True
            else:
                coords_valid = False
        # Place queen in space
        coord_list.append((random_num_x, random_num_y))
        place_queen_np(board, (random_num_x, random_num_y))
        num_queens += 1

    print(f"Ending number of queens: {num_queens}")
    if num_queens > best_num_queens:
        best_num_queens = num_queens
        best_coord_list = coord_list

print("Best number of queens: ", best_num_queens)
print("Coord list")
print(best_coord_list)
