#!/bin/python3

import math
import os
import random
import re
import sys

# Function Description

# Complete the repeatedString function in the editor below.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Returns

# int: the frequency of a in the substring
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

def repeatedString(s, n):
    if not "a" in s:
        return 0

    if len(s) == 1 and s == "a":
        return n

    def a_in_str(sg):
        return len([l for l in list(sg) if l == "a"])

    if len(s) > n:
        return a_in_str(s[:n])

    count = 0
    m = n // len(s)
    count += m * a_in_str(s)
    count += a_in_str(s[:n-(len(s) * m)])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
