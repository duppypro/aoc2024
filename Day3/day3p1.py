# Day 3: Part 1 Mull It Over
# However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

# For example, consider the following section of corrupted memory:

# xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
# Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

# Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

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

total = 0
for line in sys.stdin:
    total += process(line)
    
print("Sum of all mul instructions is: ", total)
