# Day 2 - Safe PART TWO

import sys

def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0

# return index of first unsafe level (0 is first level)
# IMNSHO, the problem is unclear on whether the first level can be unsafe or is it the second level that causes the unsafe?
# return -1 if all levels are safe
def where_unsafe(levels):
    prev_level = levels[0]
    change = levels[1] - prev_level
    direction = sign(change)
    change = abs(change)
    if change > 3 or change <= 0:
        return 1
    prev_level = levels[1]
    for where, level in enumerate(levels[2:]):
        # print(where, prev_level, level)
        new_direction = sign(level - prev_level)
        if new_direction != direction:
            return where + 2
        if abs(level - prev_level) > 3:
            return where + 2
        prev_level = level
    return -1 # all levels are safe

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
    where = where_unsafe(levels)
    print(f"{where} = where_unsafe({levels})")
    tryB = where - 1
    tryC = where + 1
    if where != -1:
        lvl_removed = levels.copy()
        lvl_removed.pop(where)
        where = where_unsafe(lvl_removed)
        print(f" A {where} = where_unsafe({lvl_removed})")
        if where != -1:
            lvl_removed = levels.copy()
            lvl_removed.pop(tryB)
            where = where_unsafe(lvl_removed)
            print(f" B {where} = where_unsafe({lvl_removed})")
            if where != -1:
                lvl_removed = levels.copy()
                lvl_removed.pop(tryC)
                where = where_unsafe(lvl_removed)
                print(f" C {where} = where_unsafe({lvl_removed})")
    if where == -1:
        safe_count += 1
        # print("Count is now: ", safe_count)
# END for line

print("Final count is: ", safe_count)