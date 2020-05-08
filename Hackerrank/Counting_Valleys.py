#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    height = 0
    prev_height = 0
    cnt = 0
    for i in range(len(s)):
        if (s[i] == 'U'):
            height += 1
        elif s[i] == 'D':
            height -= 1
        if height == 0 and prev_height < 0:
            cnt += 1
        prev_height = height
    return cnt

if __name__ == '__main__':
    fptr = open("Counting_Valleys.txt", 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
