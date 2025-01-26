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

# if removing a single level from an unsafe report would make it safe, the report instead counts as safe.
# More of the above example's reports are now safe:

# 7 6 4 2 1: Safe without removing any level.
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.

# Thanks to the Problem Dampener, 4 reports are actually safe!

    safe = 1 # assume safe until proven otherwise
    level_removed = 0 # haven't removed a level yet
    prev_level = levels[0]
    direction = sign(levels[1] - prev_level)
    print_result = False
    # special case: first level
    if direction == 0 or abs(levels[1] - prev_level) > 3:
        print(levels)
        levels.pop(0)
        print("\tnew: ", levels)
        safe = 1
        level_removed = 1
        prev_level = levels[0]
        direction = sign(levels[1] - prev_level)
        print_result = True
    for lvl in levels[1:]:
        new_direction = sign(lvl - prev_level)
        if new_direction == 0 or new_direction != direction:
            safe = 0
        if abs(lvl - prev_level) > 3:
            safe = 0
        if (safe == 0 and level_removed == 1):
            break
        if (level_removed == 0 and safe == 0):
            level_removed = 1 # can only do this once
            safe = 1
        else:
            prev_level = lvl
    # END for lvl
    
    safe_count += safe # CONSTRAINT: safe is either 1 or 0
    if print_result:
        print("\t", safe_count, "this: ", safe, "\n")

# END for line

print(safe_count)