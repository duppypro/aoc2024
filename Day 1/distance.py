# Day 1 - Distance

import sys

# Initialize two arrays
array1 = []
array2 = []

# Read a text file from stdin, put first 2 integers from each line into two different arrays
for line in sys.stdin:
    num1, num2 = map(int, line.split())
    array1.append(int(num1))
    array2.append(int(num2))

array1.sort()
array2.sort()

# Now calculate the differences
differences = [abs(a - b) for a, b in zip(array1, array2)]

# sum the differences
total = sum(differences)

# Print the total
print(total)

# Print the arrays
# print("Array 1:", array1)
# print("Array 2:", array2)