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

# fill a grid from stdin
grid = []
for line in sys.stdin:
    line = line.strip() # strip '\n' from line
    grid_width = len(line)
    grid += [line] # strip '\n' from line

print(grid)

def check(grid, start, dir):
    # print(start, dir, start[1]+dir[1], start[0]+dir[0])
    # print("\t", grid[start[1]][start[0]])
    # print("\t\t", grid[start[1]+dir[1]][start[0]+dir[0]])
    cursor = list(start)
    for i in range(word_length):
        if cursor[0] < 0 or cursor[1] < 0 or cursor[0] >= grid_width or cursor[1] >= len(grid):
            return 0
        if grid[cursor[1]][cursor[0]] != search_word[i]:
            return 0
        cursor[0] += dir[0]
        cursor[1] += dir[1]
    return 1

total = 0
for y in range(len(grid)):
    for x in range(grid_width):
        print(grid[y])
        print(' ' * x + grid[y][x])
        for dir in range(len(directions)):
            total += check(grid, (x, y), directions[dir])

print(total)