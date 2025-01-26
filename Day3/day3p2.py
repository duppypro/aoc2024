# Day 3: Part 2 Mull It Over
# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

# There are two new instructions you'll need to handle:

# The do() instruction enables future mul instructions.
# The don't() instruction disables future mul instructions.
# Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

# For example:

# xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
# This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

# This time, the sum of the results is 48 (2*4 + 8*5).

# Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?

import sys
# use regular expressions
import re

def process(line):
    # use regex to find strings matching mul(x,y)
    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, line)
    total = 0
    for match in matches:
        ints =  re.findall(r'\d+', match)
        print(ints)
        total += int(ints[0]) * int(ints[1])
    return total

def preprocess(line):
    # remove everything between 'don't()' and 'do()'
    pattern = r'don\'t\(\)(.*?)do\(\)'
    post = re.sub(pattern, '', line)
    print(line, "->", post)
    return post

total = 0
for line in sys.stdin:
    total += process(preprocess(line))
    
print("Sum of all ENABLED mul instructions is: ", total)
