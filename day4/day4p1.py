# Day 4: Part One

# MMMSXXMASM
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX

# In this word search, XMAS occurs a total of 18 times

import sys

search_word = "XMAS"
# CONSTRAINT: pad_char must not be in search_word
pad_char = "."
word_length = len(search_word)
directions = (
    (-1, 0),  # left
    (-1, -1),  # left-up
    (0, -1),  # up
    (1, -1),  # right-up
    (1, 0),  # right
    (1, 1),  # right-down
    (0, 1),  # down
    (-1, 1),  # left-down
)

# make grid larger than input by word_length on each side
# CONSTRAINT: Assumes input is no larger than 140x140
grid_size = 16
# Initialize a grid of grid_size tuples of grid_size pad_char
grid = [pad_char * grid_size] * grid_size

# fill the center of it from stdin
x = word_length - 1
y = word_length - 1
for line in sys.stdin:
    grid[y] = grid[y][:x] + line.strip() + grid[y][grid_size-word_length+1:]
    y += 1

print(grid)
y = word_length - 1

def check(grid, start, dir):
    print(dir, grid[start[1]][start[0]], grid[start[1]+dir[1]][start[0]+dir[0]])
    return True

for y in range(word_length-1, grid_size - word_length + 1):
    for x in range(word_length-1, grid_size - word_length + 1):
        for dir in range(len(directions)):
            check(grid, (x, y), directions[dir])