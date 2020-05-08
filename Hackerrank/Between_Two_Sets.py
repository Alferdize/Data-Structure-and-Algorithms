#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    x=a[-1]
    y=b[0]
    count=0
    for p in range(x,y+1):
        chk=0
        for i in b:
            if i%p!=0:
                chk=1
                break
        chk1=0
        for i in a:
            if p%i!=0:
                chk1=1
                break
        if chk==0 and chk1==0:
            count+=1
    return count
    


    # Write your code here

if __name__ == '__main__':
    fptr = open("Between_Two_Sets.txt", 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
