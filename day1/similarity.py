# Day 1 - Similarity

import sys

# Initialize two arrays
array1 = []
appear_count = [0] * 100000  # Set the size of the array to 10000 elements, all initialized to 0

# Read a text file from stdin, put first 2 integers from each line into two different arrays
for line in sys.stdin:
    num1, num2 = map(int, line.split())
    array1.append(num1)
    appear_count[num2] += 1
    # print(array1, appear_count, "\n")


# Now calculate the similarity score
similarity = [n*appear_count[n] for n in array1]
# print("similarity", similarity)

# sum the similarities
total = sum(similarity)

# Print the total
print(total)

# Print the arrays
# print("Array 1:", array1)
# print("Array 2:", array2)