# Day 2 - Safe PART TWO

import sys

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

levels = [] # set array type
safe_count = 0

# Read a text file from stdin
for line in sys.stdin:
    # Split the line into a list of integers
    levels = list(map(int, line.split()))
    # print(levels)

# safe if both of the following are true:

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# In the example above, the reports can be found safe or unsafe by checking those rules:

# 7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
# 1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
# 9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
# 1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
# 8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
# 1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
# So, in this example, 2 reports are safe.

    # assume safe until proven otherwise
    safe = 1
    direction = 0 # 0 implies unknown
    restore_direction = direction
    # set prev_level to the first number in the list
    prev_level = levels[0]
    level_removed = 0
    
    for lvl in levels[1:]:
        new_direction = sign(lvl - prev_level)
        restore_direction = direction # save old direction in case we remove this level
        if direction == 0: # if the direction hasn't been set yet
            direction = new_direction
        # if the current number equals the previous number, then it's unsafe
        if direction == 0:
            safe = 0
        else:
            if new_direction != direction:
                safe = 0
        # check magnitude of change
        if abs(lvl - prev_level) > 3:
            safe = 0
        # END of loop cleanup
        if (level_removed == 0 and safe == 0):
            level_removed = 1 # can only do this once
            direction = restore_direction
            safe = 1
            continue # don't update prev_level
        # set prev_level to the current number
        prev_level = lvl 
        if safe == 0:
            break
    # END for lvl
    
    safe_count += safe # CONSTRAINT: safe is either 1 or 0
    # print(safe_count)

# END for line

print(safe_count)